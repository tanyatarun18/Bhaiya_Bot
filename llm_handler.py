# llm_handler.py

import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompt_templates import get_prompt_for_level

# Load environment variables from .env file
load_dotenv()

# --- Configuration for Google Gemini API ---
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Using the faster 'gemini-1.5-flash' model
model = genai.GenerativeModel('gemini-1.5-flash')

# Configuration to allow for longer answers
generation_config = genai.types.GenerationConfig(
    max_output_tokens=8192
)


def get_llm_response(user_question, level="default"):
    """
    Gets a response from the Google Gemini LLM based on the user's question and academic level.
    """
    if not api_key:
        return "Error: GOOGLE_API_KEY is not set. Please check your .env file."

    # The colon was missing here in your file. It is now corrected.
    try:
        # 1. Get the specialized prompt from our templates file
        formatted_prompt = get_prompt_for_level(level, user_question)

        # 2. Make the API call to Gemini, now with the new generation_config
        response = model.generate_content(
            formatted_prompt,
            generation_config=generation_config
        )

        # 3. Extract the text from the response
        ai_answer = response.text
        return ai_answer.strip()

    except Exception as e:
        # Handle potential API errors
        print(f"An error occurred while calling the Gemini API: {e}")
        return "Sorry, I seem to be having trouble connecting to my brain right now. Please try again in a moment."

