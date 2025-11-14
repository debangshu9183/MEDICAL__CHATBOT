import os
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from MEDIBOT.ingest import ingestdata

load_dotenv()

# Chat memory list
chat_history = []


def generation(vstore):
    # Retriever from AstraDB
    retriever = vstore.as_retriever(search_kwargs={"k": 3})

    PRODUCT_BOT_TEMPLATE = """
You are Dr. Nova, a compassionate and knowledgeable medical assistant.

Your role:
- Speak like an experienced, calm, and friendly doctor.
- Explain medical information clearly and in simple language.
- Be empathetic, supportive, and patient-focused.

Critical rules:
1. Use ONLY the information provided in the context.
2. If the information is not in the context, say: "I don't know based on the available information."
3. Do NOT guess, assume, or create medical facts.
4. Avoid giving direct medical diagnoses or prescriptions.
5. Prioritize safety: Encourage users to consult a real healthcare professional when needed.

Tone & style:
- Warm, respectful, and reassuring.
- Conversational, like a real doctor speaking to a patient.
- Short, clear answers—no unnecessary complexity.

Chat History:
{chat_memory}

Context:
{context}

Question:
{question}

Your Answer:
"""

    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)

    # ---- GROQ LLM ----
    llm = ChatGroq(
        api_key=os.getenv("GROQ_API_KEY"),
        model="llama-3.3-70b-versatile",
        temperature=0.2
    )

    # --- MEMORY HANDLER ---
    def add_memory(inputs):
        last_turns = chat_history[-3:]  # last 3 turns only
        formatted = "\n".join([f"User: {u}\nBot: {b}" for u, b in last_turns])
        inputs["chat_memory"] = formatted
        return inputs

    # --- RETRIEVAL HANDLER ---
    def retrieve_context(inputs):
        question = inputs["question"]
        docs = retriever.invoke(question)
        inputs["context"] = "\n\n".join([d.page_content for d in docs])
        return inputs

    chain = (
        RunnablePassthrough()
        | add_memory
        | retrieve_context
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain


def chat_with_bot(chain, question):
    answer = chain.invoke({"question": question})
    chat_history.append((question, answer))
    return answer


if __name__ == "__main__":
    # LOAD ASTRA VECTORSTORE
    vstore = ingestdata()[0]

    chain = generation(vstore)

    print(chat_with_bot(chain, "What is pneumonia?"))
    print(chat_with_bot(chain, "What are the symptoms?"))
    print(chat_with_bot(chain, "How to prevent it?"))
    print(chat_with_bot(chain, "Can you suggest some treatments?"))