import pytest
from unittest.mock import AsyncMock, patch
from app.core.orchestrator import orchestrator

MOCK_RESPONSE = '[{"issue": "Dummy", "line": 1, "suggestion": "Fix", "severity": "LOW"}]'

@pytest.mark.asyncio
@patch("app.core.tool_registry.tools.run_llm", new_callable=AsyncMock)
async def test_orchestrator_pipeline(mock_llm):
    mock_llm.return_value = MOCK_RESPONSE

    diff = """diff --git a/app.py b/app.py
@@ -1,1 +1,1 @@
- old
+ new
"""
    result = await orchestrator.run(diff)

    assert "summary" in result
    assert "comments" in result
    assert result["total_comments"] >= 1
