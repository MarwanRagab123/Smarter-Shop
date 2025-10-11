from crewai import Task
from typing import List
from pydantic import BaseModel, Field
import os

class KeyWordTaskOutput(BaseModel):
    keywords: List[str] = Field(..., description="A list of relevant and highly specific search queries.", min_items=1)

def key_word_task(
    product_name: str,
    country_name: str,
    no_keywords: int,
    language: str,
    websites_list: List[str],
    extract_key_word_Agent,
):
    output_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Data'))
    os.makedirs(output_dir, exist_ok=True)
    output_file=os.path.join(output_dir, 'key_word_task_output.json')

    return Task(
         description="\n".join([
            f"Rankyx aims to find **{product_name}** with a focus on value-for-money options.",
            f"Search should target the following websites: {websites_list}.",
            f"Locate **all relevant product listings** available online to enable comprehensive price and feature comparison.",
            f"Only include products that are sold in **{country_name}**.",
            f"Generate up to **{no_keywords}** highly specific search queries.",
            f"Queries must be composed in **{language}**.",
            "Include specific **brands, product types, or technologies**  avoid vague or generic terms.",
            "Make sure queries lead to **e-commerce product pages** directly, excluding blogs, news articles, or category hubs."
        ]),
        expected_output="A JSON object containing a list of relevant and highly specific search queries.",
        output_json=KeyWordTaskOutput,
        output_file=output_file,
        agent=extract_key_word_Agent
    )