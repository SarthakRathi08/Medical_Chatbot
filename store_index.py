from dotenv import load_dotenv
import os
from pinecone import Pinecone , ServerlessSpec
from src.helper import load_pdf_files, filter_to_minimal_docs, text_split, download_embeddings   
from langchain_pinecone import PineconeVectorStore


load_dotenv()

# Database
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")    
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
os.environ["GROQ_API_KEY"] = GROQ_API_KEY
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

extracted_data = load_pdf_files("data/")
filter_data = filter_to_minimal_docs(extracted_data)
texts_chunks = text_split(filter_data)
embeddings = download_embeddings()

pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)

# Index

from pinecone import ServerlessSpec

index_name = "medical-chatbot"
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384, # dimesion of the embedding model
        metric="cosine", # cosine similarity
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )
index = pc.Index(index_name)

docsSearch = PineconeVectorStore.from_documents(
    documents=texts_chunks,
    embedding=embeddings,
    index_name=index_name,

)
