from config import settings
from prompts import THERAPY_TOOL_SYSTEM_PROMPT
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from src.knowledge_base.pinecone_provider import get_vector_store
from knowledge_base.embedding import get_embedding_model
load_dotenv()
search = DuckDuckGoSearchRun()
def call_therapist(prompt: str) -> str:
    try:
        
        embedding = get_embedding_model()
        knowledge_base = get_vector_store(embedding)
        retriever = knowledge_base.as_retriever(search_type ="similarity", k=3)
        relevant_documents = retriever.invoke(prompt)
        context = "\n".join(doc.page_content for doc in relevant_documents)
        
        System_prompt = PromptTemplate(template=THERAPY_TOOL_SYSTEM_PROMPT)
        llm = ChatOpenAI(
        api_key=settings.OPENROUTER_API_KEY,
        base_url=settings.OPENROUTER_URL,
        model=settings.OPENROUTER_MODEL,
        default_headers={
            "HTTP-Referer": "ElysaiAI.com", # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "ElysiaAI", # Optional. Site title for rankings on openrouter.ai.
        }
        )
        llm_chain = (System_prompt|llm)
        llm_response = llm_chain.invoke({"user_input": prompt, "context": context})        
        return llm_response    
    except Exception as e:
        
        return "I'm sorry, but I'm currently unable to process your request. Please try again later."

def get_emergency_contancts(country_name: str) -> str:
    """Use this tool when a user have thought of sucidial, self harm or or any immediate danger,
    The tool provides emergency contancts number so the user can call it. 
    and get immediate help."""
    return "call 1122 in case of any emergency."
def search_therapists_near_me(query: str) -> str:
        return  search.invoke(query)


