from crewai import Agent
from tool.search_tool0 import search_tool


def search_engine_word_Agent(llm):
      return Agent(
        role="Search Engine Agent",
        goal="To search for products based on the suggested search query",
        backstory="The agent is designed to help in looking for products by searching for products based on the suggested search queries.",
        llm=llm,
        verbose=True,
    tools=[search_tool]
    )
