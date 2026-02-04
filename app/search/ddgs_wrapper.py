from duckduckgo_search import DDGS

class DDGSWrapper:
    def __init__(self, max_results: int = 10):
        self.max_results = max_results
        self.ddgs = DDGS()

    def search(self, topic: str) -> list[dict]:
        """Search the internet for information about a topic."""
        results = self.ddgs.text(topic, max_results=self.max_results)
        return results
