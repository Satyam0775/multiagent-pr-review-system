import re
from typing import List, Dict
from loguru import logger

DIFF_HEADER_RE = re.compile(r"diff --git a/(.*?) b/(.*?)")
HUNK_HEADER_RE = re.compile(r"@@ -(\d+),?(\d*) \+(\d+),?(\d*) @@")

class DiffParser:

    def parse_diff(self, diff_text: str) -> List[Dict]:
        files = []
        current_file = None
        current_hunk = None

        lines = diff_text.split("\n")

        for line in lines:

            # Detect file header
            file_match = DIFF_HEADER_RE.match(line)
            if file_match:
                if current_file:
                    files.append(current_file)

                file_path = file_match.group(2)
                current_file = {"file_path": file_path, "hunks": []}
                current_hunk = None
                continue

            # Detect hunk header
            hunk_match = HUNK_HEADER_RE.match(line)
            if hunk_match:
                if current_hunk:
                    current_file["hunks"].append(current_hunk)

                old_start = int(hunk_match.group(1))
                new_start = int(hunk_match.group(3))

                current_hunk = {
                    "old_start": old_start,
                    "new_start": new_start,
                    "added_lines": [],
                    "removed_lines": [],
                    "context_lines": []
                }
                continue

            # Add lines inside hunk
            if current_hunk:
                if line.startswith("+") and not line.startswith("+++"):
                    current_hunk["added_lines"].append((current_hunk["new_start"], line[1:]))
                    current_hunk["new_start"] += 1

                elif line.startswith("-") and not line.startswith("---"):
                    current_hunk["removed_lines"].append((current_hunk["old_start"], line[1:]))
                    current_hunk["old_start"] += 1

                else:
                    current_hunk["context_lines"].append((None, line))

        # Finalize last file
        if current_file:
            if current_hunk:
                current_file["hunks"].append(current_hunk)
            files.append(current_file)

        logger.info("Parsed diff into structured format")
        return files
