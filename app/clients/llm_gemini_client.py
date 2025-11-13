import google.generativeai as genai
from app.config import settings


class GeminiClient:
    """
    Unified Gemini LLM client used by all agents.
    Supports: JSON output + text output.
    """

    def __init__(self):
        genai.configure(api_key=settings.GEMINI_API_KEY)
        self.model_name = settings.GEMINI_MODEL

    async def run(self, prompt: str) -> str:
        """
        Automatically decides: JSON mode or text mode.
        """

        # JSON MODE DETECTION
        wants_json = (
            "JSON" in prompt
            or "json" in prompt
            or "Return ONLY a JSON" in prompt
            or "JSON array" in prompt
        )

        model = genai.GenerativeModel(self.model_name)

        if wants_json:
            response = model.generate_content(
                prompt,
                generation_config={
                    "response_mime_type": "application/json"
                }
            )
        else:
            response = model.generate_content(prompt)

        return response.text
