# 🤖 AI Agentic Chatbot with LangGraph + FastAPI + Streamlit

This repository contains an **AI Agentic Chatbot** application powered by **LangChain**, **LangGraph**, and **FastAPI**, with a frontend built in **Streamlit**. It supports both **OpenAI** and **Groq** models (e.g., GPT-4o-mini, Mixtral, LLaMA 3) and allows optional web search via Tavily.

---

## 🔧 Features

- 🌐 Frontend UI built using Streamlit
- ⚙️ Backend served using FastAPI with `/chat` endpoint
- 🧠 Uses LangGraph + LangChain agent for structured multi-step reasoning
- 🔍 Supports web search via Tavily (optional)
- 🤖 Pluggable support for OpenAI & Groq model providers
- ✅ Compatible with `gpt-4o-mini`, `llama3-70b`, `mixtral-8x7b`, and more

---

## 📁 Project Structure

├── .env # API keys (OpenAI, Groq, Tavily) 
├── ai_agent.py # Core agent logic using LangGraph 
├── backend.py # FastAPI backend server 
├── frontend.py # Streamlit frontend UI 
├── requirements.txt # List of Python dependencies 
└── README.md # Project documentation


---

## 🚀 How to Run the Project

### 1. 📦 Clone the Repository

```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name

### 2. 🧪 Create a Virtual Environment

```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\\Scripts\\activate

3. 📦 Install Requirements

```bash
    pip install -r requirements.txt

4. 🔐 Setup Environment Variables
    Create a .env file with your API keys:

    OPENAI_API_KEY=your-openai-api-key
    GROQ_API_KEY=your-groq-api-key
    TAVILY_API_KEY=your-tavily-api-key

5. 🖥️ Start Backend (FastAPI)

```bash
    python backend.py

    Runs on: http://127.0.0.1:8000

    Test in browser: http://127.0.0.1:8000/docs

6. 💬 Start Frontend (Streamlit)

    In another terminal/tab:
    ```bash
        streamlit run frontend.py

    Access at: http://localhost:8501

🛠️ Supported Models

    Provider	Model
    OpenAI	gpt-4o-mini
    Groq	mixtral-8x7b-32768
    Groq	llama3-70b-8192

🧠 Powered By
    LangChain

    LangGraph

    Streamlit

    FastAPI

    Groq

    OpenAI

    Tavily
### 🙌 Contributing
    Feel free to open issues or pull requests if you'd like to contribute, improve, or extend the agentic capabilities!



