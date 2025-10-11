from crewai import Agent,LLM
from dotenv import load_dotenv
import os

load_dotenv()
llmm = LLM(
     model="groq/llama-3.3-70b-versatile",
     temperature=0,
     api_key=os.getenv("GROQ_API_KEY")
    )

def extract_key_word_Agent(llm):
    """
    Creates an agent specialized in extracting relevant keywords from user input.
    
    Args:
        llm: The language model to be used by the agent
        
    Returns:
        Agent: A configured CrewAI agent for keyword extraction
    """


    agent = Agent(
        role="Keyword Extraction Specialist",
        goal="\n".join([
            "Extract the most relevant and actionable keywords from user input",
            "Identify main topics, entities, and concepts while filtering out noise.",
            "Provide concise keywords that can be used for search queries or content analysis.",
        ]),
        backstory="\n".join([
            "You are an expert in natural language processing and information retrieval",
            "with years of experience in keyword extraction and search optimization",
            "You have a keen eye for identifying the core concepts in any text and",
            "translating them into effective search terms. You understand context",
            "synonyms, and semantic relationships between words",
        ]),

        llm=llmm,
        verbose=True,
    )
    
    return agent