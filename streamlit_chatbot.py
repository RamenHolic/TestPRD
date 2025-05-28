import streamlit as st
import requests
import os

headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

# Judul aplikasi
st.title("🤖 Chatbot Asuransi - Gratis & Online")

# Input pertanyaan dari user
user_question = st.text_input("Tanyakan apa pun tentang asuransi:")

# Fungsi untuk kirim ke Hugging Face API
def ask_huggingface(question):
    API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
    payload = {
        "inputs": question,
        "parameters": {"max_new_tokens": 300}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    print("Status code:", response.status_code)
    print("Response text:", response.text)
    if response.status_code != 200:
        return f"Error dari API: {response.status_code} - {response.text}"
    try:
        return response.json()[0]['generated_text']
    except Exception as e:
        return f"Kesalahan parsing JSON: {e}"

# Tampilkan respons jika user memasukkan pertanyaan
if user_question:
    with st.spinner("Sedang memproses jawaban..."):
        answer = ask_huggingface(user_question)
        st.write("**Jawaban:**")
        st.success(answer)
