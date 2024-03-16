# Medica Data Extraction
An OCR project to extract information about Patient and Prescription details from PDF Documents.
Also this project involved creation of a backend server which will process data extraction requests.

## Demo

https://github.com/abhijeetk597/medical-data-extraction/assets/138308825/3d5d90e8-2858-4831-b1d5-97a3874f256c

## Presentation
![1.jpg](mde-pngs\1.jpg)
![2.jpg](mde-pngs\2.jpg)
![3.jpg](mde-pngs\3.jpg)
![4.jpg](mde-pngs\4.jpg)
![5.jpg](mde-pngs\5.jpg)
![6.jpg](mde-pngs\6.jpg)
![7.jpg](mde-pngs\7.jpg)
![8.jpg](mde-pngs\8.jpg)
![9.jpg](mde-pngs\9.jpg)
![10.jpg](mde-pngs\10.jpg)
![11.jpg](mde-pngs\11.jpg)

## Directory Structure of Project
```
medical-data-extraction
│   .gitignore
│   README.md
│   requirements.txt
│
├───backend
│   │
│   ├───resources
│   │   │
│   │   ├───patient_details
│   │   │       pd_1.pdf
│   │   │       pd_2.pdf
│   │   │
│   │   └───prescription
│   │           pre_1.pdf
│   │           pre_2.pdf
│   │
│   ├───src
│   │       extractor.py
│   │       main.py              //Fastapi Backend Server
│   │       parser_generic.py
│   │       parser_patient_details.py
│   │       parser_prescription.py
│   │       utils.py
│   │    
│   ├───tests
│   │       test_prescription_parser.py
│   │
│   └───uploads
│
├───frontend
│       app.py              //Streamlit app
│
├───Notebooks
│       01_prescription_parser.ipynb
│       02_patient_details_parser.ipynb
│       03_RegEx.ipynb
│    
└───reference
        tesseract_papar_by_google.pdf
```
