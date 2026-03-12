import streamlit as st
import random
import os

# ------------------------------
# Logo
# ------------------------------
logo_path = os.path.join(os.path.dirname(__file__), "images", "Logo.png")
if os.path.exists(logo_path):
    st.image(logo_path, width=150)

# ------------------------------
# Title
# ------------------------------
st.title("Hobby Hub")
st.write("Ask me anything about hobbies!")

# ------------------------------
# Hobby Suggestions
# ------------------------------
HOBBY_CATEGORIES = [
    "Sports", "Music", "Art", "Gaming", "Coding",
    "Reading", "Writing", "Cooking", "Photography",
    "Gardening", "Fitness", "Drawing"
]

# ------------------------------
# Question / Answer Database
# ------------------------------
qa = {

# General
"what are your hobbies": "My hobbies include learning new things, chatting with people, and exploring fun topics.",
"why are hobbies important": "Hobbies help people relax, learn skills, and enjoy their free time.",
"how can i find a new hobby": "Try new activities, watch tutorials, or think about what makes you happy.",
"can hobbies change over time": "Yes, people often discover new interests as they grow.",
"is it okay to have many hobbies": "Of course! Having many hobbies keeps life interesting.",

# Sports
"what sports do people enjoy most": "Popular sports include football, basketball, swimming, and tennis.",
"why do people play sports": "Sports help keep the body healthy and reduce stress.",
"can walking be a hobby": "Yes, walking is a great and relaxing hobby.",
"is dancing a hobby or a sport": "It can be both!",
"what is a good hobby for staying fit": "Running, cycling, yoga, or swimming are great choices.",

# Games & Technology
"do many people enjoy video games": "Yes, video games are a very popular hobby.",
"can gaming be educational": "Yes, many games improve problem-solving and creativity.",
"what is coding as a hobby": "Coding means creating programs or games using a computer.",
"is building games a hobby": "Yes, game development is a fun and creative hobby.",
"what hobbies use technology": "Coding, video editing, photography, and robotics.",

# Music & Arts
"why do people like music": "Music helps express feelings and relax the mind.",
"can singing be a hobby": "Yes, singing is a great hobby for fun and confidence.",
"what instruments are easy to learn": "The ukulele, keyboard, and recorder are beginner-friendly.",
"is drawing a useful hobby": "Yes, drawing improves creativity and focus.",
"can painting reduce stress": "Yes, many people find painting calming.",

# Learning
"is reading a hobby": "Yes, reading is a very popular hobby.",
"what can i learn as a hobby": "Languages, history, science, or new skills.",
"is writing stories a hobby": "Yes, writing is a creative and fun hobby.",
"can learning languages be fun": "Yes, it helps you understand new cultures.",
"what is a quiet hobby": "Reading, drawing, or puzzles.",

# Outdoor
"what are outdoor hobbies": "Hiking, gardening, cycling, and camping.",
"is gardening a good hobby": "Yes, it teaches patience and care.",
"can photography be a hobby": "Yes, it helps capture special moments.",
"what hobby helps you relax": "Meditation, listening to music, or drawing.",
"is collecting things a hobby": "Yes, many people collect coins, stamps, or cards.",

# Fun Questions
"what hobby should i try today": "Try something creative like drawing or something active like cycling!",
"what hobby costs no money": "Walking, writing, or exercising at home.",
"can hobbies turn into jobs": "Yes, many people turn hobbies into careers.",
"what hobby helps with focus": "Puzzles, chess, or drawing.",
"what is the best hobby": "The best hobby is the one you enjoy most!"
}

# ------------------------------
# Chatbot Logic
# ------------------------------
def bot_reply(user_msg):

    msg = user_msg.lower().strip()

    if msg in qa:
        return qa[msg]

    if "suggest" in msg or "idea" in msg:
        return "You could try: **" + random.choice(HOBBY_CATEGORIES) + "**!"

    return "That's interesting! Tell me more about what hobbies you like."

# ------------------------------
# Chat Interface
# ------------------------------
with st.form("chat_form"):
    user_input = st.text_input("You:", placeholder="Ask a hobby question...")
    submitted = st.form_submit_button("Send")

if submitted and user_input:
    st.write("**You:**", user_input)
    st.write("**Bot:**", bot_reply(user_input))
