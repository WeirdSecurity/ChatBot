from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from openai import OpenAI
import uuid


client = OpenAI(
    api_key="API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

STORE_FILE = "store.txt"
sessions = {}

def load_history():
    history = [{"role": "system", "content": "You are a helpful assistant."}]
    try:
        with open(STORE_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(":", 2)
                if len(parts) == 3:
                    _, role, content = parts
                    if role == "user":
                        history.append({"role": "user", "content": content.strip()})
                    elif role == "bot":
                        history.append({"role": "assistant", "content": content.strip()})
    except FileNotFoundError:
        pass
    return history

def load_session(session_id):
    chat = []
    try:
        with open(STORE_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith(f"{session_id}:user: "):
                    chat.append({"role": "user", "content": line.split("user: ", 1)[1].strip()})
                elif line.startswith(f"{session_id}:bot: "):
                    chat.append({"role": "assistant", "content": line.split("bot: ", 1)[1].strip()})
    except FileNotFoundError:
        pass
    return chat

def save_message(session_id, role, content):
    with open(STORE_FILE, "a", encoding="utf-8") as f:
        f.write(f"{session_id}:{role}: {content}\n")

def chatbot(session_id: str, prompt: str) -> str:
    history = load_history()
    history.append({"role": "user", "content": prompt})
    save_message(session_id, "user", prompt)

    resp = client.chat.completions.create(
        model="gemini-2.0-flash-lite",
        messages=history
    )
    reply = resp.choices[0].message.content
    save_message(session_id, "bot", reply)
    return reply

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    session_id = str(uuid.uuid4())
    sessions[request.client.host] = session_id
    return chat_page(session_id, [])

@app.post("/chat", response_class=HTMLResponse)
def chat(request: Request, prompt: str = Form(...), session_id: str = ""):
    if not session_id:
        session_id = sessions.get(request.client.host, str(uuid.uuid4()))

    chatbot(session_id, prompt)
    session_chat = load_session(session_id)
    return chat_page(session_id, session_chat)

@app.post("/clear")
def clear_chat():
    # Clear the file completely
    open(STORE_FILE, "w", encoding="utf-8").close()
    new_session_id = str(uuid.uuid4())
    return RedirectResponse(url=f"/?session_id={new_session_id}", status_code=303)

def chat_page(session_id, session_chat):
    chat_html = ""
    for msg in session_chat:
        role_class = "user" if msg["role"] == "user" else "bot"
        chat_html += f"<div class='message {role_class}'><b>{'You' if role_class == 'user' else 'Bot'}:</b> {msg['content']}</div>"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Gemini Chatbot</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .chat-container {{
                width: 500px;
                background: white;
                border-radius: 10px;
                box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
                display: flex;
                flex-direction: column;
                padding: 20px;
            }}
            h2 {{
                text-align: center;
                color: #333;
            }}
            .messages {{
                flex: 1;
                overflow-y: auto;
                margin-bottom: 15px;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 8px;
                background: #fafafa;
            }}
            .message {{
                margin: 8px 0;
                padding: 10px;
                border-radius: 8px;
                max-width: 75%;
                word-wrap: break-word;
            }}
            .user {{
                background: #007bff;
                color: white;
                margin-left: auto;
                text-align: right;
            }}
            .bot {{
                background: #e9ecef;
                color: black;
                margin-right: auto;
            }}
            form {{
                display: flex;
                gap: 10px;
            }}
            input[type="text"] {{
                flex: 1;
                padding: 10px;
                border-radius: 6px;
                border: 1px solid #ccc;
            }}
            input[type="submit"] {{
                padding: 10px 20px;
                border: none;
                border-radius: 6px;
                background: #007bff;
                color: white;
                cursor: pointer;
            }}
            input[type="submit"]:hover {{
                background: #0056b3;
            }}
            .clear-btn {{
                background: #dc3545;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 12px;
                cursor: pointer;
                margin-bottom: 10px;
            }}
            .clear-btn:hover {{
                background: #a71d2a;
            }}
        </style>
    </head>
    <body>
        <div class="chat-container">
            <h2>Gemini Chatbot</h2>
            <form method="post" action="/clear">
                <button type="submit" class="clear-btn">Clear Chat</button>
            </form>
            <div class="messages" id="messages">
                {chat_html}
            </div>
            <form method="post" action="/chat?session_id={session_id}">
                <input type="text" name="prompt" placeholder="Type your message..." required>
                <input type="submit" value="Send">
            </form>
        </div>
        <script>
            const messages = document.getElementById('messages');
            messages.scrollTop = messages.scrollHeight;
        </script>
    </body>
    </html>
    """
