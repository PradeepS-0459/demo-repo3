import fitz

pdf_path=r"C:\Users\Pradeep S\Desktop\PROJECTS\RAG\demo-repo3\data\papers\A_Simulation-based_Online_Evolutionary_Algorithm_for_Combat_in_StarCraft_II.pdf"


document=fitz.open(pdf_path)


for page in document:
    text=page.get_text()
    print(text)
