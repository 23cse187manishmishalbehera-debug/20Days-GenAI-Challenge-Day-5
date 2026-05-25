from groq import Groq
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

# Create client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# User input
topic = input("Enter joke topic: ")

# AI response
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Tell me a funny joke about {topic}"
        }
    ],
    model="llama-3.1-8b-instant",
)

# Output
print("\nJoke:\n")
print(chat_completion.choices[0].message.content)