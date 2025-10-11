from crewai import Task
from src.Agents.procurement_report_author_agent import procurement_report_author_agent
import os

def report_task(report_agent):
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../Data'))
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "step_4_procurement_report.html")

    return Task(
    description="\n".join([
        "Your task is to create a **professional HTML procurement report** using the Bootstrap CSS framework for layout and styling.",
        "The report must be easy to read, well-structured, and visually polished for presentation purposes.",
        "",
        "Include the following sections in order:",
        "1. Executive Summary – Provide a concise overview of the procurement process and key insights.",
        "2. Introduction – Explain the purpose, scope, and context of the report.",
        "3. Methodology – Describe how data was gathered and how price comparisons were made.",
        "4. Findings – Present detailed price comparisons from different websites using tables and (optional) charts.",
        "5. Analysis – Interpret the findings, highlight patterns, and identify cost-effective options.",
        "6. Recommendations – Offer strategic purchasing suggestions based on the analysis.",
        "7. Conclusion – Summarize key takeaways and next steps.",
        "8. Appendices – Include supplementary materials or raw data (if provided).",
        "",
        "Guidelines:",
        "- Use Bootstrap components (cards, tables, grids, etc.) for a clean and responsive layout.",
        "- Keep the HTML structure semantic (use <header>, <main>, <section>, <footer>).",
        "- Use a professional color palette (e.g., light background, dark text, subtle accents).",
        "- Add a table of contents or navigation bar for usability (optional).",
        "",
        "Output must be a **complete HTML document**, ready to be viewed in a browser.",
    ]),

    expected_output="A complete and professional HTML page for the procurement report styled with Bootstrap.",
    output_file=output_path,
    agent=report_agent,
)