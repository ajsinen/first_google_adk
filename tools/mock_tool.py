import requests
from dotenv import load_dotenv
import os

load_dotenv()


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
