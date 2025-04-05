import streamlit as st
from model.generator import QuestionGenerator

st.title("AutoQuest - AI Question Generator")

text_input = st.text_area("Enter text to generate questions:", height=200)

if st.button("Generate Questions") and text_input:
    qg = QuestionGenerator()
    questions = qg.generate_questions(text_input)
    st.subheader("Generated Questions:")
    for i, q in enumerate(questions):
        st.markdown(f"**{i+1}.** {q}")