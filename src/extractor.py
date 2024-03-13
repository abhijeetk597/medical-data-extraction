from pdf2image import convert_from_path
import pytesseract
import utils

POPPLER_PATH = r"C:/poppler-24.02.0/Library/bin"
TESSERACT_ENGINE_PATH = r"C:/Program Files/Tesseract-OCR/tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = TESSERACT_ENGINE_PATH


def extract(file_path, file_format):
    # extracting text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ""

    for page in pages:
        processed_image = utils.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang="eng")
        document_text = document_text + "\n" + text

    return document_text

    # if file_format == "prescription":
    #     pass # extract data from prescription
    # elif file_format == "patient_details":
    #     pass # extract data from patient_details

if __name__ == "__main__":
    data = extract("./resources/prescription/pre_2.pdf", "prescription")
    # data = extract("./resources/patient_details/pd_2.pdf", "prescription")
    print(data)