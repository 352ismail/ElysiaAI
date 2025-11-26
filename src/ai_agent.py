from fastapi import Query
from helpers import parse_ai_response
from langchain.tools import tool
from langchain.agents import create_agent
from tools import call_therapist, search_therapists_near_me,get_emergency_contancts
from langchain_community.tools import DuckDuckGoSearchRun
from prompts import SYSTEM_PROMPT
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

@tool
def get_emergency_numbers(country_name: str) -> str:
    """Use this tool when a user have thought of sucidial, self harm or or any immediate danger,
    The tool provides emergency contancts number so the user can call it. 
    and get immediate help."""
    return get_emergency_contancts(country_name=country_name)

@tool
def ask_therapist(query: str) -> str:
    """Generate a therapeutic, emotionally supportive response.
    Use this for all general therapy related interactions, emotional questions, and
    supportive conversations. The tool provides warm, empathetic guidance, reflective
    listening, and psychologically informed support."""
    return call_therapist(prompt=query)

@tool
def web_search(query: str) -> str:
    """Use this tool to search the web for therapists. this will require location of the user.
    and based on the user location you will need to proide a list of therapist website links, 
    names, addresses and contact information."""
    return search_therapists_near_me(query=query)
import os
google_api_key = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", convert_system_message_to_human=True, temperature=0.9
)
tools = [ask_therapist, web_search, get_emergency_numbers]
graph = create_agent(model=llm, tools=tools)


def get_ai_response(previous_messages: list = None) -> str:
    messages = []
    inputs = {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
        ]
    }
    if previous_messages:
        for message in previous_messages:
            inputs["messages"].append(message.dict())
   
    stream = graph.stream(inputs, stream_mode="updates")
    for data in stream:
        messages.append(parse_ai_response(data))

    return ' '.join(messages)
