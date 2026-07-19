import os
from dotenv import load_dotenv
from groq import Groq
print("===== USING GROQ AI_HELPER =====")
print("Groq package imported successfully")

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_minutes(meeting_notes):

    prompt = f"""
You are a professional meeting assistant.

Convert the following meeting notes into:

1. Meeting Summary
2. Action Items
3. Professional Follow-up Email

Meeting Notes:
{meeting_notes}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content