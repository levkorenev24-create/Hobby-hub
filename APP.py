import streamlit as st
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI()

st.set_page_config(page_title="ChatGPT+", page_icon="🤖")

st.title("🤖 ChatGPT+ Clone")

# Store chat history
if "messages" not in st.session_state:
st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
with st.chat_message(msg["role"]):
st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask me anything...")

if prompt:
# Save user message
st.session_state.messages.append({"role": "user", "content": prompt})

with st.chat_message("user"):
st.markdown(prompt)

# Get response from OpenAI
with st.chat_message("assistant"):
response = client.chat.completions.create(
model="gpt-5-mini", # fast + cheap (you can change to gpt-5.3)
messages=st.session_state.messages
)

reply = response.choices[0].message.content
st.markdown(reply)

# Save assistant reply
st.session_state.messages.append({"role": "assistant", "content": reply})
