from pdf2image import convert_from_path
import pytesseract
import utils
from parser_patient_details import PatientDetailsParser
from parser_prescription import PrescriptionParser

POPPLER_PATH = r"C:/poppler-24.02.0/Library/bin"
TESSERACT_ENGINE_PATH = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_ENGINE_PATH


def extract(file_path, file_format):
    # 1. extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ""

    for page in pages:
        processed_image = utils.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang="eng")
        document_text = document_text + "\n" + text

    # 2. extract fields from text
    if file_format == "prescription":
        extracted_data = PrescriptionParser(document_text).parse()

    elif file_format == "patient_details":
        extracted_data = PatientDetailsParser(document_text).parse()
    
    else:
        raise Exception(f"Invalid file format: {file_format}")
    
    return extracted_data

if __name__ == "__main__":
    # data = extract("backend/resources/prescription/pre_1.pdf", "prescription")
    data = extract("backend/resources/patient_details/pd_1.pdf", "patient_details")
    print(data)

    # path = backend\resources\prescription\pre_1.pdf