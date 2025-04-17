import os
import httpx
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

load_dotenv()
# Load environment variables from .env file
api_key = os.getenv("OPENAI_API_KEY")
groq_api_key = os.getenv("GROQ_API_KEY")
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Check if the API keys are loaded correctly
# print(api_key)

# Initialize the Openai LLM with the API key and HTTP client with SSL verification disabled
openai_llm = ChatOpenAI(
    model='gpt-4o-mini', 
    openai_api_key=api_key,
    http_client=httpx.Client(verify=False))

# Initialize the Groq LLM with the API key and HTTP client
groq_llm = ChatGroq(
    model='llama-3.3-70b-versatile',
    api_key=groq_api_key,
    http_client=httpx.Client(verify=False))


from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

# Define the system prompt for the agent
system_prompt = "Act as an AI assistant who is smart and friendly that can search the web for information. " \
               "You can use the Travily search tool to find relevant information. " \
               "When you find the information, summarize it and provide a link to the source."


# 
def get_response_from_ai_agent(llm_id,query,allow_search,system_prompt,provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)

    # Initialize the Tavily search tool with the API key
    tools = [TavilySearchResults(max_results=3)] if allow_search else []

    # Create the agent with the Groq LLM and the Tavily search tool
    agent = create_react_agent(
    model=llm,
    tools=tools,
    state_modifier = system_prompt)

    # Invoke the agent with a query
    state = {"messages": query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
    
    return ai_messages[-1] 
