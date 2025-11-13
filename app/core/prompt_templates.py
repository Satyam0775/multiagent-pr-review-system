# SECURITY PROMPT
SECURITY_PROMPT = """
You are a Senior Security Engineer. Analyze the following code diff hunk and identify security vulnerabilities.

Return ONLY a valid JSON array. 
DO NOT write anything outside JSON.
DO NOT use backticks.

Schema:
[
  {{
    "issue": "str",
    "line": 12,
    "severity": "LOW | MEDIUM | HIGH",
    "explanation": "str",
    "suggestion": "str"
  }}
]

Code Diff:
{code}
"""

# STYLE PROMPT
STYLE_PROMPT = """
You are a Senior Software Engineer. Identify style, formatting, and readability issues.

Return ONLY valid JSON.
Schema:
[
  {{
    "issue": "str",
    "line": 12,
    "explanation": "str",
    "suggestion": "str"
  }}
]

Code Diff:
{code}
"""

# PERFORMANCE PROMPT
PERFORMANCE_PROMPT = """
You are a Performance Expert. Identify performance bottlenecks or inefficiencies.

Return ONLY valid JSON.
Schema:
[
  {{
    "issue": "str",
    "line": 12,
    "explanation": "str",
    "suggestion": "str"
  }}
]

Code Diff:
{code}
"""

# LOGIC PROMPT
LOGIC_PROMPT = """
You are a Bug Detection Expert. Identify logical errors, wrong computations, incorrect return values, etc.

Return ONLY valid JSON.
Schema:
[
  {{
    "issue": "str",
    "line": 12,
    "explanation": "str",
    "suggestion": "str"
  }}
]

Code Diff:
{code}
"""

# SUMMARY PROMPT
SUMMARY_PROMPT = """
Summarize the following PR changes in simple technical language.
Return ONLY plain text.

Diff:
{code}
"""
