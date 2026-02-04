from crewai import Crew, Process
from app.agents.research_agent import ResearchAgent
from app.agents.writer_agent import WriterAgent
from app.models.blog_generation_type import BlogGenerationType


class BlogGenerationCrew:
    def __init__(self, topic: str, blog_type: BlogGenerationType):
        self.topic = topic
        self.blog_type = blog_type
        self.research_agent = ResearchAgent(topic=topic)
        self.writer_agent = WriterAgent(topic=topic, blog_type=blog_type)

    def run(self) -> str:
        research_crew_agent = self.research_agent.create_agent()
        writer_crew_agent = self.writer_agent.create_agent()

        research_task = self.research_agent.create_task(research_crew_agent)
        writing_task = self.writer_agent.create_task(writer_crew_agent, research_task)

        crew = Crew(
            agents=[research_crew_agent, writer_crew_agent],
            tasks=[research_task, writing_task],
            process=Process.sequential,
            verbose=True,
        )

        result = crew.kickoff()
        return str(result)
