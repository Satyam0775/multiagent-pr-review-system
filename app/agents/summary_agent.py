from app.agents.base_agent import BaseAgent
from app.core.prompt_templates import SUMMARY_PROMPT
from app.core.tool_registry import tools


class SummaryAgent(BaseAgent):

    async def analyze(self, code: str, file_path: str):
        return []

    async def summarize(self, diff_text: str) -> str:
        prompt = SUMMARY_PROMPT.format(code=diff_text)

        # Use tool_registry directly for text (NOT run_prompt)
        response = await tools.run_llm(prompt)

        return str(response).strip()
