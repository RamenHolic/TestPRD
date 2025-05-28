import streamlit as st
import requests
import os

# Judul aplikasi
st.title("🤖 Chatbot Asuransi - Gratis & Online")

# Input pertanyaan dari user

API_KEY = os.getenv("HUGGINGFACE_API_KEY")
if not API_KEY:
    raise ValueError("API key tidak ditemukan! Set environment variable HUGGINGFACE_API_KEY dulu.")

API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
HEADERS = {"Authorization": f"Bearer {API_KEY}"}
# Fungsi untuk kirim ke Hugging Face API
def ask_huggingface(question: str) -> str:
    payload = {
        "inputs": question,
        "parameters": {"max_new_tokens": 150}
    }
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code != 200:
        return f"Error dari API: {response.status_code} - {response.text}"
    try:
        generated_text = response.json()[0]['generated_text']
        return generated_text.strip()
    except Exception as e:
        return f"Error parsing response: {e}"


def main():
    print("Chatbot Asuransi Kesehatan (ketik 'exit' untuk keluar)")
    while True:
        user_input = input("Kamu: ")
        if user_input.lower() in ("exit", "keluar"):
            print("Chatbot: Terima kasih! Sampai jumpa.")
            break
        answer = ask_huggingface(user_input)
        print(f"Chatbot: {answer}")
        
if __name__ == "__main__":
    main()
