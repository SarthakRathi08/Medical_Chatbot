# 🩺 Medical Chatbot Using GenAI

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-3.1.1-lightgrey.svg)](https://flask.palletsprojects.com/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red.svg)](https://medicalchatbot-aryandhanuka10.streamlit.app/)  
[![LangChain](https://img.shields.io/badge/LangChain-0.3.26-orange.svg)](https://www.langchain.com/)  
[![License](https://img.shields.io/badge/License-Apache_2.0-green.svg)](./LICENSE)  

---

## 🚀 Overview

The **Medical Chatbot** is an AI-powered assistant built using **Generative AI, LangChain, Pinecone, and LLMs**.  
It retrieves medical knowledge from indexed PDFs, processes queries, and provides concise, medically relevant answers.

You can interact with the chatbot using:

- 🖥 **Flask Web Interface** (local run)  
- 🌐 **Streamlit Deployed App** → [Medical Chatbot on Streamlit]( https://medicalchatbot-aryandhanuka10.streamlit.app/)  

---

## ✨ Features

- 📄 **PDF Knowledge Base** → Medical documents are embedded and indexed using Pinecone.  
- 🤖 **LLM-Powered** → Uses `llama-3.3-70b` (via `ChatGroq`) for answering queries.  
- 💬 **Interactive Chat UI** → Flask (Bootstrap UI) and Streamlit (modern chat UI).  
- 🔐 **Environment Variable Support** → `.env` for API keys (OpenAI, Pinecone, Groq).  

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SarthakRathi08/Medical_Chatbot_Using_GenAI
cd Medical_Chatbot_Using_GenAI
```

### 2️⃣ Create a Conda Environment
```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables
Create a `.env` file in the root directory:
```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxx"
GROQ_API_KEY = "xxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxx"
```

### 5️⃣ Store Embeddings in Pinecone
```bash
python store_index.py
```

### 6️⃣ Run Locally

👉 **Flask App**
```bash
python app.py
```
App will run at: `http://localhost:8080`

👉 **Streamlit App**
```bash
streamlit run streamlit.py
```
App will run at: `http://localhost:8501`

---

## 🌐 Deployed Link

- 🚀 **Streamlit Deployment** → [https://medicalchatbot-sarthak.streamlit.app/]( https://medicalchatbot-aryandhanuka10.streamlit.app/)  

---

## 🛠 Tech Stack

- **Backend**: Python, Flask, Streamlit  
- **AI/LLM**: LangChain, ChatGroq, HuggingFace Embeddings  
- **Database**: Pinecone (Vector Database)  
- **Deployment**: Streamlit Cloud  

---

## 📂 Project Structure

```
├── app.py                # Flask Web App
├── streamlit.py          # Streamlit App
├── store_index.py        # Pinecone Embedding Store
├── src/
│   ├── helper.py         # Helper functions
│   ├── prompt.py         # System + user prompts
├── templates/chat.html   # Flask frontend (Bootstrap UI)
├── static/style.css      # Chat styling
├── requirements.txt      # Dependencies
├── Dockerfile            # Docker configuration
├── .github/workflows/    # CI/CD pipeline
└── README.md             # Project documentation
```

---

## 📜 License

This project is licensed under the **Apache 2.0 License**.  
See the [LICENSE](./LICENSE) file for details.

---

## 👨‍💻 Author

**Sarthak Rathi**  
🌐 [GitHub Repository](https://github.com/SarthakRathi08/Medical_Chatbot_Using_GenAI)  
