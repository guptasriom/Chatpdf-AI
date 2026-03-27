from langchain_huggingface import HuggingFaceEmbeddings

def get_embeddings():
    # Free HuggingFace embedding model (no API key needed)
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
