from github import Github
from app.config import settings
from loguru import logger

class GitHubClient:
    def __init__(self):
        if not settings.GITHUB_TOKEN:
            raise ValueError("GITHUB_TOKEN not found in environment variables")

        self.client = Github(settings.GITHUB_TOKEN)

    def get_pr_diff(self, owner: str, repo: str, pr_number: int) -> str:
        """
        Fetch PR diff from GitHub.
        Returns unified diff string.
        """
        try:
            repository = self.client.get_repo(f"{owner}/{repo}")
            pr = repository.get_pull(pr_number)
            diff = pr.patch  # unified diff
            logger.info(f"Fetched PR diff for {owner}/{repo}#{pr_number}")
            return diff
        except Exception as e:
            logger.error(f"Failed to fetch PR diff: {e}")
            raise

github_client = GitHubClient()
