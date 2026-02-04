from typing import List
from crewai.tools import BaseTool
from pydantic import Field
from app.search.ddgs_wrapper import DDGSWrapper

class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = "Search the web for information on a given topic. Returns a list of relevant search results with titles, descriptions, and source URLs."
    max_results: int = Field(default=10)
    sources: List[dict] = Field(default_factory=list)

    def _run(self, query: str) -> str:
        search_client = DDGSWrapper(max_results=self.max_results)
        results = search_client.search(query)

        if not results:
            return "No search results found for the given query."

        formatted_results = []
        for i, item in enumerate(results, 1):
            title = item.get("title", "No title")
            body = item.get("body", "No description")
            url = item.get("href", "")

            # Track source for later retrieval
            if url and not any(s["url"] == url for s in self.sources):
                self.sources.append({"title": title, "url": url})

            formatted_results.append(f"{i}. {title}\n   {body}\n   Source: {url}")

        return "\n\n".join(formatted_results)

    def get_sources(self) -> List[dict]:
        return self.sources

    def clear_sources(self):
        self.sources = []
