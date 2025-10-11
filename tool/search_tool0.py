from tavily import TavilyClient
import os
from crewai.tools import tool


TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

@tool
def search_tool(query: str):
      """Searches for products using Tavily API based on the provided query."""
      return tavily_client.search(query=query)