#Import required Libs and packages
import requests
import gradio as gr

# DeepSeek API url to get response from ollma
OLLAMA_URL = "http://localhost:11434/api/generate"

#Setting up the model and set the word generation limit to 100
def generate_text(prompt, word_limit=100, language="English"):
    """
    Uses DeepSeek AI to generate text based on a given prompt.
    """
    full_prompt = f"Write a {language}-language like human text to Generate a response within {word_limit} words:\n\n{prompt}" # set the prompt to write like a human 

    payload = {
        "model": "deepseek-r1",
        "prompt": full_prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        return response.json().get("response", "No content generated.")
    else:
        return f"Error: {response.text}"

# Create Gradio interface
interface = gr.Interface(
    fn=generate_text,
    inputs=[gr.Textbox(lines=3, placeholder="Enter your prompt here"), gr.Slider(50, 500, step=50, label="Word Limit"), gr.Button("Regenrate")],
    outputs="text",
    title="AI-Powered Text Generator",
    theme='NoCrypt/miku', #a custom theme for the web app
    description="Enter a prompt, select word limit, and generate AI-written content."
)

# Launch the web app
if __name__ == "__main__":
    interface.launch()


# # Test AI Generation
# if __name__ == "__main__":
#     prompt = "Write an introduction for an article about the future of AI."
#     print("### AI-Generated Content ###")
#     print(generate_text(prompt))
