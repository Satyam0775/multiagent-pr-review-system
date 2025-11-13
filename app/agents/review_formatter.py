class ReviewFormatter:
    def merge(self, summary: str, security: list, logic: list, performance: list, style: list):
        comments = security + logic + performance + style
        return {
            "summary": summary,
            "total_comments": len(comments),
            "comments": comments
        }
