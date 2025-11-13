import os
from app.vector_db.store_manager import store_manager

"""
This script loads sample best-practice texts into FAISS vector DB.

Run:
    python scripts/load_sample_vectors.py
"""

examples = [
    "Use parameterized SQL queries to avoid SQL injection.",
    "Avoid using eval() and exec() as they can lead to security vulnerabilities.",
    "Use descriptive variable names to improve code readability.",
    "Avoid nested loops when a single-pass alternative exists.",
    "Cache expensive operations to improve performance in large datasets.",
]

def main():
    print("Loading sample vectors into FAISS database...")
    for text in examples:
        store_manager.add_text(text)
    print("Done.")

if __name__ == "__main__":
    main()
