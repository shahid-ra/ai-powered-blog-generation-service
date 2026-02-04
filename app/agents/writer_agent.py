from app.models.blog_generation_type import BlogGenerationType


class WriterAgent:
    def __init__(self):
        self.style_prompts = {
            BlogGenerationType.PROFESSIONAL: "Write a professional, authoritative blog post suitable for industry experts.",
            BlogGenerationType.EDUCATIONAL: "Write an educational blog post that teaches concepts clearly with examples.",
            BlogGenerationType.INFORMATIONAL: "Write an informative blog post that presents facts and insights objectively.",
            BlogGenerationType.STORYTELLING: "Write an engaging narrative-style blog post that tells a story.",
        }

    def build_prompt(self, topic: str, blog_type: BlogGenerationType, research_data: list[dict]) -> str:
        """Build a prompt for blog generation based on research data."""
        style = self.style_prompts.get(blog_type, self.style_prompts[BlogGenerationType.INFORMATIONAL])
        research_summary = self._format_research(research_data)

        prompt = f"""Topic: {topic}

				Style: {style}

				Research Data:
				{research_summary}

				Write a well-structured blog post based on the above topic and research data.
				Include an engaging introduction, main content, and conclusion."""

        return prompt

    def _format_research(self, research_data: list[dict]) -> str:
        """Format research results into a readable summary."""
        if not research_data:
            return "No research data available."

        formatted = []
        for item in research_data:
            title = item.get("title", "")
            body = item.get("body", "")
            formatted.append(f"- {title}: {body}")

        return "\n".join(formatted)
