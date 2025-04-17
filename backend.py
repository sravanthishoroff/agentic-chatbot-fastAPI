import uvicorn
from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name:str
    model_provider:str
    system_prompt:str
    messages:list[str]
    allow_search:bool 


from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

# list of allowed model names
ALLOWED_MODEL_NAMES = ["llama3-70b-8192", 
                       "mixtral-8x7b-32768", 
                       "llama-3.3-70b-versatile", 
                       "gpt-4o-mini"]

# Initialize the FastAPI app
app = FastAPI(title="LangGraph Agent ", description="API for AI Agent using Langchain and Groq")

# Define the root endpoint
@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    Endpoint for chat with the AI agent.
    """
    # Check if the model name is allowed
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid Model name Kindly, select a valid AI model"}
    
    # create an AI Agent and get response from the model
    response = get_response_from_ai_agent(llm_id=request.model_name,
                                          query=request.messages,
                                          allow_search=request.allow_search,
                                          system_prompt=request.system_prompt,
                                          provider=request.model_provider)
    return response
   
# Run the FastAPI app with Uvicorn server
if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1", port=8000, log_level="info")

   