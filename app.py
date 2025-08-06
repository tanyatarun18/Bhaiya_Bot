# app.py

# Import the necessary functions from the Flask library
from flask import Flask, request, jsonify, render_template
from llm_handler import get_llm_response
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)

# Enable Cross-Origin Resource Sharing (CORS) to allow browser requests
# This is good practice even when serving the file from the same origin.
CORS(app)


# --- Main Website Route ---
# This new route will serve your beautiful website frontend.
@app.route('/')
def home():
    """
    This function runs when a user goes to the main URL (e.g., http://127.0.0.1:5000).
    It looks inside the 'templates' folder for 'index.html' and sends it to the browser.
    """
    return render_template('index.html')


# --- API Endpoint for Questions ---
# This is the same API route you built before. It acts as the "brain".
@app.route('/api/ask', methods=['POST'])
def ask_question():
    """
    This function handles the POST requests sent from the website's JavaScript.
    It receives the question, gets an answer from the LLM, and sends it back.
    """
    # Get the JSON data sent from the frontend
    data = request.get_json()

    # Basic validation to make sure the request is not empty
    if not data or 'query' not in data:
        return jsonify({"error": "Invalid request. 'query' field is required."}), 400

    # Extract the question and academic level from the data
    user_query = data['query']
    user_level = data.get('level', 'default')  # Uses 'default' if no level is sent

    # Get the AI-generated answer from our handler
    answer = get_llm_response(user_query, user_level)

    # Send the answer back to the website in JSON format
    return jsonify({"answer": answer})


# This block allows you to run the server by typing "python app.py" in the terminal
if __name__ == '__main__':
    # host='0.0.0.0' makes the server accessible from your local network
    # port=5000 is the standard port for Flask development
    app.run(host='0.0.0.0', port=5000, debug=True)
