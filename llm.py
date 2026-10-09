
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

token = os.getenv("HF_TOKEN")

client = InferenceClient(
    token=token,
    timeout=30
) if token else None


def get_response(prompt):
    if not client:
        raise ValueError(
            "HF_TOKEN is missing. Check your .env file."
        )

    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=120,
        temperature=0.5
    )

    answer = response.choices[0].message.content

    if not answer:
        raise ValueError("The model returned an empty response.")

    return answer