import streamlit as st
import boto3

lex_client = boto3.client("lex-runtime", "us-east-1")

st.set_page_config(page_title="Chatbot")
st.title("FuriaBot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

input_text = st.chat_input("Chat with your bot here")

if input_text:
    with st.chat_message("user"):
        st.markdown(input_text)

    st.session_state.chat_history.append(
        {"role": "user", "text": input_text},
    )

    try:
        payload = {
            "botName": "FuriaFanBot",
            "botAlias": "BotFuria",
            "userId": "Unique",
            "inputText": input_text,
        }
        response = lex_client.post_text(**payload)
    except Exception as e:
        print(e)
        response = "Desculpe, tive um problema processando sua mensagem. Tente novamente mais tarde."

    with st.chat_message("assistant"):
        st.markdown(response["message"])

    st.session_state.chat_history.append({"role": "assistant", "text": response})
