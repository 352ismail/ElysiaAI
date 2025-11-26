from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from config import settings

def get_embedding_model():
    embedding_model = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')
    return embedding_model

def create_chunks(documents, chunk_size=700, chunk_overlap=50):   
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
    )
    chunks = text_splitter.split_documents(documents)
    return chunks