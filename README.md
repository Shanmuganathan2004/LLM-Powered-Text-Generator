# LLM-Powered-Text-Generator
An  Chatbot Powered by Deepseek-R1 distilled  model LLM which helps to "Generate human Like Text" within seconds

## Overview
This project is a **Large Language Model (LLM) powered text generator** that utilizes the **DeepSeek-R1** model with a **Gradio** interface for text generation. Additionally, it includes a **FastAPI** implementation for API-based text generation.

## Contact
For any questions, feel free to reach out:
- **LinkedIn:** -->([Shanmuganathan](https://www.linkedin.com/in/shanmuganathan120))
- **GitHub:** ---->([Shanmuganathan](https://github.com/Shanmuganathan2004))

## Features
- **Gradio UI** for user-friendly interaction
- **FastAPI backend** for API-based text generation
- **Customizable prompts** for various text generation needs
- **Word limit control** for generated text
- **Docker support** for easy deployment

## Technologies Used
- **Python** (Core scripting language)
- **Gradio** (For UI interaction)
- **FastAPI** (For API-based access)
- **DeepSeek-R1 Model** (LLM backend)
- **Uvicorn** (For running FastAPI)
- **Docker** (For containerization)

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.11+
- pip
- Virtual environment (optional)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/llm-text-generator.git
   cd llm-text-generator
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Gradio Interface
Run the Gradio-based UI:
```sh
python text-generator.py
```
- Open the Gradio UI in your browser (default: `http://localhost:7860`).
- Enter a prompt and generate text using DeepSeek-R1.
- Adjust parameters like temperature and max tokens for fine-tuning responses.

### FastAPI Endpoint
Run the API-based text generator:
```sh
uvicorn app:app --reload
```
- Access the API at `http://127.0.0.1:8000/generate/`.
- Example usage with `curl`:
  ```sh
  curl -X POST "http://127.0.0.1:8000/generate/" -H "Content-Type: application/json" -d '{"prompt": "Write an article about AI", "word_limit": 100}'
  ```

## Code Structure

### `text-generator.py`
```python
import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate_text(prompt, word_limit=100, language="English"):
    full_prompt = f"Write a {language}-language text to generate a response within {word_limit} words:\n\n{prompt}"
    payload = {"model": "deepseek-r1", "prompt": full_prompt, "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No content generated.")

interface = gr.Interface(
    fn=generate_text,
    inputs=[gr.Textbox(lines=3, placeholder="Enter your prompt here"), gr.Slider(50, 500, step=50, label="Word Limit"), gr.Button("Regenerate")],
    outputs="text",
    title="AI-Powered Text Generator",
    description="Enter a prompt, select word limit, and generate AI-written content."
)

if __name__ == "__main__":
    interface.launch()
```

### `app.py`
```python
from fastapi import FastAPI
import requests

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/api/generate"

@app.post("/generate/")
def generate_text(prompt: str, word_limit: int = 100):
    payload = {"model": "deepseek-r1", "prompt": f"Generate {word_limit} words:\n\n{prompt}", "stream": False}
    response = requests.post(OLLAMA_URL, json=payload)
    return response.json().get("response", "No content generated.")
```

## Deployment
For Docker users:
```sh
docker build -t llm-text-generator .
docker run -p 7860:7860 llm-text-generator
```

## Future Improvements
- Adding support for fine-tuning on custom datasets
- Implementing more LLMs (Llama, Falcon, etc.)
- Enhancing UI with additional customization options

## License
This project is licensed under the MIT License.
