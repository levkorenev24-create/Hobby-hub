Sure — here is the same idea remade in Python with Flask. Flask is a lightweight Python web framework commonly used to build small web apps and APIs, which makes it a good fit for a simple chatbot backend.
Python backend
This version serves a small HTML page and sends user messages to a chat completions API from Python. It uses Flask for the web server and requests for the HTTP call to the model API.
python
# app.py
from flask import Flask, request, jsonify, send_from_directory
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder="public")
API_KEY = os.getenv("OPENAI_API_KEY")

@app.route("/")
def home():
    return send_from_directory("public", "chatbot.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message", "")

        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {"role": "system", "content": "You are a helpful chatbot."},
                    {"role": "user", "content": user_message}
                ],
                "temperature": 0.7
            },
            timeout=60
        )

        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        return jsonify({"reply": reply})

    except Exception:
        return jsonify({"reply": "Server error"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=3000)
HTML page
Place this file in public/chatbot.html. The page sends the typed message to /chat and renders the answer returned by Flask.
xml
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Python Chatbot</title>
  <style>
    body { font-family: Arial, sans-serif; max-width: 700px; margin: 40px auto; }
    #chat { border: 1px solid #ccc; padding: 16px; height: 400px; overflow-y: auto; margin-bottom: 12px; }
    .msg { margin: 8px 0; }
    .user { color: blue; }
    .bot { color: green; }
  </style>
</head>
<body>
  <h1>Simple Python Chatbot</h1>
  <div id="chat"></div>
  <input id="input" type="text" placeholder="Ask anything..." style="width: 80%;" />
  <button onclick="sendMessage()">Send</button>

  <script>
    async function sendMessage() {
      const input = document.getElementById("input");
      const chat = document.getElementById("chat");
      const message = input.value.trim();
      if (!message) return;

      chat.innerHTML += `<div class="msg user"><b>You:</b> ${message}</div>`;
      input.value = "";

      const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
      });

      const data = await res.json();
      chat.innerHTML += `<div class="msg bot"><b>Bot:</b> ${data.reply}</div>`;
      chat.scrollTop = chat.scrollHeight;
    }
  </script>
</body>
</html>
