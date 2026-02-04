from app.search.ddgs_wrapper import DDGSWrapper

class ResearchAgent:
    def __init__(self, max_results: int = 10):
        self.search_client = DDGSWrapper(max_results=max_results)

    def research(self, topic: str) -> list[dict]:
        """Research a topic and return search results."""
        return self.search_client.search(topic)
