from flask import Flask, request, jsonify, render_template
from llm_handler import get_llm_response
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/api/ask', methods=['POST'])
def ask_question():

    data = request.get_json()

    if not data or 'query' not in data:
        return jsonify({"error": "Invalid request. 'query' field is required."}), 400

    user_query = data['query']
    user_level = data.get('level', 'default')  # Uses 'default' if no level is sent

    answer = get_llm_response(user_query, user_level)

    return jsonify({"answer": answer})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
