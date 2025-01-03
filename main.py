import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from datetime import datetime

# Only needed once
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Load stopwords
stop_words = set(stopwords.words('english'))

# Create lemmatizer
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
    "time": ["time", "clock", "hour"]
}

def chatbot():
    print("I'm MimzyBot, how can I help?")
    
    while True:
        user_input = input("You: ").lower()
        
        # Tokenize, remove stop words, and lemmatize
        tokens = word_tokenize(user_input)
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
        
        # Predefined responses
        if matched_intent == "hello":
            print("MimzyBot: Hello! Need any help today?")
        elif matched_intent == "time":
            print(f"MimzyBot: The current time is {datetime.now().strftime('%H:%M:%S')}")
        elif matched_intent == "bye":
            print("MimzyBot: Byeeeee! Have a nice day!")
            break
        elif matched_intent == "weather":
            print("MimzyBot: I can't do weather yet, but maybe soon!")
        else:
            print("MimzyBot: I'm not sure how to respond to that.")

chatbot()
