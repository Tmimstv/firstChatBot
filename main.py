import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from datetime import datetime

#Only needed once
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

#load stopwords
stop_words = set(stopwords.words('english'))

#create lemmatizer
#pls push to repo
lemmatizer = WordNetLemmatizer()


def chatbot():
    print("I'm MimzyBot, how can I help?")
    
    while True:
        user_input = input("You: ").lower()
        tokens = word_tokenize(user_input)
        filtered_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
        
        #print(filtered_tokens)
        
        #predefined responses
        if "hello" in filtered_tokens:
            print("MimzyBot: Hello! Need any help today")
        elif "time" in filtered_tokens:
            print(f"MimzyBot: The current time is {datetime.now().strftime('%H:%M:%S')}")
        elif "bye" in filtered_tokens:
            print("MimzyBot: Byeeeee have a nice day!")
            break
        elif "weather" in filtered_tokens:
            print("I cant do weather yet but maybe soon!")
        else:
            print("MimzyBot: im not sure how to respond to that")
        
chatbot()
    
