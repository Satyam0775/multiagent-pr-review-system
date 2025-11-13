import asyncio
from app.core.orchestrator import orchestrator
from app.storage.cache_manager import cache_manager
from app.storage.local_store import local_store

"""
Run a PR Review locally without FastAPI.

Usage:
    python scripts/run_local_review.py
"""

async def run_review():
    diff_path = "data/sample_diffs/sample.diff"

    with open(diff_path, "r", encoding="utf-8") as f:
        diff_text = f.read()

    print("Running multi-agent PR review...")
    result = await orchestrator.run(diff_text)

    print("\n=== SUMMARY ===")
    print(result["summary"])

    print("\n=== COMMENTS ===")
    for c in result["comments"]:
        print(
            f"[{c['category']}] {c['file']}:{c['line']} → {c['issue']}"
        )

    # Save outputs
    cache_manager.save(diff_text, result)
    local_store.save_review(result)

asyncio.run(run_review())
