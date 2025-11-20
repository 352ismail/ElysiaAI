from fastapi import FastAPI
from pydantic import BaseModel
from ai_agent import get_ai_response

app = FastAPI(
    title="Elysia AI Backend",
    version="1.0.0",
    description="Elysia AI Backend API",
    debug=True,
)

class Query(BaseModel):
    role: str
    content: str

@app.post("/ask")
async def ask(messages: list[Query]):
    response = get_ai_response(previous_messages=messages)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
