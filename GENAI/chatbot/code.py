from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
import logging

# =========================
# Load Environment Variables
# =========================
load_dotenv()

os.environ['GEMINI_API_KEY'] = os.getenv('API_KEY')



llm = init_chat_model('google_genai:gemini-2.5-flash-lite')



# =========================
# System Prompt
# =========================
SYSTEM_PROMPT = """
You are an AI Blog Assistant Chatbot.

Your tasks:
- Generate blog content
- Create SEO-friendly titles
- Summarize blog articles
- Rewrite blog content professionally
- Improve grammar and readability
- Suggest SEO keywords and hashtags

Always provide professional and well-structured responses.
"""

# =========================
# Generate Response Function
# =========================
def generate_response(user_input):

    try:
        full_prompt = SYSTEM_PROMPT + "\nUser: " + user_input

        response = llm.invoke(full_prompt)


        return response.text

    except Exception as e:

        return "Something went wrong while generating the response."