# 📄 ChatPDF AI

Chat with your PDF using AI! Built with RAG (Retrieval-Augmented Generation) architecture.

## 🚀 Features
- Upload any PDF and chat with it instantly
- Powered by DeepSeek V3 via HuggingFace (Free!)
- Beautiful dark theme UI
- Fast vector search with FAISS
- No paid APIs required!

## 🛠️ Tech Stack
- **Backend**: FastAPI + LangChain
- **Frontend**: Streamlit (Dark Theme UI)
- **LLM**: DeepSeek V3 via HuggingFace (Free!)
- **Embeddings**: Sentence Transformers
- **Vector DB**: FAISS

## ⚙️ Local Setup

1. Clone the repository:
```bash
   git clone https://github.com/guptasriom/Chatpdf-AI
   cd Chatpdf-AI
   pip install -r requirements.txt
```

2. Get your FREE HuggingFace token:
   - Go to [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
   - Click **"New Token"** → Select **Read** → Copy token

3. Set your HuggingFace token:
```bash
   # Mac/Linux
   export HF_TOKEN=hf_xxxxxxxx

   # Windows (PowerShell)
   $env:HF_TOKEN="hf_xxxxxxxx"
```

4. Run the backend:
```bash
   cd backend
   uvicorn main:app --reload --port 8000
```

5. Run the frontend (open new terminal):
```bash
   cd frontend
   streamlit run app.py
```

6. Open browser at `http://localhost:8501` 🎉

## 💡 How It Works
1. Upload any PDF file from the sidebar
2. Ask questions in natural language
3. Get instant AI-powered answers from your document!

## ⚠️ Important
- Never share your `HF_TOKEN` publicly
- Each user should generate their own free token from HuggingFace
- Token is completely free — no credit card required!

## 📁 Project Structure
```
Chatpdf-AI/
├── backend/
│   ├── main.py          # FastAPI server
│   ├── rag_pipeline.py  # RAG logic
│   └── embeddings.py    # Embeddings setup
├── frontend/
│   └── app.py           # Streamlit UI
└── requirements.txt
```

## 🤝 Contributing
Pull requests are welcome! Feel free to open an issue or submit a PR.

## ⭐ Show your support
Give a ⭐ if this project helped you!