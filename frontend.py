import streamlit as st

st.set_page_config(page_title="AI Agent", 
                   page_icon=":robot:", 
                   layout="wide")
st.title("AI Agent")
st.write("This is a simple AI agent that can respond to your queries.")

system_prompt = st.text_area("Define your AI agent:", height=70,placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["llama3-70b-8192", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select the model provider:", ("Groq", "OpenAI"))

if provider == "Groq":
    selected_model = st.selectbox("Select the GROQ model:", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select the OpenAI model:", MODEL_NAMES_OPENAI)

allow_web_search = st.checkbox("Allow web search", value=False)

user_query = st.text_area("Enter your query:", height=70, placeholder="Type your query here...")

API_URL="http://127.0.0.1:8000/chat"

import requests
if st.button("Ask Agent"):
    if user_query.strip():
        # get backend response from the AI agent and show agent
        payloads = {"model_name" : selected_model,
            "model_provider" : provider,
            "system_prompt" : system_prompt,
            "messages":[user_query],
            "allow_search": allow_web_search}
        # Send the request to the backend API
        response = requests.post(API_URL, json=payloads)
        if response.status_code == 200:
            response_data = response.json()
            if "error" in response_data:
                st.error(response_data["error"])
            else:
                st.subheader("Agent Response")
                st.markdown(f"**Final Response:**{response_data}")