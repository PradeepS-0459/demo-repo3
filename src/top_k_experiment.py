
import numpy as np
from sentence_transformers import SentenceTransformer

# 1. Sample chunks from a research paper
chunks = [
    "The algorithm uses Differential Evolution for optimization.",
    "The experiments were conducted using StarCraft II.",
    "The proposed method improves strategy optimization.",
    "Differential Evolution is used to optimize real-valued parameters.",
    "The paper compares the proposed algorithm with baseline methods."
]

# 2. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 3. Convert chunks into embeddings
embeddings = model.encode(chunks)

# 4. Enter a question
question = "Which optimization algorithm was used?"

question_embedding = model.encode(question)

# 5. Calculate cosine similarity
similarities = []

for embedding in embeddings:
    score = np.dot(question_embedding, embedding) / (
        np.linalg.norm(question_embedding)
        * np.linalg.norm(embedding)
    )

    similarities.append(score)

# 6. Retrieve the top 3 chunks
top_k = 3

top_indices = np.argsort(similarities)[::-1][:top_k]

# 7. Display results
for rank, index in enumerate(top_indices, start=1):
    print(f"\nRank: {rank}")
    print("Chunk index:", index)
    print("Similarity score:", round(float(similarities[index]), 4))
    print("Text:", chunks[index])
