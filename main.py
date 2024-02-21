import streamlit as st
from utils.summarize import summarize, template

st.title("AI Summarizer")

with st.sidebar:
    prompt = st.text_area(label="Your Prompt here", value=template.strip(), height=300)


form = st.form("summarize-form")
subject = form.text_input("Subject")
submitted = form.form_submit_button("Summarize")
if submitted:
    with st.spinner("Summarizing..."):
        summary = summarize(prompt, subject)
        st.markdown(summary)
