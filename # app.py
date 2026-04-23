# app.py
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def generate_reply(message):
    message = message.lower()

    if "study" in message:
        return "Try studying with Pomodoro technique (25 min focus)."
    elif "task" in message:
        return "Break your tasks into smaller chunks."
    elif "hello" in message:
        return "Hello! I'm your SmartAssist bot."
    else:
        return "I'm here to help with productivity and study tips!"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    reply = generate_reply(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)