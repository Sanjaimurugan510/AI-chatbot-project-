from services.speech_to_text import listen_to_microphone
from services.chatbot import get_ai_response
from services.text_to_speech import speak_text


print("\n🎙️ AI Voice Chatbot")
print("====================")
print("Say 'exit' to stop.\n")


while True:

    print("🎤 Speak your question...")

    user_text = listen_to_microphone()

    print("\n📝 You said:")
    print(user_text)

    if user_text.lower() in ["exit", "quit", "stop"]:
        print("\n👋 Goodbye!")
        break

    print("\n🧠 Gemini is thinking...")

    ai_response = get_ai_response(user_text)

    print("\n🤖 AI:")
    print(ai_response)

    print("\n🔊 AI is speaking...")

    speak_text(ai_response)

    print("\n" + "-" * 50 + "\n")