import os 

class settings:
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "your_google_api_key_here")
    BACKEND_URL: str = os.getenv("BACKEND_URL", "http://localhost:8000/ask")
    #cohere
    COHERE_API_KEY = os.getenv("COHERE_API_KEY", "your_cohere_api_key_here")
    #pine cone
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY", "your_pinecone_api_key_here")
    PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "your_pinecone_index_name_here")
    #open router
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "your_OPENROUTER_API_KEY_here")
    OPENROUTER_URL = os.getenv("OPENROUTER_URL", "your_OPENROUTER_API_KEY_here")
    OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL", "your_OPENROUTER_API_KEY_here") 
    
    HF_TOKEN =  os.getenv("HF_TOKEN", "HF_TOKEN")