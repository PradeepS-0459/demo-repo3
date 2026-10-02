import ollama


def generate_answer(context, question):

    prompt = f"""
You are a research paper assistant.

Answer the question directly using only the information given in the context.

If the context contains the answer, give the answer clearly.
Do not say that the information is missing if the answer is present.

Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]



context = """
The basic optimization method is a differential evolution
(DE) algorithm since it can effectively optimize the real
number coordinates.
"""

question = "What algorithm was used in the program?"

answer = generate_answer(context, question)

print("\nAnswer:")
print(answer)