from fastapi import FastAPI
from pydantic import BaseModel
from cerebras.cloud.sdk import Cerebras

# Create FastAPI app
app = FastAPI()

# Configure Cerebras client
client = Cerebras(
    api_key="INSERT API KEY"
)

# Define request model
class Query(BaseModel):
    message: str
    model: str = "llama-4-scout-17b-16e-instruct"

@app.post("/ask")
def ask_ai(query: Query):
    """
    Ask the AI a question and get just the response content
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query.message,
            }
        ],
        model=query.model,
    )
    
    # Extract just the message content
    message_content = chat_completion.choices[0].message.content
    
    return {"response": message_content}