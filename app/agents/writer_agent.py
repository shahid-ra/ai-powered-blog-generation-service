from crewai import Agent, Task
from app.models.blog_generation_type import BlogGenerationType


class WriterAgent:
    STYLE_DESCRIPTIONS = {
        BlogGenerationType.PROFESSIONAL: "professional, authoritative, suitable for industry experts with technical depth",
        BlogGenerationType.EDUCATIONAL: "educational, teaching concepts clearly with examples and step-by-step explanations",
        BlogGenerationType.INFORMATIONAL: "informative, presenting facts and insights objectively with balanced perspectives",
        BlogGenerationType.STORYTELLING: "engaging narrative-style that tells a story and connects with readers emotionally",
    }

    def __init__(self, topic: str, blog_type: BlogGenerationType):
        self.topic = topic
        self.blog_type = blog_type
        self.style = self.STYLE_DESCRIPTIONS.get(
            blog_type,
            self.STYLE_DESCRIPTIONS[BlogGenerationType.INFORMATIONAL]
        )

    def create_agent(self) -> Agent:
        return Agent(
            role="Content Writer",
            goal=f"Write a compelling {self.style} blog post about '{self.topic}'",
            backstory=f"""You are a skilled content writer specializing in creating
            {self.style} content. You have a talent for transforming research data into
            engaging, well-structured articles that resonate with readers. You understand
            SEO best practices and how to craft content that is both informative and
            captivating. Your writing style adapts to the target audience while maintaining
            clarity and professionalism.""",
            verbose=True,
            allow_delegation=False,
        )

    def create_task(self, agent: Agent, research_task: Task) -> Task:
        return Task(
            description=f"""Write a {self.style} blog post about '{self.topic}' using the research provided.

            Your task is to:
            1. Create an attention-grabbing headline
            2. Write an engaging introduction that hooks the reader
            3. Develop the main content with clear sections and subheadings
            4. Include relevant facts, examples, and insights from the research
            5. Write a compelling conclusion with a call-to-action
            6. Ensure the tone matches the {self.blog_type.value} style throughout

            The blog post should be well-structured, informative, and engaging.""",
            expected_output="""A complete blog post with:
            - An attention-grabbing headline
            - An engaging introduction (2-3 paragraphs)
            - Main content with 3-5 sections, each with subheadings
            - Relevant facts, statistics, and examples integrated naturally
            - A compelling conclusion with key takeaways
            - Appropriate formatting with headers and paragraphs
            - Word count between 800-1500 words""",
            agent=agent,
            context=[research_task],
        )
