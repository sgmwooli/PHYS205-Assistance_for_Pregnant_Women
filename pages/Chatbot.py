# Cell 3 - Streamlit chatbot wrapper
import streamlit as st
import random
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import sqlite3

st.set_page_config(page_title="Chatbot")

# Connect to SQLite DB
conn = sqlite3.connect('/Users/maxwooliscroft/Desktop/NEW_Website_-_PHYS205_-_Long_Project/pages/chatbot9.db')
cur = conn.cursor()

# Load responses from DB
def load_responses():
    responses = {}
    cur.execute('SELECT keyword, response FROM responses')
    for keyword, response in cur.fetchall():
        if keyword not in responses:
            responses[keyword] = []
        responses[keyword].append(response)
    return responses

responses = load_responses()
lemmatizer = WordNetLemmatizer()

# Your chatbot function
def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())
    lemmatized_input = [lemmatizer.lemmatize(word) for word in tokens]

    if any(word in lemmatized_input for word in ['hi', 'hello', 'hey']):
        return random.choice(responses.get('greeting', []))
    elif any(word in lemmatized_input for word in ['bye', 'goodbye', 'exit']):
        return random.choice(responses.get('bye', []))
    elif any(word in lemmatized_input for word in ['emergency', 'urgent', 'help']):
        return random.choice(responses.get('emergency', []))
    elif any(word in lemmatized_input for word in ['hospital', 'doctor', 'clinic']):
        return random.choice(responses.get('hospital', []))
    elif any(word in lemmatized_input for word in ['pregnancy', 'baby', 'trimester']):
        return random.choice(responses.get('pregnancy', []))
    elif any(word in lemmatized_input for word in ['nutrition', 'diet', 'food']):
        return random.choice(responses.get('nutrition', []))
    elif any(word in lemmatized_input for word in ['symptoms', 'signs', 'feeling']):
        return random.choice(responses.get('symptoms', []))
    elif any(word in lemmatized_input for word in ['trimester', 'trimesters']):
        return random.choice(responses.get('trimester', []))
    elif any(word in lemmatized_input for word in ['first', '1st']):
        return random.choice(responses.get('first', []))
    elif any(word in lemmatized_input for word in ['second', '2nd']):
        return random.choice(responses.get('second', []))  
    elif any(word in lemmatized_input for word in ['third', '3rd']):
        return random.choice(responses.get('third', []))
    elif any(word in lemmatized_input for word in ['contractions', 'contraction', 'labour']):
        return random.choice(responses.get('contractions', []))
    elif any(word in lemmatized_input for word in ['vision', 'blurry', 'eyes']):
        return random.choice(responses.get('vision', []))
    elif any(word in lemmatized_input for word in ['stomach', 'bellyache', 'cramps', 'cramping', 'abdominal']):
        return random.choice(responses.get('abdominal pain', []))
    elif any(word in lemmatized_input for word in ['liverpool']):
        return random.choice(responses.get('Liverpool', []))
    elif any(word in lemmatized_input for word in ['birmingham']):
        return random.choice(responses.get('Birmingham', []))
    elif any(word in lemmatized_input for word in ['manchester']):
        return random.choice(responses.get('Manchester', []))
    elif any(word in lemmatized_input for word in ['leicester']):
        return random.choice(responses.get('Leicester', []))
    elif any(word in lemmatized_input for word in ['lancaster']):
        return random.choice(responses.get('Lancaster', []))
    elif any(word in lemmatized_input for word in ['nottingham']):
        return random.choice(responses.get('Nottingham', []))
    elif any(word in lemmatized_input for word in ['london']):
        return random.choice(responses.get('London', []))
    elif any(word in lemmatized_input for word in ['bath']):
        return random.choice(responses.get('Bath', []))
    elif any(word in lemmatized_input for word in ['bradford']):
        return random.choice(responses.get('Bradford', []))
    elif any(word in lemmatized_input for word in ['brighton', 'hove']):
        return random.choice(responses.get('Brighton and Hove', []))
    elif any(word in lemmatized_input for word in ['oxford']):
        return random.choice(responses.get('Oxford', []))
    elif any(word in lemmatized_input for word in ['bristol']):
        return random.choice(responses.get('Bristol', []))
    elif any(word in lemmatized_input for word in ['cambridge']):
        return random.choice(responses.get('Cambridge', []))
    elif any(word in lemmatized_input for word in ['newcastle']):
        return random.choice(responses.get('Newcastle', []))
    elif any(word in lemmatized_input for word in ['Ectopic pregnancy', 'ectopic', 'Ectopic Pregnancy']):
        return random.choice(responses.get('Ectopic pregnancy', []))
    elif any(word in lemmatized_input for word in ['Miscarriage', 'miscarriage', 'loss of pregnancy']):
        return random.choice(responses.get('Miscarriage', []))  
    elif any(word in lemmatized_input for word in ['Infection', 'infection', 'sepsis']):
        return random.choice(responses.get('Infection', []))    
    elif any(word in lemmatized_input for word in ['High blood pressure', 'blood pressure', 'High Blood Pressure']):
        return random.choice(responses.get('High blood pressure', []))
    elif any(word in lemmatized_input for word in ['Hyperemesis Gravidrum', 'hyperemesis gravidrum']):
        return random.choice(responses.get('Hyperemesis Gravidrum', []))
    elif any(word in lemmatized_input for word in ['Auto-immune disease', 'Auto immune disease']):
        return random.choice(responses.get('Auto-immune disease', []))   
    elif any(word in lemmatized_input for word in ['Gestational diabetes', 'Gestational Diabetes']):
        return random.choice(responses.get('Gestational diabetes', [])) 
    elif any(word in lemmatized_input for word in ['Incompetant cervix', 'incompetant cervix']):
        return random.choice(responses.get('Incompetant cervix', []))  
    elif any(word in lemmatized_input for word in ['Pre-eclampsia', 'Pre eclampsia']):
        return random.choice(responses.get('Pre-eclampsia', []))   
    elif any(word in lemmatized_input for word in ['Placental abruption', 'placental abruption']):
        return random.choice(responses.get('Placental abruption', []))    
    else:
        return "I'm sorry, I didn't quite understand that. Could you please rephrase?"

# Streamlit UI
st.title("🤖 Pregnancy Chatbot")

# Initialise chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input box
user_input = st.chat_input("Ask me anything about pregnancy, symptoms, hospitals...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get bot response
    response = chatbot_response(user_input)

    # Display bot message
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

st.page_link("Homepage.py", label="Home", icon="🏠")