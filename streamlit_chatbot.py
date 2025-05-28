import os
import requests
import streamlit as st

API_KEY = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}

def ask_huggingface(question: str) -> str:
    payload = {
        "inputs": question,
        "parameters": {"max_new_tokens": 150}
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code != 200:
        return f"Error dari API: {response.status_code} - {response.text}"
    try:
        return response.json()[0]["generated_text"].strip()
    except Exception as e:
        return f"Error parsing response: {e}"

def main():
    st.title("Chatbot Asuransi Kesehatan")
    st.write("Tanya apa saja tentang asuransi kesehatan dan klaim premi.")
    
    if "history" not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("Kamu:", "")

    if user_input:
        answer = ask_huggingface(user_input)
        st.session_state.history.append({"user": user_input, "bot": answer})

    for chat in st.session_state.history:
        st.markdown(f"**Kamu:** {chat['user']}")
        st.markdown(f"**Chatbot:** {chat['bot']}")

if __name__ == "__main__":
    main()
