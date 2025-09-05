Got it 👍 Since your project **uses the OpenAI Python wrapper to connect with Google’s Gemini API**, I’ll make that very clear in the **README**.
Here’s the updated and polished version:

---

# 🤖 Gemini Chatbot (FastAPI + OpenAI Wrapper + HTML/CSS)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-teal?logo=fastapi)
![OpenAI Wrapper](https://img.shields.io/badge/OpenAI-Wrapper-orange?logo=openai)
![Gemini API](https://img.shields.io/badge/Google-Gemini%20API-red?logo=google)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)

This is a **simple chatbot web app** built with **FastAPI**, **HTML/CSS**, and powered by **Google Gemini API** using the **OpenAI Python wrapper**.
It supports **session-based chat history**, message persistence in a file, and a clean UI for chatting.

---

## 🚀 Features

✅ **FastAPI backend** – lightweight and scalable
✅ **HTML + CSS frontend** – clean and responsive design
✅ **OpenAI Wrapper** – connects to Gemini API using OpenAI’s SDK
✅ **Session management** – each user gets a unique session ID
✅ **Chat history** – stored in a `store.txt` file
✅ **Auto-scroll** – always scrolls to the latest message
✅ **Beautiful UI** – user and bot messages styled differently

---

## 📸 Demo Preview

Here’s how the chatbot looks in action:

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
📦 chatbot-app
├── app.py          # Main FastAPI app
├── store.txt       # Stores chat history
└── README.md       # Project documentation
```

---

## ⚡ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/chatbot-app.git
   cd chatbot-app
   ```

2. **Install dependencies**

   ```bash
   pip install fastapi uvicorn openai
   ```

3. **Add your Gemini API key**
   Replace `"API_KEY"` in `app.py` with your actual Gemini API key.

4. **Run the app**

   ```bash
   uvicorn app:app --reload
   ```

5. **Open in browser**
   Go to 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🎨 UI Screenshot

*(Example placeholder – you can add an actual screenshot later)*

![Chatbot UI Preview](https://via.placeholder.com/600x350.png?text=Gemini+Chatbot+Preview)

---

## 📜 Example Conversation

```
You: What is FastAPI?
Bot: FastAPI is a modern, fast web framework for building APIs with Python 3.7+.
```

---

## 💡 Future Improvements

* [ ] Add **database support** (SQLite/Postgres)
* [ ] Add **user authentication**
* [ ] Deploy on **Render / Vercel / AWS**
* [ ] Support **streaming responses**

---

## 🤝 Contributing

Contributions are welcome!
Feel free to **fork this repo** and submit a pull request with your improvements.

---

✨ Built with ❤️ using **FastAPI**, **Gemini API**, and the **OpenAI Wrapper** ✨

---

