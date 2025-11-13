from fastapi import FastAPI, HTTPException, Header
from app.schemas import DiffRequest, PRRequest, ReviewResponse
from app.core.orchestrator import orchestrator
from app.clients.github_client import github_client
from app.storage.cache_manager import cache_manager
from app.storage.local_store import local_store
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Automated GitHub PR Review Agent"
)

@app.post("/review/diff", response_model=ReviewResponse)
async def review_diff(
    req: DiffRequest,
    bypass_cache: bool = Header(default=False)
):
    diff_text = req.diff

    if not bypass_cache and cache_manager.exists(diff_text):
        return cache_manager.load(diff_text)

    result = await orchestrator.run(diff_text)

    cache_manager.save(diff_text, result)
    local_store.save_diff(diff_text)
    local_store.save_review(result)

    return result


@app.post("/review/pr", response_model=ReviewResponse)
async def review_pr(
    req: PRRequest,
    bypass_cache: bool = Header(default=False)
):
    try:
        diff_text = github_client.get_pr_diff(
            req.owner, req.repo, req.pr_number
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not bypass_cache and cache_manager.exists(diff_text):
        return cache_manager.load(diff_text)

    result = await orchestrator.run(diff_text)

    cache_manager.save(diff_text, result)
    local_store.save_diff(diff_text)
    local_store.save_review(result)

    return result


@app.get("/")
def root():
    return {"message": "PR Review Agent Running Successfully!"}
