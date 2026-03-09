# Low-Resource Indian Language LLM Adaptation with RAG

This project implements a simple Retrieval-Augmented Generation (RAG) system for answering questions in low-resource Indian languages such as Telugu.

The system retrieves relevant knowledge using vector similarity search and then generates answers based on the retrieved context.

---

## Features

- Multilingual sentence embeddings
- Vector similarity search using FAISS
- Retrieval-Augmented Generation pipeline
- Question answering in Indian languages
- Simple and modular Python implementation

---

## Technologies Used

- Python
- Sentence Transformers
- FAISS
- Hugging Face Transformers

---

## Project Architecture

User Question  
↓  
Embedding Model  
↓  
Vector Search (FAISS)  
↓  
Retrieve Relevant Context  
↓  
Generate Answer  

---

## Project Structure
