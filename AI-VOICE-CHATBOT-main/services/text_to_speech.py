import re
import pyttsx3


def clean_text_for_speech(text):

    # Remove Markdown headings
    text = re.sub(r"#+\s*", "", text)

    # Remove bold and italic Markdown
    text = text.replace("**", "")
    text = text.replace("__", "")
    text = text.replace("*", "")

    # Remove bullet points
    text = re.sub(r"^\s*[-•]\s*", "", text, flags=re.MULTILINE)

    # Remove Markdown links
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def speak_text(text):

    clean_text = clean_text_for_speech(text)

    engine = pyttsx3.init()

    engine.setProperty(
        "rate",
        170
    )

    engine.setProperty(
        "volume",
        1.0
    )

    engine.say(clean_text)

    engine.runAndWait()