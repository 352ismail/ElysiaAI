from langchain_community.document_loaders import PyPDFLoader

def load_pdfs(pdf_files):
    pdf_list = []
    
    for pdf in pdf_files:
        
        loader = PyPDFLoader(pdf)
        docs = loader.load()
        pdf_list.append(docs)
    return pdf_list

