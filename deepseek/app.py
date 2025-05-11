from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Configuración del cliente de OpenAI
client = OpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Obtener la consulta del frontend
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({'error': 'No se proporcionó un mensaje'}), 400

        # Enviar la consulta a la API de OpenAI
        chat = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",
            messages=[
                {
                    "role": "user",
                    "content": user_message
                }
            ]
        )
        # Obtener la respuesta
        response = chat.choices[0].message.content
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)