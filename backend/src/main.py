from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from extractor import extract
import uuid
import os
from db_utils import DBUtility

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
    print(data)
    return data

@app.post("/patient_details")
def add_new_patient(
    name: str = Form(...),
    phone: str = Form(...),
    vacc_status: str = Form(...),
    med_problems: str = Form(...),
    has_insurance: str = Form(...),
):  
    new_patient = (name, phone, vacc_status, med_problems, has_insurance)

    db = DBUtility()
    resp = db.update_table(table='patient', data=new_patient)
    return resp
    
@app.post("/prescription")
def add_new_prescription(
    name: str = Form(...),
    address: str = Form(...),
    medicines: str = Form(...),
    directions: str = Form(...),
    refill: str = Form(...)
):
    new_prescription = (name, address, medicines, directions, refill)

    db = DBUtility()
    resp = db.update_table(table='prescription', data=new_prescription)
    return resp



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)