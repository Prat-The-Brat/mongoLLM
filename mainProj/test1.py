from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/conversation', methods=['POST'])
def handle_conversation():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid request'}), 400

    conversation_text = data['text']
    print(f"Received text: {conversation_text}")

    # Process the conversation text here if needed

    return jsonify({'result': 'Success!'})

if __name__ == '__main__':
    app.run(debug=True)
