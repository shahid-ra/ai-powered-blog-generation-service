from crewai.tools import BaseTool
from pydantic import Field
from app.search.ddgs_wrapper import DDGSWrapper


class WebSearchTool(BaseTool):
    name: str = "web_search"
    description: str = "Search the web for information on a given topic. Returns a list of relevant search results with titles and descriptions."
    max_results: int = Field(default=10)

    def _run(self, query: str) -> str:
        search_client = DDGSWrapper(max_results=self.max_results)
        results = search_client.search(query)

        if not results:
            return "No search results found for the given query."

        formatted_results = []
        for i, item in enumerate(results, 1):
            title = item.get("title", "No title")
            body = item.get("body", "No description")
            formatted_results.append(f"{i}. {title}\n   {body}")

        return "\n\n".join(formatted_results)
