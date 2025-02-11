from fastapi import FastAPI #import fastapi
import requests #sending requests to ollama

app = FastAPI() 
OLLAMA_URL = "http://localhost:11434/api/generate" #api key to use the llm

@app.post("/generate/") #sending post requests
def generate_text(prompt: str, word_limit: int = 100): #Load the model and set word limit for text generation
    payload = {"model": "deepseek-r1:7b", "prompt": f"Generate {word_limit} words:\n\n{prompt}", "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No content generated.")

# Run with: uvicorn app:app --reload # this cmd helps to run the app.py
