import streamlit as st
import time

st.title("AI Summarizer")

with st.sidebar:
    prompt = st.text_area("Your prompt here", height=300)


def summarize():
    content = ""
    time.sleep(2)
    with open("output_cache/summary.md", "r") as f:
        content = f.read()
        st.markdown(content)


form = st.form("summarize-form")
text = form.text_input("Subject")
submitted = form.form_submit_button("Summarize")
if submitted:
    summarize()
