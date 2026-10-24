# 🎙️ AI Voice Assistant | Python + Gemini AI

An AI-powered voice assistant built using Python that allows users to interact with an intelligent chatbot through text and voice in a web-based interface. The project integrates Gemini AI to generate responses and provides a simple, interactive user experience.

## 🚀 Features

- 💬 **Text Chat:** Ask questions and receive AI-generated responses.
- 🎙️ **Voice Interaction:** Communicate with the assistant using voice input.
- 🤖 **Gemini AI Integration:** Generate intelligent responses using Google's Gemini AI.
- 🌐 **Web-Based Interface:** Interact with the assistant through a Streamlit web application.
- 🔍 **Web Search:** Retrieve relevant online information when web search is configured.
- 🗣️ **Voice Output:** Hear responses spoken aloud if text-to-speech is enabled.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Frontend:** Streamlit
- **AI Model:** Google Gemini AI
- **Speech Recognition:** Speech-to-text library or configured speech recognition service
- **Text-to-Speech:** pyttsx3 or the configured speech output library
- **Web Search:** Configured search API or web search integration

## 📂 Project Structure

```text
AI-Voice-Assistant/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Project dependencies
├── .env                # API keys and environment variables
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

*Note: The structure may vary depending on your implementation.*

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Navigate to the project directory:

```bash
cd YOUR_REPOSITORY
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API Keys

Create a `.env` file in the project directory and add the API keys required by your implementation.

```env
GEMINI_API_KEY=your_gemini_api_key
```

Keep your API keys private. Never upload your `.env` file to GitHub.

### 5. Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

## 🧠 How It Works

1. The user enters a question through text or voice input.
2. Voice input is converted into text using the configured speech recognition system.
3. The application sends the question to Gemini AI.
4. Gemini AI generates a response based on the user's query.
5. The response is displayed in the web interface.
6. If voice output is enabled, the assistant reads the response aloud.
7. If web search is configured, the application can retrieve relevant online information.

## 🎯 Project Objective

The objective of this project is to develop an interactive AI voice assistant that combines natural language processing, speech recognition, and generative AI to provide a convenient way for users to ask questions and receive responses through a web interface.

## 🔮 Future Enhancements

- Add multilingual voice recognition.
- Improve conversation history and context retention.
- Add support for multiple AI models.
- Improve speech recognition accuracy.
- Add a customizable assistant interface.
- Enhance error handling and response speed.

## 👨‍💻 Author

sanjaimurugan510-(https://github.com/Sanjaimurugan510)

## 📄 License

This project is intended for educational and learning purposes. You may add an appropriate open-source license if you plan to distribute or reuse the project.

---

⭐ If you find this project interesting, consider starring the repository on GitHub!
⭐ If you find this project interesting, feel free to explore the repository and share your feedback.
