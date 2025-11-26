from src.knowledge_base.pinecone_provider import Pinecone
from config import settings
from langchain_pinecone import PineconeVectorStore

def initialize_pinecone():
    pc = Pinecone(api_key=settings.PINECONE_API_KEY)

    # Check if index exists
    existing_indexes = pc.list_indexes().names()

    if settings.PINECONE_INDEX_NAME not in existing_indexes:
        
        pc.create_index(
            name=settings.PINECONE_INDEX_NAME,
            dimension=384,
            metric="cosine",
            spec={"serverless": {"cloud": "aws", "region": "us-east-1"}}
        )   
    # Now connect to index (do NOT pass dimension here)
    index = pc.Index(settings.PINECONE_INDEX_NAME)
    return index

def create_vector_store(chunks, embedding_model):
    """Create a Pinecone vector store from chunks.""" 
    #create the vector store
    vectorstore = PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=embedding_model,
        index_name=settings.PINECONE_INDEX_NAME
    )
    return vectorstore

def get_vector_store(embedding_model):
    """Get the Pinecone vector store."""
    vectorstore = PineconeVectorStore(
        index_name=settings.PINECONE_INDEX_NAME,
        embedding=embedding_model
    )
    return vectorstore