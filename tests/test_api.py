from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    resp = client.get("/")
    assert resp.status_code == 200

def test_review_diff():
    diff = """diff --git a/a.py b/a.py
@@ -1 +1 @@
- x
+ y
"""
    resp = client.post("/review/diff", json={"diff": diff})
    assert resp.status_code == 200
    body = resp.json()
    assert "summary" in body
    assert "comments" in body
