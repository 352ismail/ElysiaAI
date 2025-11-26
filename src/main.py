from fastapi import FastAPI
from pydantic import BaseModel
from ai_agent import get_ai_response
from dotenv import load_dotenv
from src.knowledge_base.pinecone_provider import initialize_pinecone,create_vector_store
from knowledge_base.embedding import get_embedding_model
from knowledge_base.pdf_loader import load_pdfs
import glob
import threading
load_dotenv()

app = FastAPI(
    title="Elysia AI Backend",
    version="1.0.0",
    description="Elysia AI Backend API",
    debug=True,
)

class Query(BaseModel):
    role: str
    content: str
    
    
def load_context()-> int:
    files = glob.glob("context/*.pdf")
    pdfs= load_pdfs(files)
    initialize_pinecone()  
    for pdf in pdfs:  
        create_vector_store(pdf,get_embedding_model()) 
    return 1
         
@app.post("/embeddings")
async def startup_event():
    thread = threading.Thread(target=load_context)
    thread.daemon = True
    thread.start()
    return {"status": "Success",
            "message": "loading context has been started"}
    
@app.post("/ask")
async def ask(messages: list[Query]):
    response = get_ai_response(previous_messages=messages)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
