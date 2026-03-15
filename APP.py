import streamlit as st
import os

# Page setup
st.set_page_config(page_title="Hobby Hub", page_icon="Logo.png")

# ---------- Logo ----------
logo_path = os.path.join(os.path.dirname(__file__), "Logo.png")

if os.path.exists(logo_path):
    st.image(logo_path, width=350)
else:
    st.warning("Logo.png not found. Make sure it is in the same folder as APP.py.")

# ---------- Title ----------
st.title("Ask me anything about hobbies!")

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
    177. Q: Can hobbies help people slow down? A: Yes, slowing down is good. 178. Q: Is it okay to love quiet hobbies? A: Yes, quiet joy is beautiful. 179. Q: Can hobbies be soft and gentle? A: Yes, softness is strength. 180. Q: Are hobbies meant to feel kind? A: Yes, kindness is key. 181. Q: Can hobbies bring warmth to life? A: Yes, they add warmth. 182. Q: Is it okay to change hobbies? A: Yes, change is natural. 183. Q: Can hobbies help people feel balanced? A: Yes, they support balance. 184. Q: Are hobbies a form of care? A: Yes, caring for yourself matters. 185. Q: Can hobbies make ordinary days nicer? A: Yes, they brighten days. 186. Q: Is enjoying hobbies a good habit? A: Yes, it’s a healthy habit. 187. Q: Can hobbies feel like comfort? A: Yes, comfort is important. 188. Q: Are hobbies allowed to be simple joys? A: Yes, simple joy is perfect. 189. Q: Can hobbies help people breathe easier? A: Yes, they ease the mind. 190. Q: Are hobbies about happiness, not pressure? A: Yes, happiness comes first. 191. Q: Can hobbies help people feel okay? A: Yes, they offer support. 192. Q: Is enjoying hobbies a kind choice? A: Yes, kindness starts with you. 193. Q: Can hobbies be a quiet celebration? A: Yes, gentle joy counts. 194. Q: Are hobbies meant to feel safe and warm? A: Yes, always. 195. Q: Can hobbies make people feel at home? A: Yes, comfort matters. 196. Q: Is it okay to enjoy hobbies your own way? A: Yes, your way is best. 197. Q: Can hobbies help people feel whole? A: Yes, they support well-being. 198. Q: Are hobbies a soft place to land? A: Yes, they can be. 199. Q: Can hobbies bring gentle happiness? A: Yes, gentle happiness is beautiful. 200. Q: What kind of hobbies are best? A: The kind that feel kind to you 💛
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
