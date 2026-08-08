import os
import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Replit Secrets سے Gemini API Key حاصل کرنا
api_key = os.environ.get('GEMINI_API_KEY')

if not api_key:
    print("WARNING: GEMINI_API_KEY نہیں ملی! Replit Secrets چیک کریں۔")
else:
    genai.configure(api_key=api_key)

# آپ ڈیٹ شدہ Gemini ماڈل
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"reply": "براہ کرم صحیح پیغام کا متن بھیجیں۔"}), 400

        user_message = data.get("message")
        
        # Gemini سے جواب حاصل کرنا
        response = model.generate_content(user_message)
        
        return jsonify({"reply": response.text})

    except Exception as e:
        print(f"Error encountered: {e}")
        return jsonify({"reply": "معذرت، کچھ خرابی آگئی ہے۔ دوبارہ کوشش کریں۔"}), 500

if __name__ == "__main__":
    # Replit کے ماحول کے مطابق پورت سیٹ کرنا
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

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
import os
import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Environment Variable / Secrets سے API Key حاصل کرنا
api_key = os.environ.get('GEMINI_API_KEY')

if api_key:
    genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"reply": "براہ کرم صحیح پیغام کا متن بھیجیں۔"}), 400

        user_message = data.get("message")
        response = model.generate_content(user_message)
        
        return jsonify({"reply": response.text})

    except Exception as e:
        return jsonify({"reply": "معذرت، کچھ خرابی آگئی ہے۔ دوبارہ کوشش کریں۔"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

