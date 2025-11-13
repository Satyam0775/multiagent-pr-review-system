from app.core.diff_parser import DiffParser
from app.agents.security_agent import SecurityAgent
from app.agents.style_agent import StyleAgent
from app.agents.performance_agent import PerformanceAgent
from app.agents.logic_agent import LogicAgent
from app.agents.summary_agent import SummaryAgent
from app.agents.review_formatter import ReviewFormatter


class Orchestrator:

    def __init__(self):
        self.diff_parser = DiffParser()
        self.formatter = ReviewFormatter()

    async def run(self, diff_text: str):
        parsed_files = self.diff_parser.parse_diff(diff_text)

        security_comments = []
        style_comments = []
        performance_comments = []
        logic_comments = []

        for file_obj in parsed_files:
            file_path = file_obj["file_path"]

            for hunk in file_obj["hunks"]:
                code_block = self.hunk_to_text(hunk)

                sec = await SecurityAgent().analyze(code_block, file_path)
                sty = await StyleAgent().analyze(code_block, file_path)
                perf = await PerformanceAgent().analyze(code_block, file_path)
                log = await LogicAgent().analyze(code_block, file_path)

                security_comments.extend(sec)
                style_comments.extend(sty)
                performance_comments.extend(perf)
                logic_comments.extend(log)

        summary = await SummaryAgent().summarize(diff_text)

        return self.formatter.merge(
            summary,
            security_comments,
            logic_comments,
            performance_comments,
            style_comments
        )

    def hunk_to_text(self, hunk):
        added = [f"+ {line}" for _, line in hunk["added_lines"]]
        removed = [f"- {line}" for _, line in hunk["removed_lines"]]
        context = [f"  {line}" for _, line in hunk["context_lines"]]
        return "\n".join(context + added + removed)


# ⬇️ ⬇️ ⬇️  REQUIRED FOR IMPORT TO WORK
orchestrator = Orchestrator()
