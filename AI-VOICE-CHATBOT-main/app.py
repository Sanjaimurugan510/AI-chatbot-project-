import streamlit as st

from services.speech_to_text import listen_to_microphone
from services.chatbot import get_ai_response
from services.text_to_speech import speak_text


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Voice Assistant",
    page_icon="🎙️",
    layout="wide"
)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "voice_enabled" not in st.session_state:
    st.session_state.voice_enabled = True


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🎙️ AI Voice Assistant")

    st.caption("Version 1.0")

    st.divider()

    st.subheader("⚙️ Settings")

    st.session_state.voice_enabled = st.toggle(
        "🔊 Voice Response",
        value=st.session_state.voice_enabled
    )

    st.divider()

    st.subheader("🧠 AI Stack")

    st.write("🎤 Microphone")
    st.write("📝 OpenAI Whisper")
    st.write("🤖 Gemini Flash-Lite")
    st.write("🔊 pyttsx3")
    st.write("🖥️ Streamlit")

    st.divider()

    st.subheader("✨ Features")

    st.write("✓ Voice conversations")
    st.write("✓ Text conversations")
    st.write("✓ Conversation memory")
    st.write("✓ AI-generated responses")
    st.write("✓ Text-to-speech")
    st.write("✓ Error handling")

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.caption("Built with Python + AI")


# ============================================================
# MAIN HEADER
# ============================================================

st.title("🎙️ AI Voice Assistant")

st.subheader(
    "Speak naturally. Ask anything. Get an intelligent response."
)

st.divider()


# ============================================================
# WELCOME MESSAGE
# ============================================================

if not st.session_state.messages:

    st.info(
        "👋 Welcome! You can type a message or start a voice conversation."
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎤 Input",
            "Voice + Text"
        )

    with col2:
        st.metric(
            "🤖 AI",
            "Gemini"
        )

    with col3:
        st.metric(
            "🔊 Output",
            "Voice"
        )


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])


# ============================================================
# TEXT CHAT
# ============================================================

user_input = st.chat_input(
    "Type your message here..."
)


if user_input:

    # Display user message

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.write(user_input)

    # Generate AI response

    with st.chat_message("assistant"):

        with st.spinner("🧠 Gemini is thinking..."):

            try:

                response = get_ai_response(
                    user_input
                )

                st.write(response)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": response
                    }
                )

            except Exception as e:

                st.error(
                    "⚠️ Unable to get a response. Please try again."
                )

                st.caption(
                    f"Technical details: {str(e)}"
                )

                response = None

    # Voice response

    if response and st.session_state.voice_enabled:

        with st.spinner("🔊 AI is speaking..."):

            try:
                speak_text(response)

            except Exception as e:

                st.warning(
                    f"Voice output failed: {str(e)}"
                )


# ============================================================
# VOICE CONVERSATION
# ============================================================

st.divider()

st.subheader("🎤 Voice Conversation")

st.write(
    "Click the button below and speak your question."
)


voice_button = st.button(
    "🎤 Start Voice Conversation",
    use_container_width=True
)


if voice_button:

    # --------------------------------------------------------
    # Speech to Text
    # --------------------------------------------------------

    try:

        with st.spinner(
            "🎧 Listening... Speak now"
        ):

            user_text = listen_to_microphone()

    except Exception as e:

        st.error(
            "⚠️ Could not access the microphone."
        )

        st.caption(
            f"Technical details: {str(e)}"
        )

        user_text = None


    # --------------------------------------------------------
    # Process voice input
    # --------------------------------------------------------

    if user_text:

        st.success(
            f"📝 You said: {user_text}"
        )

        st.session_state.messages.append(
            {
                "role": "user",
                "content": user_text
            }
        )

        # ----------------------------------------------------
        # Gemini
        # ----------------------------------------------------

        try:

            with st.spinner(
                "🧠 Gemini is thinking..."
            ):

                response = get_ai_response(
                    user_text
                )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )

            with st.chat_message("user"):
                st.write(user_text)

            with st.chat_message("assistant"):
                st.write(response)

            # ------------------------------------------------
            # Text to Speech
            # ------------------------------------------------

            if st.session_state.voice_enabled:

                with st.spinner(
                    "🔊 AI is speaking..."
                ):

                    try:

                        speak_text(response)

                    except Exception as e:

                        st.warning(
                            f"Voice output failed: {str(e)}"
                        )

        except Exception as e:

            st.error(
                "⚠️ Unable to process your request."
            )

            st.caption(
                f"Technical details: {str(e)}"
            )

    else:

        st.warning(
            "I couldn't understand your speech. Please try again."
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Voice Assistant • Whisper + Gemini + pyttsx3 + Streamlit"
)