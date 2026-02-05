import streamlit as st
import random

st.set_page_config(page_title="Hobby & Interest Chatbot", page_icon="🎯")

st.title("🎯 Hobby & Interest Chatbot")
st.write("Ask me anything about hobbies, interests, and what you might enjoy!")

# Example hobby categories
HOBBY_CATEGORIES = [
    "Sports", "Music", "Art", "Games", "Technology", "Reading",
    "Writing", "Cooking", "Outdoors", "Fitness", "Collecting",
    "Learning", "Creative hobbies", "Relaxing hobbies", "Social hobbies"
]

# Simple chatbot logic
def bot_reply(user_msg):
    user_msg = user_msg.lower()

    # If user asks for hobby suggestion
    if "suggest" in user_msg or "idea" in user_msg or "hobby" in user_msg:
        return "How about trying **" + random.choice(HOBBY_CATEGORIES) + "**?"

    # If user asks "what hobbies do you know?"
    if "what hobbies" in user_msg:
        return "Here are some hobbies I know:\n- " + "\n- ".join(HOBBY_CATEGORIES)

    # If user asks "what is a good hobby for me?"
    if "for me" in user_msg:
        return "Tell me about what you enjoy — indoors or outdoors? Calm or active?"

    # Default response
    return "That's interesting! Tell me more about what you enjoy."

# Chat UI
with st.form("chat_form"):
    user_input = st.text_input("You:", placeholder="Ask about hobbies or interests...")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.write("**You:**", user_input)
    st.write("**Bot:**", bot_reply(user_input))
