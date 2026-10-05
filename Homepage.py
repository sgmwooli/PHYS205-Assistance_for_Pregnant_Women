import streamlit as st

st.set_page_config(page_title="Homepage")

st.header("Assistance for Pregnant Women")

st.page_link("pages/Decision_Tree.py", label="Go to 'Decision Tree'", icon="🌳")
st.page_link("pages/Chatbot.py", label="Go to 'Chatbot'", icon="💬")
st.page_link("pages/Hospital_Locator.py", label="Go to 'Hospital Locator'", icon="🏥")