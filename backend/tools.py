import ollama
from prompts import THERAPY_TOOL_SYSTEM_PROMPT
from langchain_community.tools import DuckDuckGoSearchRun
search = DuckDuckGoSearchRun()
def query_medgemma(prompt: str) -> str:
    try:
        response = ollama.chat(
            model="alibayram/medgemma:4b",
            messages=[
                {"role": "system", "content": THERAPY_TOOL_SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            options={
                "temperature": 0.7,
                "num_predict": 350,
                "top_p": 0.9}
        )
        return response["message"]["content"].strip()
    except Exception as e:
        return "I'm sorry, but I'm currently unable to process your request. Please try again later."
    
def search_therapists_near_me(query: str) -> str:
        return  search.invoke(query)


