from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
from google.generativeai.types import GenerationConfig

app = Flask(__name__, static_folder="static")

genai.configure(api_key="AIzaSyD_sxHzRaC9cWZy4-UbDyP-cwcDHMJyPDk")  # Replace with your Gemini API Key

model = genai.GenerativeModel("models/gemini-1.5-flash")
chat_history = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if not user_input:
        return jsonify({"reply": "❌ Empty message."})

    chat_history.append({"role": "user", "parts": [user_input]})

    try:
        response = model.generate_content(
            contents=chat_history,
            generation_config=GenerationConfig(
                temperature=0.7,
                max_output_tokens=512
            )
        )
        reply = response.text
        chat_history.append({"role": "model", "parts": [reply]})
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"❌ Error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)
