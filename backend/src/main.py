from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from extractor import extract
import uuid
import os

app = FastAPI()

@app.post("/extract_from_doc")
def extract_from_doc(
    file: UploadFile = File(...),
    file_format: str = Form(...)
):
    content = file.file.read()
    FILE_PATH = "backend/uploads/" + str(uuid.uuid4()) + ".pdf"
    with open(FILE_PATH, "wb") as f:
        f.write(content)

    try:
        data = extract(FILE_PATH, file_format)
    except Exception as e:
        data = {
            'error': str(e)
        }

    if os.path.exists(FILE_PATH):
        os.remove(FILE_PATH)

    return data


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)