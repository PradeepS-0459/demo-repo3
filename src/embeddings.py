from sentence_transformers import SentenceTransformer


# We have loaded the enbedding model here
model=SentenceTransformer("all-MiniLM-L6-v2")

# Example text
text="Evolutionary algorithms are optimization methods used to solve complex problems."

# We are converting the text into an embedding here
embeddings=model.encode(text)


print("Embeddings:")
print(embeddings)

print(len(embeddings))

