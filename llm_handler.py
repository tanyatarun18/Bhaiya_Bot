import os
import google.generativeai as genai
from dotenv import load_dotenv
from prompt_templates import get_prompt_for_level

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

generation_config = genai.types.GenerationConfig(
    max_output_tokens=8192
)


def get_llm_response(user_question, level="default"):

    if not api_key:
        return "Error: GOOGLE_API_KEY is not set. Please check your .env file."

    try:
        formatted_prompt = get_prompt_for_level(level, user_question)

        response = model.generate_content(
            formatted_prompt,
            generation_config=generation_config
        )

        ai_answer = response.text
        return ai_answer.strip()

    except Exception as e:
        print(f"An error occurred while calling the Gemini API: {e}")
        return "Sorry, I seem to be having trouble connecting to my brain right now. Please try again in a moment."

