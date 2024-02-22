import streamlit as st
from app.summary import summarize, template

st.set_page_config(page_title="📝 Summarizer", page_icon="📝")
st.title("AI Summarizer")

with st.sidebar:
    prompt = st.text_area(label="Your Prompt here", value=template.strip(), height=200)


form = st.form("summarize-form")
subject = form.text_input("Subject")
submitted = form.form_submit_button("Summarize")
if submitted:
    with st.spinner("Summarizing..."):
        summary = summarize(prompt, subject)
        st.markdown(summary)
