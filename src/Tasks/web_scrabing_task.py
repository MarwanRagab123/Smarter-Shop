from crewai import Task
import os
from pydantic import BaseModel, Field
from typing import List
from tool import web_scarping_tool1
from src.Agents.web_scrabing_agent import web_scraping_agent


def Scraping_task(top_recommendations_no: int, scraping_agent) -> Task:
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Data'))
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "step_3_scraping_results.json")

    class ScrapingResults(BaseModel):
        products: List[web_scarping_tool1.SingleExtractedProduct]

    return Task(
        description="\n".join([
        f"The task is to extract product details from any ecommerce store page url.",
        "The task has to collect results from multiple pages urls.",
        "Collect the best {top_recommendations_no} products from the search results.",
        ]),
        expected_output="A JSON object containing product details",
        output_json=ScrapingResults, 
        output_file=output_path,
        agent=scraping_agent
    )