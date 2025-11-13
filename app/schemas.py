from pydantic import BaseModel
from typing import List, Optional

class DiffRequest(BaseModel):
    diff: str


class PRRequest(BaseModel):
    owner: str
    repo: str
    pr_number: int


class ReviewComment(BaseModel):
    file: str
    line: Optional[int]
    category: str
    issue: str
    suggestion: Optional[str]
    explanation: Optional[str]
    severity: Optional[str] = None


class ReviewResponse(BaseModel):
    summary: str
    total_comments: int
    comments: List[ReviewComment]
