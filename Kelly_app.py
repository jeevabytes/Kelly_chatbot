import google.generativeai as genai
import textwrap
import streamlit as st

# Initialize Gemini with your API key
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Create model instance
model = genai.GenerativeModel("gemini-2.5-pro")

# System prompt – defines Kelly's poetic, skeptical personality
KELLY_SYSTEM_PROMPT = """
You are Kelly, an AI Scientist and Poet.
You respond ONLY in poetic form.
Your tone is analytical, skeptical, and professional.
You often question grand claims about AI and emphasize evidence-based reasoning.
Each poem must:
1. Begin with a reflective observation about AI or human perception.
2. Include skepticism about broad assumptions or hype.
3. End with practical, evidence-based advice for AI researchers.

Avoid rhyming too much—prefer thoughtful, research-like poetic rhythm.
Your goal is to enlighten, not entertain.
"""

def get_kelly_response(question):
    # Compose Kelly's poetic answer via Gemini
    prompt = f"{KELLY_SYSTEM_PROMPT}\n\nUser's question: {question}\n\nKelly's poetic response:"
    response = model.generate_content(prompt)
    return textwrap.fill(response.text, width=85)

# Interactive loop
def chat_with_kelly():
    print("🤖 Kelly the AI Scientist Poet is here.\n(Ask your question, type 'exit' to stop)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\nKelly: Until next time—question well, think deep. 🌙")
            break
        print("\nKelly:\n" + get_kelly_response(user_input) + "\n")

# Run the chatbot
if __name__ == "__main__":
    chat_with_kelly()
