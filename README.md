Prompt Engineering Tool
About the Project

Prompt Engineering Tool is a web-based application developed using Python and Streamlit to demonstrate different prompt engineering techniques. It allows users to enter a task, select a prompting technique, generate a structured prompt, and obtain an AI-generated response using a Hugging Face language model.

The project demonstrates how providing examples within a prompt can guide a Large Language Model (LLM) to produce relevant and structured answers.

Features
Zero-Shot Prompting: Generates prompts without examples.
One-Shot Prompting: Uses one example to guide the model.
Two-Shot Prompting: Uses two examples to demonstrate the expected answer pattern.
Three-Shot Prompting: Uses three examples to guide the model.
Sample Task: Automatically fills the input field with a sample Artificial Intelligence task.
Prompt Generation: Creates prompts based on the selected technique.
AI Response Generation: Generates answers using the Hugging Face Inference API.
Prompt Preview: Displays the generated prompt.
Download Prompt: Allows users to download the generated prompt as a text file.
Interactive Interface: Provides a Streamlit-based interface for selecting techniques and viewing results.
Technologies Used
Python
Streamlit
Hugging Face InferenceClient
Qwen2.5-7B-Instruct
python-dotenv
Project Structure
Prompt-Engineering/
├── app.py
├── prompt_templates.py
├── llm.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md

