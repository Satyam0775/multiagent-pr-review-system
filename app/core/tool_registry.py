from app.clients.llm_gemini_client import GeminiClient


class ToolRegistry:
    def __init__(self):
        self.llm = GeminiClient()

    async def run_llm(self, prompt: str) -> str:
        return await self.llm.run(prompt)


tools = ToolRegistry()
