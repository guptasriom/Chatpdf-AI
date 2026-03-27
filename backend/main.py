
from fastapi import FastAPI, UploadFile
from rag_pipeline import process_pdf, query_pdf
import tempfile

app = FastAPI()

vectorstore = None

@app.post("/upload")
async def upload_pdf(file: UploadFile):
    global vectorstore
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name
    vectorstore = process_pdf(tmp_path)
    return {"message": "PDF processed successfully"}

@app.get("/ask")
def ask_question(q: str):
    global vectorstore
    if vectorstore is None:
        return {"answer": "Please upload a PDF first"}
    try:
        answer = query_pdf(vectorstore, q)
        return {"answer": answer}
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print("FULL ERROR:", error_detail)  # backend terminal mein dikhega
        return {"answer": f"Error: {str(e)} | Detail: {error_detail[-300:]}"}