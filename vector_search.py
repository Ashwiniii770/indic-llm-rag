import faiss
import numpy as np
from embedding_model import create_embedding
from llm_model import generate_answer

# Knowledge base (documents)
documents = [
    "భారత రాజ్యాంగం 1950 జనవరి 26 న అమలులోకి వచ్చింది",
    "India got independence on August 15 1947",
    "Hyderabad is the capital of Telangana"
]

# Create embeddings for documents
embeddings = []

for doc in documents:
    emb = create_embedding(doc)
    embeddings.append(emb)

embeddings = np.array(embeddings)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Ask user question
query = input("Ask your question: ")

# Convert query to embedding
query_embedding = np.array([create_embedding(query)])

# Search similar documents
D, I = index.search(query_embedding, 1)

# Retrieve context
context = documents[I[0][0]]

print("\nRetrieved context:")
print(context)

# Generate answer
answer = generate_answer(context, query)

print("\nGenerated Answer:")
print(answer)