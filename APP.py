import streamlit as st
import os

# Page setup
st.set_page_config(page_title="Hobby Hub", page_icon="Logo.png")

# ---------- Logo ----------
logo_path = os.path.join(os.path.dirname(__file__), "Logo.png")

if os.path.exists(logo_path):
    st.image(logo_path, width=150)
else:
    st.warning("Logo.png not found. Make sure it is in the same folder as APP.py.")

# ---------- Title ----------
st.title("Logo.png Hobby Hub Chatbot")
st.write("Ask me anything about hobbies!")

# ---------- Knowledge Base ----------
qa_pairs = {

"what are your hobbies": "My hobbies include learning new things, chatting with people, and exploring fun topics.",
"why are hobbies important": "Hobbies help people relax, learn skills, and enjoy their free time.",
"how can i find a new hobby": "Try new activities, watch tutorials, or think about what makes you happy.",
"can hobbies change over time": "Yes, people often discover new interests as they grow.",
"is it okay to have many hobbies": "Of course! Having many hobbies keeps life interesting.",

"what sports do people enjoy most": "Popular sports include football, basketball, swimming, and tennis.",
"why do people play sports": "Sports help keep the body healthy and reduce stress.",
"can walking be a hobby": "Yes, walking is a great and relaxing hobby.",
"is dancing a hobby or a sport": "It can be both!",
"what is a good hobby for staying fit": "Running, cycling, yoga, or swimming are great choices.",

"do many people enjoy video games": "Yes, video games are a very popular hobby.",
"can gaming be educational": "Yes, many games improve problem-solving and creativity.",
"what is coding as a hobby": "Coding means creating programs or games using a computer.",
"is building games a hobby": "Yes, game development is a fun and creative hobby.",
"what hobbies use technology": "Coding, video editing, photography, and robotics.",

"why do people like music": "Music helps express feelings and relax the mind.",
"can singing be a hobby": "Yes, singing is a great hobby for fun and confidence.",
"what instruments are easy to learn": "The ukulele, keyboard, and recorder are beginner-friendly.",
"is drawing a useful hobby": "Yes, drawing improves creativity and focus.",
"can painting reduce stress": "Yes, many people find painting calming.",

"is reading a hobby": "Yes, reading is a very popular hobby.",
"what can i learn as a hobby": "Languages, history, science, or new skills.",
"is writing stories a hobby": "Yes, writing is a creative and fun hobby.",
"can learning languages be fun": "Yes, it helps you understand new cultures.",
"what is a quiet hobby": "Reading, drawing, or puzzles.",

"what are outdoor hobbies": "Hiking, gardening, cycling, and camping.",
"is gardening a good hobby": "Yes, it teaches patience and care.",
"can photography be a hobby": "Yes, it helps capture special moments.",
"what hobby helps you relax": "Meditation, listening to music, or drawing.",
"is collecting things a hobby": "Yes, many people collect coins, stamps, or cards.",

"can cooking be a hobby": "Yes, cooking is creative and useful.",
"why do people bake as a hobby": "Baking is fun and makes tasty results.",
"is watching movies a hobby": "Yes, many people enjoy movies in their free time.",
"can traveling be a hobby": "Yes, traveling helps explore new places and cultures.",
"is learning magic tricks a hobby": "Yes, it’s fun and entertaining.",

"can hobbies help make friends": "Yes, shared hobbies bring people together.",
"are group hobbies better than solo hobbies": "Both are good — it depends on the person.",
"can hobbies improve confidence": "Yes, learning skills builds confidence.",
"is volunteering a hobby": "It can be a meaningful hobby.",
"can hobbies reduce stress": "Yes, hobbies help people relax.",

"what hobby should i try today": "Try something creative or something active!",
"what is a hobby for rainy days": "Reading, gaming, or drawing.",
"what hobby costs no money": "Walking, writing, or exercising at home.",
"can hobbies turn into jobs": "Yes, many people turn hobbies into careers.",
"what hobby helps with focus": "Puzzles, chess, or drawing.",

"what hobby is good for kids": "Drawing, sports, and building things.",
"what hobby is good for adults": "Reading, cooking, or fitness activities.",
"what hobby is good for creativity": "Art, music, or writing.",
"can hobbies make you happier": "Yes, doing what you enjoy boosts happiness.",
"what is the best hobby": "The best hobby is the one you enjoy most!"
}

# ---------- User Input ----------
user_input = st.text_input("Ask a question about hobbies:")

# ---------- Chatbot Logic ----------
if user_input:

    question = user_input.lower().strip().replace("?", "")

    answer = None

    for q in qa_pairs:
        if q in question:
            answer = qa_pairs[q]
            break

    if answer:
        st.success(answer)
    else:
        st.info("That's an interesting question! Try asking about hobbies, sports, music, games, or creativity.")
