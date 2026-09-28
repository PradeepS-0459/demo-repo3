# Import required for reading the values from pdf
import fitz

# The path where the pdf exists
pdf_path=r"C:\Users\Pradeep S\Desktop\PROJECTS\RAG\demo-repo3\data\papers\A_Simulation-based_Online_Evolutionary_Algorithm_for_Combat_in_StarCraft_II.pdf"

# Opening the document
#Document is the pdf file here
document=fitz.open(pdf_path)

# We are collecting all the text value into a single large string
full_text=""


# Page corresponds to every page in the pdf file
# The fitz get the values for each page and stores it in the variable text
for page in document:
    text = page.get_text()
    full_text+=text
    
print(full_text)




# The chunk size for the files
chunk_size=1000


# List where chunks are stored
chunks=[]




# for i in range(0,len(full_text),chunk_size):
    # Chunk text size start from the previous end to 1000 characters
    # chunk=full_text[i:i+chunk_size] 
    # Append the chunk files which are created in the list where is chunk is stored
    # chunks.append(chunk)




# Add overlap logic to preserve context between chunks (basically having some 
# parts of the previous chunk in the current chunk)

overlap=200

start=0

while start<len(full_text):
    end=start+chunk_size
    chunk=full_text[start:end]
    chunks.append(chunk)
    start=end-overlap






for chunk in chunks:
    print("\n----CHUNK----")
    print(chunk)

print("Number of chunks:", len(chunks))
