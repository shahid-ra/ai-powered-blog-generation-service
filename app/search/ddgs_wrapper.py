from ddgs import DDGS


class DDGSWrapper:
    def __init__(self, max_results: int = 10):
        self.max_results = max_results

    def search(self, topic: str) -> list[dict]:
        """Search the internet for information about a topic."""
        ddgs = DDGS()
        results = ddgs.text(topic, max_results=self.max_results)
        return list(results) if results else []
