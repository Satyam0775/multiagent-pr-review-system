import pytest
from unittest.mock import AsyncMock, patch

from app.agents.security_agent import SecurityAgent
from app.agents.style_agent import StyleAgent
from app.agents.logic_agent import LogicAgent
from app.agents.performance_agent import PerformanceAgent


MOCK_RESPONSE = '[{"issue": "Test Issue", "line": 5, "suggestion": "Fix it", "severity": "HIGH"}]'

@pytest.mark.asyncio
@patch("app.core.tool_registry.tools.run_llm", new_callable=AsyncMock)
async def test_security_agent(mock_llm):
    mock_llm.return_value = MOCK_RESPONSE
    
    agent = SecurityAgent()
    result = await agent.analyze("+ dangerous_code()", "file.py")

    assert len(result) == 1
    assert result[0]["category"] == "security"


@pytest.mark.asyncio
@patch("app.core.tool_registry.tools.run_llm", new_callable=AsyncMock)
async def test_style_agent(mock_llm):
    mock_llm.return_value = MOCK_RESPONSE
    
    agent = StyleAgent()
    result = await agent.analyze("+ bad_style()", "file.py")

    assert len(result) == 1
    assert result[0]["category"] == "style"


@pytest.mark.asyncio
@patch("app.core.tool_registry.tools.run_llm", new_callable=AsyncMock)
async def test_logic_agent(mock_llm):
    mock_llm.return_value = MOCK_RESPONSE
    
    agent = LogicAgent()
    result = await agent.analyze("+ wrong_logic()", "file.py")

    assert len(result) == 1
    assert result[0]["category"] == "logic"


@pytest.mark.asyncio
@patch("app.core.tool_registry.tools.run_llm", new_callable=AsyncMock)
async def test_performance_agent(mock_llm):
    mock_llm.return_value = MOCK_RESPONSE
    
    agent = PerformanceAgent()
    result = await agent.analyze("+ loop()", "file.py")

    assert len(result) == 1
    assert result[0]["category"] == "performance"
