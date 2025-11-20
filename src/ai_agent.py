from fastapi import Query
from helpers import parse_ai_response
from langchain.tools import tool
from langchain.agents import create_agent
from tools import query_medgemma, search_therapists_near_me
from langchain_community.tools import DuckDuckGoSearchRun
from prompts import SYSTEM_PROMPT
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

@tool
def ask_elysia_ai(query: str) -> str:
    """Generate a therapeutic, emotionally supportive response using the ElysiaAI model.
    Use this for all general therapy related interactions, emotional questions, and
    supportive conversations. The tool provides warm, empathetic guidance, reflective
    listening, and psychologically informed support."""
    return query_medgemma(prompt=query)

@tool
def web_search(query: str) -> str:
    """Use this tool to search the web for therapists. this will require location of the user.
    and based on the user location find them the best therapists nearby.
    query has to be in the format: "therapists near <location>" """
    return search_therapists_near_me(query=query)


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash", convert_system_message_to_human=True, temperature=0.7
)
tools = [ask_elysia_ai, web_search]
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
