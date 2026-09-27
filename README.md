# Research Paper RAG Assistant

## What is this project?

This project is an AI assistant that helps us find information from research papers. We can upload one or more research papers as PDF files and ask questions about them. Instead of reading the complete papers to find an answer, the system searches the papers, finds the relevant parts, and gives those parts to an AI model. The AI then uses that information to give us an answer. It will also show the paper and page where the information was found.

## How it works

- Upload research papers.
- Extract the text from the PDFs.
- Break the text into small parts called chunks.
- Convert the chunks into numbers called embeddings.
- Store these embeddings so they can be searched.
- When we ask a question, convert the question into an embedding.
- Find the paper sections that are most similar to the question.
- Give the relevant sections to the AI model.
- The AI generates the answer.
- Show the source and page of the answer.

## Main Technologies

- **Python** – Build the project.
- **PyMuPDF** – Read text from PDF files.
- **Sentence Transformers** – Convert text into embeddings.
- **NumPy** – Work with the numerical data.
- **FAISS/Chroma** – Search and store embeddings.
- **LLM** – Generate the final answer.
- **Streamlit** – Create the simple web interface.
- **Git/GitHub** – Save and manage the project.

## Main Goal

The main goal is to make it easier to understand and search multiple research papers without manually going through every page.

We will build this project step by step and learn each concept when we need it.
