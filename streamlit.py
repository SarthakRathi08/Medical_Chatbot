import os
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_pinecone import PineconeVectorStore
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

from src.helper import download_embeddings
from src.prompt import system_prompt

# Load environment variables
load_dotenv()
PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Load embeddings
embeddings = download_embeddings()

# Connect to Pinecone index
index_name = "medical-chatbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

# Setup retriever
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# Setup LLM
chatModel = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

# Setup prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ]
)

# Build RAG chain
question_answer_chain = create_stuff_documents_chain(chatModel, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

# Streamlit UI
st.set_page_config(page_title="🩺 Medical Chatbot", page_icon="💬")

st.title("🩺 Medical Chatbot using GenAI")
st.write("Ask me any medical-related question. I’ll try my best to assist you!")

# Chat input
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt_text := st.chat_input("Type your medical question..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt_text})
    with st.chat_message("user"):
        st.markdown(prompt_text)

    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = rag_chain.invoke({"input": prompt_text})
            answer = response["answer"]

            st.markdown(answer)

    # Save bot response
    st.session_state.messages.append({"role": "assistant", "content": answer})
