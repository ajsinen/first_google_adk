from typing import Optional
import requests
from google.adk.agents.llm_agent import Agent
import os
from dotenv import load_dotenv

load_dotenv()

# Mock tool implementation
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    return {"status": "success", "city": city, "time": "10:30 AM"}


def get_cat_facts(number: Optional[int]) -> dict:
    """Returns a random facts about cats everytime. Use the parameter {number} if user ask for more than 1 fact"""
    cat_url = os.getenv("CAT_API_BASE_URL")
    if number:
        cat_url += f"?count={number}"
    print("cat url ", cat_url)
    response = requests.get(cat_url)
    message = response.json()

    return {"fact": message.get(["data"][0])}


root_agent = Agent(
    model='gemini-flash-latest',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that tells the current time in cities. Use the 'get_current_time' tool for this purpose.",
    tools=[get_current_time, get_cat_facts],
)
