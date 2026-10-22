
import os
from google import genai

# Gemini configuration
MODEL_NAME = "gemini-3.8-flash"


def get_ai_response(user_message, *args, **kwargs):
    """
    Generate an AI response using the Gemini API.
    Compatible with calls that pass additional arguments.
    """

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        return (
            "Gemini API key is missing. "
            "Please set the GEMINI_API_KEY environment variable "
            "in your VS Code terminal and restart the app."
        )

    if not user_message or not str(user_message).strip():
        return "Please enter a message."

    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=str(user_message).strip()
        )

        answer = getattr(response, "text", None)

        if answer:
            return answer.strip()

        return "Gemini did not return any text. Please try again."

    except Exception as error:
        print("Gemini API error:", str(error))

        return (
            "Sorry, I could not get a response from Gemini. "
            f"Error: {error}"
        )
