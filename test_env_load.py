import os
from dotenv import load_dotenv

load_dotenv()

print("Loaded GEMINI KEY:", os.getenv("GEMINI_API_KEY"))
print("Loaded GEMINI MODEL:", os.getenv("GEMINI_MODEL"))
