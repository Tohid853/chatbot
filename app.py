
import streamlit as st
import joblib
import random

# Load trained model
model = joblib.load("Chatbot.pkl")
vector = joblib.load("vector.pkl")
res = joblib.load("res.pkl")

st.title("ChatBot")
st.write("Ask Something to the Chatbot")

# 1. Chat history store karna
if "chat" not in st.session_state:
    st.session_state.chat = []

# 2. User input
user = st.text_input("You:", key="user_input")

# 3. Send button
if st.button("Send"):
    if user.strip():

        # User input ko vector mein convert karna
        user_vector = vector.transform([user]).toarray()

        # Prediction
        predict = model.predict(user_vector)[0]

        # Bot ka reply
        if predict in res:
            reply = random.choice(res[predict])
        else:
            reply = "Sorry, mujhe samajh nahi aaya."

        # 4. History mein user aur bot ka message save karna
        st.session_state.chat.append((user, reply))

        # Input clear karne aur page rerun ke liye
        st.rerun()

# 5. Purani aur nayi chat display karna
st.subheader("Chat History")

for user_msg, bot_msg in st.session_state.chat:
    st.write(f"**You:** {user_msg}")
    st.success(f"Bot: {bot_msg}")

