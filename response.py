
import numpy as np
import nltk
import random
import json
import pickle
from tensorflow.keras.models import load_model

# Download NLTK data (if not already downloaded)
nltk.download('punkt')
nltk.download('wordnet')

# Initialize lemmatizer
lemmatizer = nltk.WordNetLemmatizer()

# Load the saved model
model = load_model('C:/Users/Ajmel/Desktop/Ai_c/try/Travel-Guidence-Chatbot/chatbot.h5')  # Update path if needed

# Load vocabulary and classes (assuming you saved them during training)
with open('words.pkl', 'rb') as f:
    words = pickle.load(f)

with open('classes.pkl', 'rb') as f:
    classes = pickle.load(f)

def clean_text(text): 
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    return tokens

def bag_of_words(text, vocab): 
    tokens = clean_text(text)
    bow = [0] * len(vocab)
    for w in tokens: 
        for idx, word in enumerate(vocab):
            if word == w: 
                bow[idx] = 1
    return np.array(bow)

def pred_class(text, vocab, labels): 
    bow = bag_of_words(text, vocab)
    result = model.predict(np.array([bow]))[0]
    thresh = 0.2
    y_pred = [[idx, res] for idx, res in enumerate(result) if res > thresh]
    y_pred.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in y_pred:
        return_list.append(labels[r[0]])
    return return_list

def get_response(intents_list, intents_json): 
    tag = intents_list[0]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents: 
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result

# Load intents JSON file
with open('C:/Users/Ajmel/Desktop/Ai_c/try/baale_mountain.json', 'r') as file:
    intents_json = json.load(file)

print("Hello, I am your TravelBot!!")

while True:
    message = input("You: ")
    
    if message.lower() in ['exit', 'cancel']:
        print("TravelBot: Are you sure you want to exit? Type 'yes' to exit or 'no' to continue.")
        confirm_exit = input("You: ").lower()
        
        if confirm_exit == 'yes':
            print("TravelBot: Goodbye! Have a nice day!")
            break
        else:
            print("TravelBot: Let's continue! How can I help you?")
            continue
            
    intents = pred_class(message, words, classes)
    result = get_response(intents, intents_json)
    print("TravelBot:", result)