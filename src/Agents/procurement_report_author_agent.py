from crewai import Agent

def procurement_report_author_agent(llm):

    return Agent(
    role="Procurement Report Author",
    goal="Generate a polished and well-structured HTML procurement report using Bootstrap.",
    backstory=(
        "This agent specializes in creating professional procurement reports. "
        "After analyzing a list of products and their prices from various e-commerce platforms, "
        "it compiles the findings into a clean, visually appealing HTML report that can be shared with stakeholders."
    ),
    llm=llm,
    verbose=True,
)