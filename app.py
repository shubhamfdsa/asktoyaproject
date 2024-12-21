# app.py
from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "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"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    prompt = request.json.get('prompt')
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response['choices'][0]['message']['content']
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'answer': f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
app.py
#