import streamlit as st
from vector_search import search_answer

st.title("Indian Language RAG Assistant")

question = st.text_input("Ask your question")

if question:
    answer = search_answer(question)
    st.write(answer)