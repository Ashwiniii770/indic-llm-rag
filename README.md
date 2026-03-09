# Low-Resource Indian Language LLM Adaptation using RAG

This project demonstrates a simple Retrieval-Augmented Generation (RAG) system for answering questions in low-resource Indian languages such as Telugu.

## Features
- Multilingual sentence embeddings
- Vector similarity search using FAISS
- Retrieval-Augmented Generation pipeline
- Question answering based on contextual knowledge

## Technologies Used
- Python
- Sentence Transformers
- FAISS
- Hugging Face Transformers

## Project Structure
embedding_model.py → generates multilingual embeddings  
vector_search.py → performs vector similarity search  
llm_model.py → generates answers  
app.py → testing script

## Example

Question:
భారత రాజ్యాంగం ఎప్పుడు అమలులోకి వచ్చింది?

Answer:
భారత రాజ్యాంగం 1950 జనవరి 26 న అమలులోకి వచ్చింది.
