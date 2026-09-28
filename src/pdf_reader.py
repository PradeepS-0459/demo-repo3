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


chunk_size=1000

chunks=[]

for i in range(0,len(full_text),chunk_size):
    chunk=full_text[i:i+chunk_size]
    chunks.append(chunk)



