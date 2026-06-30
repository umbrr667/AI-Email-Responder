from groq import Groq
from dotenv import load_dotenv
import os
COMPANY_NAME = "GUL E NAZ"
# Load API key from .env
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Create Groq client
client = Groq(api_key=api_key)

print("=" * 50)
print("   GUL E NAZ - AI EMAIL RESPONDER")
print("=" * 50)

print("\nPaste your email below.")
print("When you're done, type END on a new line and press Enter.\n")

lines = []

while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

email = "\n".join(lines)
print("\n========== EMAIL RECEIVED ==========")
print(email)
print("====================================\n")

completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": f"""
You are a professional AI Email Assistant working for the company {COMPANY_NAME}.

You will receive ONE customer email.

Your tasks are:
1. Read the customer's email carefully.
2. Classify it as exactly one of these:
   - Inquiry
   - Complaint
   - Support
3. Write a professional reply on behalf of {COMPANY_NAME}.
4. End every reply with:

Best Regards,
Customer Support Team
{COMPANY_NAME}

IMPORTANT:
- Do NOT ask the user to provide the email.
- The email has already been provided.
- Respond directly to the customer's email.

Return ONLY this format:

Category:
Reply:
"""
        },
        {
            "role": "user",
            "content": email
        }
    ]
)

print("\n" + "=" * 50)
print("AI RESPONSE")
print("=" * 50)

print(completion.choices[0].message.content)