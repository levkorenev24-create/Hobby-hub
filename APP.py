import streamlit as st
import os

# Logo path
logo_path = os.path.join(os.path.dirname(__file__), "images", "Logo.png")

# Show logo first
st.image(logo_path, width=120)

# Then show the title
st.title("Hobby Hub")
st.write("Ask me anything about hobbies, interests, and what you might enjoy!")

# Robust logo path: relative to this Python file
logo_path = os.path.join(os.path.dirname(__file__), "Logo.png")

if os.path.exists(logo_path):
    st.image(logo_path, width=300)
else:
    st.warning(f"Logo not found at '{logo_path}'. Make sure the file exists in the same folder as APP.py.")

# ------------------------------
# Hobby Categories
# ------------------------------
HOBBY_CATEGORIES = [
    "Sports", "Music", "Art", "Games", "Technology", "Reading",
    "Writing", "Cooking", "Outdoors", "Fitness", "Collecting",
    "Learning", "Creative hobbies", "Relaxing hobbies", "Social hobbies"
]

# ------------------------------
# Chatbot Logic
# ------------------------------
def bot_reply(user_msg):
    user_msg = user_msg.lower()
    
    # Suggest a hobby
    if "suggest" in user_msg or "idea" in user_msg or "hobby" in user_msg:
        return "How about trying **" + random.choice(HOBBY_CATEGORIES) + "**?"
    
    # List known hobbies
    if "what hobbies" in user_msg:
        return "Here are some hobbies I know:\n- " + "\n- ".join(HOBBY_CATEGORIES)
    
    # Give advice for personal hobby
    if "for me" in user_msg:
        return "Tell me about what you enjoy — indoors or outdoors? Calm or active?"
    
    # Default reply
    return "That's interesting! Tell me more about what you enjoy."

# ------------------------------
# Chat UI
# ------------------------------
with st.form("chat_form"):
    user_input = st.text_input("You:", placeholder="Ask about hobbies or interests...")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.write("**You:**", user_input)
    st.write("**Bot:**", bot_reply(user_input))
