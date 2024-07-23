import requests
import streamlit as st


def call_llama(prompt):

    prompt=f"<s>[INST] {prompt} [/INST]"

    data = {"prompt": prompt, "n_predict": 2048, "temperature": 0.7, "stop":['</s>']}

    response = requests.post("http://localhost:8080/completion", json=data)

    if response.status_code == 200:
        return response.json()['content']

    return "error..."

st.title("💬 Chatbot")
st.caption("🚀 A streamlit chatbot powered by llama.cpp")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    msg = call_llama(prompt)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)