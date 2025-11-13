from typing import List, Dict
from app.agents.base_agent import BaseAgent
from app.core.prompt_templates import LOGIC_PROMPT


class LogicAgent(BaseAgent):

    async def analyze(self, code: str, file_path: str) -> List[Dict]:
        if not code.strip():
            return []

        prompt = LOGIC_PROMPT.format(code=code)
        issues = await self.run_prompt(prompt)

        if not isinstance(issues, list):
            return []

        formatted = []
        for item in issues:
            formatted.append({
                "file": file_path,
                "line": item.get("line"),
                "category": "logic",
                "issue": item.get("issue"),
                "suggestion": item.get("suggestion"),
                "explanation": item.get("explanation"),
            })

        return formatted
