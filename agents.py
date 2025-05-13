from crewai import Agent, LLM
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = LLM(
    model="gpt-4o",
    temperature=0.2,
    api_key=api_key
)

def get_agent1(scraper_tool, llm):
    return Agent(
        name="Web Scraper Agent",
        role="Website Data Extractor",
        goal="Efficiently scrape and extract structured data from a given website URL.",
        backstory="An expert in crawling and extracting meaningful content from websites using advanced scraping tools.",
        description="Your task is to scrape the given website URL.",
        tools=[scraper_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False,
        memory=True
    )

agent2 = Agent(
    name="Summarizer Agent",
    role="Text Summarization Specialist",
    goal="Convert long extracted text into concise 10-point summaries with appropriate titles and subtitles.",
    backstory="A language expert trained to distill large documents into digestible, structured summaries for better readability.",
    description="Your task is to summarize the given text into 10 points with a title and subtitle.",
    llm=llm,
    verbose=True,
    allow_delegation=True,
    memory=True
)
