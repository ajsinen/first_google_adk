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


def get_cat_facts(number: int = 1) -> dict:
    """Returns a random facts about cats everytime.
    Args:
        number: Number of cat facts to return. Defaults to 1
    """
    cat_url = os.getenv("CAT_API_BASE_URL")
    print("cat url without param", cat_url)
    if number > 1:
        cat_url += f"?count={str(number)}"
    print("cat url ", cat_url)
    response = requests.get(cat_url)
    message = response.json()

    return dict(message)


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that gives what the user wants. Use the tool for the user inquiry "
                "if possible",
    tools=[get_current_time, get_cat_facts],
)
