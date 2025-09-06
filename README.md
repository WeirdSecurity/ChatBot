# 🤖 Gemini Chatbot (FastAPI + OpenAI Wrapper + HTML/CSS)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-teal?logo=fastapi)
![OpenAI Wrapper](https://img.shields.io/badge/OpenAI-Wrapper-orange?logo=openai)
![Gemini API](https://img.shields.io/badge/Google-Gemini%20API-red?logo=google)

This project is a **chatbot web application** built with **FastAPI**, **HTML/CSS**, and powered by the **Google Gemini API** using the **OpenAI Python wrapper**.
It features **session-based conversation tracking**, **persistent chat history**, and a **Clear Chat** option to reset the conversation.

---

## 🚀 Features

✅ **FastAPI backend** – lightweight & scalable
✅ **Gemini API via OpenAI Wrapper** – easy integration with Google’s AI
✅ **Session management** – each user has a unique session ID
✅ **Persistent chat history** – stored in `store.txt`
✅ **Clear button** – wipes all stored messages with one click
✅ **Auto-scroll** – always shows the latest message
✅ **Clean UI** – user messages (blue, right) & bot messages (grey, left)

---

## 📸 Demo Preview

```
You: Hello Bot!  
Bot: Hi there 👋 How can I help you today?  
```

*User messages appear on the **right (blue)**, and bot messages appear on the **left (grey)**.*

---

## 🛠️ Tech Stack

* **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
* **Frontend**: HTML + CSS (vanilla)
* **AI Model**: [Google Gemini API](https://ai.google.dev/)
* **Wrapper**: [OpenAI Python SDK](https://pypi.org/project/openai/)
* **Persistence**: File-based storage (`store.txt`)

---

## 📂 Project Structure

```
📦 gemini-chatbot
├── app.py        # Main FastAPI app
├── store.txt     # Stores all chat history
└── README.md     # Project documentation
```

---

## ⚡ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/gemini-chatbot.git
cd gemini-chatbot
```

2. **Install dependencies**

```bash
pip install fastapi uvicorn openai
```

3. **Set up API Key**
   Replace `"YOUR_API_KEY"` in `app.py` with your actual **Google Gemini API key**.

4. **Run the app**

```bash
uvicorn app:app --reload
```

5. **Open in browser**
   Go to 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📜 Example Conversation

```
You: What is FastAPI?  
Bot: FastAPI is a modern, fast web framework for building APIs with Python 3.7+.  
```

---

## 🔄 Clear Chat

Click the **Clear Chat** button to erase all stored history from `store.txt`.
This will reset the conversation for all sessions.

---

## 🤝 Contributing

Contributions are welcome!
Fork this repo and submit a **pull request** with improvements 🚀

---

✨ Built with ❤️ using **FastAPI**, **Gemini API**, and the **OpenAI Wrapper** ✨

---

Would you like me to also add **screenshots/gif placeholders** (like `![screenshot](demo.png)`) so it looks even more professional on GitHub?
