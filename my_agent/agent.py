from google.adk.agents.llm_agent import Agent
from dotenv import load_dotenv
from tools import mock_tool
from google.adk.tools import google_search

load_dotenv()


root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="You are a helpful assistant that gives what the user wants. Use the available tools for the "
                "user inquiry if needed, use google search tool if you dont know the answer.",
    tools=[mock_tool.get_current_time, mock_tool.get_cat_facts, google_search],
)


search_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description="Tells the current time in a specified city.",
    instruction="""You are a helpful AI assistant.

    Rules:
    - Answer user questions clearly and accurately.
    - Use tools whenever real-time or external information is needed.
    - Use Google Search if the answer is unknown.
    - Never invent tool results.""",
    tools=[google_search],
)