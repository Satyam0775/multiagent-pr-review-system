# 🚀 Multi-Agent Pull Request Review System (Gemini-Powered)

This project implements an intelligent **Pull Request Review System** using a **multi-agent architecture** powered by **Google Gemini 2.0 Flash**.

The backend analyzes GitHub diffs, passes them through four specialized agents, and returns structured JSON feedback that includes security, logic, performance, and style issues.

---

## 🧠 What the System Does

Whenever a diff is submitted, the backend:

1. **Parses the unified Git diff** into files and hunks.
2. Sends each hunk to **four LLM-powered agents**:
   - 🔐 Security Agent  
   - 🧠 Logic Agent  
   - ⚡ Performance Agent  
   - 🎨 Style Agent  
3. Generates:
   - A technical **summary** of the PR
   - A count of **total comments**
   - A list of all **agent-generated review comments**
4. Returns all output in a **strict JSON format**.

---

## 🏗 System Architecture

### ✔ Diff Parsing Engine  
Extracts:
- Added lines  
- Removed lines  
- Context lines  
- File sections & hunks  

### ✔ Multi-Agent Review Pipeline  
Each agent uses a specialized Gemini prompt template to produce structured review objects:
- `issue`
- `line`
- `file`
- `category`
- `explanation`
- `suggestion`
- `severity` (security only)

### ✔ JSON-Safe Execution  
All agents use:
- Strict JSON prompting  
- Regex-based extraction  
- Failure-safe parsing  

### ✔ Caching Layer  
SHA256(cache_key) → JSON  
Prevents reprocessing of identical diffs.

---

## 🛠 Tech Stack

| Component | Technology |
|----------|------------|
| Backend Framework | FastAPI |
| LLM | Google Gemini 2.0 Flash |
| Settings | Pydantic v2 + pydantic-settings |
| Server | Uvicorn |
| Logging | Loguru |
| Cache | Local SHA256 file cache |
| Storage | Local JSON file store |

---

## 📦 Installation

```bash
git clone https://github.com/Satyam0775/multiagent-pr-review-system
cd multiagent-pr-review-system

python -m venv .venv
.venv\Scripts\activate

pip install -r requirements.txt
🔧 Environment Setup

Create a .env file based on .env.example:

GEMINI_API_KEY=your_api_key
GEMINI_MODEL=gemini-2.0-flash

▶ Run the Server
uvicorn app.main:app --reload


Server will start at:

👉 http://127.0.0.1:8000

📤 API Usage
POST /review/diff

Send raw Git diff text.

Request Example:
{
  "diff": "diff --git a/app.py b/app.py\n@@ -1,4 +1,4 @@\n def process(data):\n-    return [x * 100 for x in data]\n+    return [x * 1000 for x in data]\n"
}

Response Example:
{
  "summary": "The code changes the multiplication factor...",
  "total_comments": 4,
  "comments": [
    {
      "file": "app.py",
      "line": 2,
      "category": "security",
      "issue": "Potential Integer Overflow",
      "suggestion": "Consider using a safe multiplication function...",
      "explanation": "Multiplying by 1000 increases overflow risk.",
      "severity": "MEDIUM"
    }
  ]
}

📝 Example Diff Used During Testing
diff --git a/app.py b/app.py
index 83db48a..bf12a3c 100644
--- a/app.py
+++ b/app.py
@@ -1,4 +1,4 @@
 def process(data):
-    return [x * 100 for x in data]
+    return [x * 1000 for x in data]

📦 Output Summary

Your system correctly returned:

Summary of the PR

4 Total Comments
Security Issue
Logic Issue
Performance Issue
Style Issue
All in clean JSON format, ready for CI/CD pipelines or GitHub App integration.

🧑‍💻 Author
Satyam Kumar