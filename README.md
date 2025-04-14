# Cerebras FastAPI Chatbot 

This project is a lightweight FastAPI-based backend that connects to the Cerebras API to interact with powerful large language models (LLMs) like `llama-4-scout-17b-16e-instruct`. The API accepts user input and returns AI-generated responses. It also includes a simple script to send prompts directly and save results to a file.

--- 

## Features 

- 🔌 FastAPI endpoint for querying Cerebras LLMs 
- 🧠 Supports different model selection (default: `llama-4-scout-17b-16e-instruct`) 
- 💬 Returns only the relevant response message 
- 💾 Script to save AI responses to a `.txt` file 

--- 

## Requirements 

- Python 3.8+ 
- A valid Cerebras API Key 
- Cerebras Cloud SDK installed (`cerebras-cloud-sdk`) 

--- 

## Installation 

```bash
git clone https://github.com/your-username/your-repo.git 
cd your-repo 
pip install -r requirements.txt
```

--- 

## Configuration 
Insert your Cerebras API key in the relevant lines: 
```python 
client = Cerebras(api_key="INSERT API KEY") 
``` 
You can (should) also store this as an environment variable instead.

--- 

## Running the Server 
Start the FastAPI server locally with Uvicorn: 
```bash 
uvicorn main:app --reload 
``` 
Then, send a POST request to: 
``` POST http://localhost:8000/ask ``` 
Example JSON payload: 
```json 
{ 
  "message": "Tell me a joke", 
  "model": "llama-4-scout-17b-16e-instruct" 
} 
``` 

--- 

## CLI Script (Optional) 

You can run the included script to generate a one-off response and save it to a file: 
```bash 
python generate_message.py 
``` 
This sends a prompt to the model and stores the plain message in `message_only.txt`. 

--- 

## Example Output 

``` 
> Prompt: Give me back a tetris game in python code 
✅ Response saved to message_only.txt 
``` 

--- 

## License 
MIT License. 

See `LICENSE` file for details. 

--- 

## Credits 
Built using: 
- [FastAPI](https://fastapi.tiangolo.com/) 
- [Cerebras Cloud SDK](https://docs.cerebras.net/) 

--- 
## Author 
Eric Ly (@lyeric2022) 🚀