import os
import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)

# ریپلیٹ کے سیکرٹس سے کی حاصل کرنا
api_key = os.environ.get('GEMINI_API_KEY')
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get("message")
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"reply": "معذرت، کچھ خرابی آگئی ہے۔ دوبارہ کوشش کریں۔"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
