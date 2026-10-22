# 🎙️ AI-Powered Voice Chatbot

An AI-powered voice chatbot that allows users to interact naturally through speech. It converts spoken questions into text, generates intelligent responses using Google Gemini, and converts the responses into audio for playback in the browser.

## 📌 Overview

This project combines speech recognition, Generative AI, and text-to-speech technology to create a browser-based conversational assistant.

The application uses **Django** to serve the web interface and **FastAPI** to handle backend APIs for speech transcription, AI responses, and audio generation.

## ✨ Features

* 🎤 **Voice Input:** Record speech using the browser microphone.
* 📝 **Speech-to-Text:** Transcribe recorded audio using OpenAI Whisper.
* 🤖 **AI Responses:** Generate conversational answers using Google Gemini.
* 🔊 **Text-to-Speech:** Convert AI responses into audio using gTTS.
* 💬 **Chat Interface:** Display user messages and AI responses in the browser.
* 🌐 **Browser Audio Playback:** Listen to the generated responses directly in the web application.
* 🔗 **API Integration:** Connect the Django frontend with the FastAPI backend.

## 🛠️ Tech Stack

| Category              | Technologies          |
| --------------------- | --------------------- |
| Programming Language  | Python                |
| Frontend              | HTML, CSS, JavaScript |
| Web Framework         | Django                |
| API Framework         | FastAPI               |
| Generative AI         | Google Gemini         |
| Speech-to-Text        | OpenAI Whisper        |
| Text-to-Speech        | gTTS                  |
| API Server            | Uvicorn               |
| Environment Variables | python-dotenv         |
| Version Control       | Git, GitHub           |

## 🔄 Project Workflow

1. **Voice Input:** The user records a question through the browser microphone.
2. **Audio Upload:** JavaScript sends the recorded audio to the FastAPI backend.
3. **Speech Recognition:** Whisper converts the audio into text.
4. **AI Processing:** Google Gemini generates a response based on the transcribed question.
5. **Speech Generation:** gTTS converts the AI-generated text into audio.
6. **Audio Playback:** The browser plays the generated audio to the user.

```text
User Speaks
    ↓
Browser Microphone
    ↓
Django Web Interface
    ↓
FastAPI Backend
    ↓
OpenAI Whisper
    ↓
Google Gemini
    ↓
gTTS
    ↓
Browser Audio Playback
```

## 📂 Project Structure

```text
AI-VOICE-CHATBOT/
│
├── services/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── speech_to_text.py
│   ├── browser_tts.py
│   └── text_to_speech.py
│
├── api/
│   └── main.py
│
├── backend/
│   ├── manage.py
│   └── backend/
│       ├── settings.py
│       ├── urls.py
│       ├── asgi.py
│       └── wsgi.py
│   └── chat/
│       ├── views.py
│       ├── urls.py
│       └── templates/
│           └── chat/
│               └── index.html
│
├── .env
├── .gitignore
└── README.md
```

*Note: The structure above represents the main application files. Include other files and folders that exist in your actual repository.*

## ⚙️ Installation and Setup

### Prerequisites

* Python installed
* Git installed
* FFmpeg installed and available on your system PATH
* A Google Gemini API key
* A working internet connection for Gemini API requests and gTTS audio generation

### 1. Clone the Repository

```bash
git clone https://github.com/padmavathy-mca/AI-VOICE-CHATBOT.git
cd AI-VOICE-CHATBOT
```

### 2. Create and Activate a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install django fastapi uvicorn python-multipart openai-whisper google-genai python-dotenv gTTS
```

### 4. Configure the Gemini API Key

Create a `.env` file in the project root and add your API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Replace the placeholder with your own Gemini API key. Never commit your real API key to GitHub.

### 5. Start the FastAPI Backend

Open a terminal in the project root:

```bash
python -m uvicorn api.main:app --reload --port 8001
```

The API will be available at:

* API: http://127.0.0.1:8001/
* Interactive API documentation: http://127.0.0.1:8001/docs

### 6. Start the Django Frontend

Open a second terminal:

```powershell
cd backend
python manage.py migrate
python manage.py runserver 8000
```

Open the chatbot in your browser:

**http://127.0.0.1:8000/**

Allow microphone access when prompted and start speaking to the chatbot.

## 📸 Screenshots

Add screenshots of your actual working application to a `screenshots/` folder in the repository.

For example, once you add these files:

```text
screenshots/
├── chatbot-interface.png
└── voice-conversation.png
```

You can display them here:

### Chatbot Interface

![AI Voice Chatbot Interface](screenshots/chatbot-interface.png)

### Voice Conversation

![AI Voice Chatbot Conversation](screenshots/voice-conversation.png)

*Replace these example image paths with screenshots committed to your repository.*

## 🚀 Future Enhancements

* Add persistent, user-specific conversation history.
* Improve conversation memory across sessions.
* Add light and dark themes.
* Add controls to stop or interrupt audio playback.
* Improve error handling and microphone recording feedback.
* Deploy the Django frontend and FastAPI backend for online access.

## 🎯 Learning Outcomes

* Integrating Generative AI into a web application.
* Building REST APIs with FastAPI.
* Serving web interfaces with Django.
* Implementing speech-to-text and text-to-speech pipelines.
* Connecting frontend and backend services.
* Managing API credentials through environment variables.

## 👩‍💻 Author

**Padmavathy**

GitHub: [padmavathy-mca](https://github.com/padmavathy-mca)

---

⭐ If you find this project interesting, feel free to explore the repository and share your feedback.
