from crewai import Task
from typing import List
from pydantic import BaseModel, Field
import os

class searchResukt(BaseModel):
  title:str
  url:str=Field(...,title="the page url")
  content:str
  score:float
  search_query:str

class AllSearchResult(BaseModel):
  results:List[searchResukt]

def search_engine_task(
    score_th:float,
    search_engine_word_Agent,
):
    output_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Data'))
    os.makedirs(output_dir, exist_ok=True)
    output_file=os.path.join(output_dir, "step_2_search_results.json")

    return Task(
        description="\n".join([
        "The task is to search for products based on the suggested search queries.",
        "You have to collect results from multiple search queries.",
        "Ignore any susbicious links or not an ecommerce single product website link.",
        "Ignore any search results with confidence score less than ({score_th}) .",
        "The search results will be used to compare prices of products from different websites.",
        ]),
        expected_output="A JSON object containing the search results.",
        output_json=AllSearchResult,
        output_file=output_file,
        agent=search_engine_word_Agent
)