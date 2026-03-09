from embedding_model import create_embedding

text = "భారత రాజ్యాంగం"

embedding = create_embedding(text)

print("Embedding created successfully")
print(embedding[:10])