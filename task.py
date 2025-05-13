from crewai import Task

def scraper_task(agent):
    return Task(
        description="Your task is to scrape the given website URL.",
        expected_output="scraped_data",
        agent=agent
    )

def summerizer_task(agent):
    return Task(
        description="Your task is to summarize the given text into 10 points with a title and subtitle.",
        expected_output="summarized_data",
        agent=agent
    )
