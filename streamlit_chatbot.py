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
    API_URL = "https://huggingface.co/masterful/gligen-1-4-generation-text-box"
    headers = {"Authorization": f"Bearer YOUR_HUGGINGFACE_API_KEY"}

    payload = {
        "inputs": f"[INST] {question} [/INST]",
        "parameters": {"max_new_tokens": 200}
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    print(response.status_code)
    print(response.text)
    try:
        return response.json()[0]['generated_text']
    except Exception as e:
        return "Maaf, terjadi kesalahan: " + str(e)

# Tampilkan respons jika user memasukkan pertanyaan
if user_question:
    with st.spinner("Sedang memproses jawaban..."):
        answer = ask_huggingface(user_question)
        st.write("**Jawaban:**")
        st.success(answer)
