from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from openai import OpenAI

client = OpenAI(
    api_key="API",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

history = [{"role": "system", "content": "You are a helpful assistant."}]

def chatbot(prompt: str) -> str:
    history.append({"role": "user", "content": prompt})
    resp = client.chat.completions.create(
        model="gemini-1.5-flash",
        messages=history
    )
    reply = resp.choices[0].message.content
    history.append({"role": "assistant", "content": reply})
    return reply


app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>Chatbot</h2>
    <form method="post" action="/chat">
        <input type="text" name="prompt" placeholder="Type your message">
        <input type="submit" value="Send">
    </form>
    """

@app.post("/chat", response_class=HTMLResponse)
def chat(prompt: str = Form(...)):
    reply = chatbot(prompt)
    return f"""
    <h2>Gemini Chatbot</h2>
    <p><b>You:</b> {prompt}</p>
    <p><b>Bot:</b> {reply}</p>
    <form method="post" action="/chat">
        <input type="text" name="prompt" placeholder="Type your message">
        <input type="submit" value="Send">
    </form>
    """