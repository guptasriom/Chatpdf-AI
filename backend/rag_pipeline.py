from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from embeddings import get_embeddings
import requests
import os

def process_pdf(file_path):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    docs = text_splitter.split_documents(documents)
    embeddings = get_embeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

def query_pdf(vectorstore, query):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query)
    context = "\n".join([doc.page_content for doc in docs])

    HF_TOKEN = os.environ.get("HF_TOKEN", "")

    prompt = f"""Answer ONLY from the context below.
If not found, say 'Not in document'.

Context:
{context}

Question:
{query}

Answer:"""

    response = requests.post(
        "https://router.huggingface.co/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {HF_TOKEN}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek-ai/DeepSeek-V3-0324",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 256
        }
    )

    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    if response.status_code != 200:
        return f"API Error {response.status_code}: {response.text}"

    if not response.text.strip():
        return "Empty response from HuggingFace API"

    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"]
    elif "error" in result:
        return f"HF Error: {result['error']}"
    else:
        return str(result)