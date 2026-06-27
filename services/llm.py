import json
import requests
from config import GROQ_API_KEY

def get_answer(question: str, chunks: list) -> str:
    context = "\n\n".join(chunks)
    prompt = f"""You are a helpful assistant. Answer the question below using ONLY the context provided.
If the answer is not in the context, say "I don't know based on this document."

Context:
{context}

Question: {question}

Answer:"""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    data = response.json()
    return data["choices"][0]["message"]["content"]


def get_answer_with_citations(question: str, chunks: list) -> dict:
    context = ""
    for i, chunk in enumerate(chunks):
        context += f"[Source {i+1} - Page {chunk['page']}]\n{chunk['text']}\n\n"

    prompt = f"""You are a helpful assistant. Answer the question below using ONLY the context provided.
After your answer, list which sources you used.
If the answer is not in the context, say "I don't know based on this document."

Context:
{context}

Question: {question}

Answer:"""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    data = response.json()
    answer = data["choices"][0]["message"]["content"]

    citations = [
        {
            "page": chunk["page"],
            "relevance_score": chunk["relevance_score"],
            "excerpt": chunk["text"][:200] + "..."
        }
        for chunk in chunks
    ]

    return {
        "answer": answer,
        "citations": citations
    }


def stream_answer(question: str, chunks: list):
    context = ""
    for i, chunk in enumerate(chunks):
        page = chunk.get("page", "unknown")
        context += f"[Source {i+1} - Page {page}]\n{chunk['text']}\n\n"

    prompt = f"""You are a helpful assistant. Answer the question below using ONLY the context provided.
If the answer is not in the context, say "I don't know based on this document."

Context:
{context}

Question: {question}

Answer:"""

    with requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "stream": True
        },
        stream=True
    ) as response:
        for line in response.iter_lines():
            if line:
                line = line.decode("utf-8")
                if line.startswith("data: "):
                    data = line[6:]
                    if data == "[DONE]":
                        break
                    try:
                        chunk_data = json.loads(data)
                        delta = chunk_data["choices"][0]["delta"]
                        if "content" in delta:
                            yield delta["content"]
                    except:
                        continue