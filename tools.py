from crewai_tools import ScrapeWebsiteTool

def get_scraper_tool(url):
    """Returns a configured web scraping tool instance."""
    return ScrapeWebsiteTool(website_url=url)
