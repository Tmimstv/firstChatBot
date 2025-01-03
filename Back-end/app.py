from flask import Flask, request, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if "time" in user_message.lower():
        bot_response = f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}"
    elif "hello" in user_message.lower():
        bot_response = "Hello! How can I assist you today?"
    elif "bye" in user_message.lower():
        bot_response = "Goodbye! Have a great day!"
    else:
        bot_response = "I'm not sure how to respond to that."
    
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
