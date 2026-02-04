from crewai import Agent, Task
from app.orchestration.tools.search_tool import WebSearchTool


class ResearchAgent:
    def __init__(self, topic: str, max_results: int = 10):
        self.topic = topic
        self.search_tool = WebSearchTool(max_results=max_results)

    def create_agent(self) -> Agent:
        return Agent(
            role="Research Specialist",
            goal=f"Conduct thorough research on '{self.topic}' to gather comprehensive, accurate, and relevant information",
            backstory="""You are an expert research analyst with years of experience in
            gathering and synthesizing information from various sources. You excel at
            finding credible sources, identifying key facts, and organizing information
            in a structured manner. Your research forms the foundation for high-quality content.""",
            tools=[self.search_tool],
            verbose=True,
            allow_delegation=False,
        )

    def create_task(self, agent: Agent) -> Task:
        return Task(
            description=f"""Research the topic: '{self.topic}'

            Your task is to:
            1. Search for relevant information about the topic
            2. Identify key facts, statistics, and insights
            3. Find different perspectives and viewpoints
            4. Gather examples and case studies if applicable
            5. Note any recent developments or trends

            Compile your findings into a comprehensive research summary that will
            serve as the foundation for a blog post.""",
            expected_output="""A detailed research summary containing:
            - Key facts and statistics about the topic
            - Main themes and subtopics identified
            - Notable quotes or insights from sources
            - Different perspectives on the topic
            - Relevant examples or case studies
            - Any recent trends or developments""",
            agent=agent,
        )
