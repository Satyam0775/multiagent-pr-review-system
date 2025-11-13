from abc import ABC, abstractmethod
from typing import List, Dict
from app.core.tool_registry import tools
import json, re


class BaseAgent(ABC):

    @abstractmethod
    async def analyze(self, code: str, file_path: str) -> List[Dict]:
        pass

    async def run_prompt(self, prompt: str) -> List[Dict]:
        response = await tools.run_llm(prompt)
        return self.extract_json_array(response)

    def extract_json_array(self, text: str):
        try:
            match = re.search(r"\[(.|\s)*?\]", text)
            if match:
                return json.loads(match.group(0))
            return []
        except:
            return []
