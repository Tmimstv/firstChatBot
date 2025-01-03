from flask import Flask, request, jsonify
from flask_cors import CORS
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
import datetime

# Initialize Flask app and CORS
app = Flask(__name__)
CORS(app)

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize NLP tools
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Function to get synonyms using WordNet
def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return synonyms if synonyms else set()

# Function to match a word to intents using WordNet
def match_intent(word, intent_words):
    for intent_word in intent_words:
        if word in get_synonyms(intent_word) or word == intent_word:
            return intent_word
    return None

# Intent mapping
intents = {
    "hello": ["hello", "hi", "greetings"],
    "bye": ["bye", "goodbye", "later"],
    "time": ["time", "clock", "hour"],
    "weather": ["weather", "forecast", "climate"]
}

# MimzyBot chat logic
def mimzybot_response(user_message):
    # Tokenize, remove stop words, and lemmatize
    tokens = word_tokenize(user_message.lower())
    filtered_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]

    # Match user input to intents
    matched_intent = None
    for word in filtered_tokens:
        for intent, keywords in intents.items():
            matched_intent = match_intent(word, keywords)
            if matched_intent:
                break
        if matched_intent:
            break

    # Generate a response
    if matched_intent == "hello":
        return "Hello! How can I assist you today?"
    elif matched_intent == "time":
        return f"The current time is {datetime.datetime.now().strftime('%H:%M:%S')}."
    elif matched_intent == "bye":
        return "Goodbye! Have a great day!"
    elif matched_intent == "weather":
        return "I can't fetch weather data yet, but maybe soon!"
    else:
        return "I'm not sure how to respond to that."

# Flask route for chat
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    bot_response = mimzybot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
