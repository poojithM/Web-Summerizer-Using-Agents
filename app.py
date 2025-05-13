from agents import get_agent1, agent2, llm
from task import scraper_task, summerizer_task
from tools import get_scraper_tool
from crewai import Crew, Process
import streamlit as st

st.title("Website Summarizer")

st.markdown("This app summarizes a given website URL into 10 bullet points with titles and subtitles.")

input_url = st.text_input("Enter URL", "https://www.something.com")

if st.button("Submit") and input_url:
    with st.spinner("Scraping and summarizing the website..."):

        scraper_tool = get_scraper_tool(input_url)
        agent1 = get_agent1(scraper_tool, llm)

        task1 = scraper_task(agent1)
        task2 = summerizer_task(agent2)

        crew = Crew(
            agents=[agent1, agent2],
            tasks=[task1, task2],
            process=Process.sequential,
            full_output=True,
            verbose=True
        )

        result = crew.kickoff()

        st.subheader("Scraped Data")
        st.write(result.raw)
