from app.core.diff_parser import parse_diff

def test_parse_basic_diff():
    diff = """diff --git a/test.py b/test.py
@@ -1,2 +1,2 @@
- old line
+ new line
"""
    result = parse_diff(diff)

    assert len(result) == 1
    assert result[0]["file_path"] == "test.py"
    assert len(result[0]["hunks"]) == 1

    hunk = result[0]["hunks"][0]
    assert len(hunk["added_lines"]) == 1
    assert len(hunk["removed_lines"]) == 1
