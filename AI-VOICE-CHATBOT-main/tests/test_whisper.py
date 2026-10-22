from services.speech_to_text import listen_to_microphone


print("\n🎙️ Speak something...")

text = listen_to_microphone()

print("\n📝 Whisper Transcription:")
print(text)