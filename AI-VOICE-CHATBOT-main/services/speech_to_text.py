import os
import tempfile

import speech_recognition as sr
import whisper


# Load Whisper model once when the service starts
model = whisper.load_model("base")


def listen_to_microphone():
    """
    Desktop microphone recording.
    """

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(
            source,
            timeout=10,
            phrase_time_limit=15
        )

    print("Transcribing with Whisper...")

    wav_data = audio.get_wav_data()

    temp_audio_path = "temp_audio.wav"

    with open(
        temp_audio_path,
        "wb"
    ) as audio_file:

        audio_file.write(wav_data)

    try:

        result = model.transcribe(
            temp_audio_path,
            language="en"
        )

        text = result["text"].strip()

        return text

    finally:

        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)


def transcribe_audio(audio_bytes):
    """
    Transcribe audio uploaded from the browser.
    """

    with tempfile.NamedTemporaryFile(
        suffix=".wav",
        delete=False
    ) as temp_audio:

        temp_audio.write(audio_bytes)

        temp_audio_path = temp_audio.name

    try:

        print("Transcribing browser audio with Whisper...")

        result = model.transcribe(
            temp_audio_path,
            language="en"
        )

        text = result["text"].strip()

        print("Transcription:", text)

        return text

    finally:

        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)