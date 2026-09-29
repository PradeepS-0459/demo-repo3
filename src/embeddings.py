from numpy import size
import fitz
from sentence_transformers import SentenceTransformer

# Location of the file
pdf_path=r"C:\Users\Pradeep S\Desktop\PROJECTS\RAG\demo-repo3\data\papers\A_Simulation-based_Online_Evolutionary_Algorithm_for_Combat_in_StarCraft_II.pdf"

document=fitz.open(pdf_path)

full_text=""

for page in document:
    text=page.get_text()
    full_page+=text


chunk_size=1000
overlap=200
chunks=[]
start=0

while start<len(full_text):
    end=start+chunk_size
    chunk=full_text[start:end]
    chunks.append(chunk)
    start=end-overlap





# We have loaded the enbedding model here
model=SentenceTransformer("all-MiniLM-L6-v2")

# Example text
text="Evolutionary algorithms are optimization methods used to solve complex problems."

# We are converting the text into an embedding here
embeddings=model.encode(text)


print("Embeddings:")
print(embeddings)

print(len(embeddings))

