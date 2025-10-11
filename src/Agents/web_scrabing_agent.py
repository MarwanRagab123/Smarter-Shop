from crewai import Agent
from tool.web_scarping_tool1 import web_scraping_tool

def web_scraping_agent(llm):
    return Agent(
        role="Web Scrabing Agent",
        goal="to extract details from web page",
        backstory="The agent is designed to help in looking for required values from any website url. These details will be used to decide which best product to buy.",
        llm=llm,
    tools=[web_scraping_tool],
        verbose=True,
)