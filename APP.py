import streamlit as st
import random
import os

st.title("Hobby Hub")
st.write("Ask me anything about hobbies, interests, and what you might enjoy!")

# Debug: check file
st.write("Current working directory:", os.getcwd())
st.write("Logo exists?", os.path.exists("images/logo.png"))

# Display logo
st.image("images/logo.png", width=120)

# Hobby categories
HOBBY_CATEGORIES = [
"Sports", "Music", "Art", "Games", "Technology", "Reading",
"Writing", "Cooking", "Outdoors", "Fitness", "Collecting",
"Learning", "Creative hobbies", "Relaxing hobbies", "Social hobbies"
]

# Chatbot logic
def bot_reply(user_msg):
user_msg = user_msg.lower()
if "suggest" in user_msg or "idea" in user_msg or "hobby" in user_msg:
return "How about trying **" + random.choice(HOBBY_CATEGORIES) + "**?"
if "what hobbies" in user_msg:
return "Here are some hobbies I know:\n- " + "\n- ".join(HOBBY_CATEGORIES)
if "for me" in user_msg:
return "Tell me about what you enjoy — indoors or outdoors? Calm or active?"
return "That's interesting! Tell me more about what you enjoy."

# Chat UI
with st.form("chat_form"):
user_input = st.text_input("You:", placeholder="Ask about hobbies or interests...")
submitted = st.form_submit_button("Send")

if submitted and user_input:
st.write("**You:**", user_input)
st.write("**Bot:**", bot_reply(user_input))


