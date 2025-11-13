from typing import List, Dict
from app.agents.base_agent import BaseAgent
from app.core.prompt_templates import SECURITY_PROMPT


class SecurityAgent(BaseAgent):

    async def analyze(self, code: str, file_path: str) -> List[Dict]:
        if not code.strip():
            return []

        prompt = SECURITY_PROMPT.format(code=code)
        issues = await self.run_prompt(prompt)

        if not isinstance(issues, list):
            return []

        formatted = []
        for item in issues:
            formatted.append({
                "file": file_path,
                "line": item.get("line"),
                "category": "security",
                "severity": item.get("severity", "MEDIUM"),
                "issue": item.get("issue"),
                "suggestion": item.get("suggestion"),
                "explanation": item.get("explanation"),
            })

        return formatted
