from crewai import Crew, Process ,LLM
from dotenv import load_dotenv
import re
import time
import random
from litellm.exceptions import RateLimitError
import json
from src.Agents.procurement_report_author_agent import procurement_report_author_agent
from src.Agents.search_engine_word import search_engine_word_Agent
from src.Agents.extract_key_word import extract_key_word_Agent
from src.Agents.web_scrabing_agent import web_scraping_agent
from src.Tasks.report_task import report_task
from src.Tasks.search_engine_task import search_engine_task
from src.Tasks.key_word_task import key_word_task
from src.Tasks.web_scrabing_task import Scraping_task 
import os




load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


llm = LLM(model="groq/llama-3.3-70b-versatile", api_key=GROQ_API_KEY, temperature=0, max_tokens=2048)


agent_extract = extract_key_word_Agent(llm)
agent_search  = search_engine_word_Agent(llm)
agent_scrape  = web_scraping_agent(llm)
agent_report  = procurement_report_author_agent(llm)

# Instantiate the keyword task (Crew expects Task objects, not the factory function)
key_word_task_instance = key_word_task(
    product_name="Cofee Machine",
    country_name="Egypt",
    no_keywords=10,
    language="English",
    websites_list=["www.amazon.eg", "www.jumia.com.eg", "www.noon.com/egypt-en"],
    extract_key_word_Agent=agent_extract,
)

# Instantiate the search task as well (don't pass the function object to Crew)
search_engine_task_instance = search_engine_task(
    score_th=0.10,
    search_engine_word_Agent=agent_search,
)

Scraping_task_instance = Scraping_task(
    top_recommendations_no=5,
    scraping_agent=agent_scrape,
)

report_task_instance = report_task(
    report_agent=agent_report,

)


ranky_crew=Crew(
    agents=[agent_extract,
            agent_search,
            agent_scrape,
            agent_report
           ],
    tasks=[key_word_task_instance,
        search_engine_task_instance,
        Scraping_task_instance,
      report_task_instance,
           ],
    process=Process.sequential
)




marwanx = ranky_crew.kickoff(
    inputs={
        "product_name": "Cofee Machine",
        "websites_list": ["www.amazon.eg", "www.jumia.com.eg", "www.noon.com/egypt-en"],
        "country_name": "Egypt",
        "no_keywords": 10,
        "language": "English",
        "score_th": 0.10,
        "top_recommendations_no": 5,
    },
)
