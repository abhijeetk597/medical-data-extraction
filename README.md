# Medica Data Extraction
An OCR project to extract information about Patient and Prescription details from PDF Documents.
Also this project involved creation of a backend server which will process data extraction requests.

## Demo

https://github.com/abhijeetk597/medical-data-extraction/assets/138308825/3d5d90e8-2858-4831-b1d5-97a3874f256c

## Presentation
![1.png](mde-pngs\1.png)
![2.png](mde-pngs\2.png)
![3.png](mde-pngs\3.png)
![4.png](mde-pngs\4.png)
![5.png](mde-pngs\5.png)
![6.png](mde-pngs\6.png)
![7.png](mde-pngs\7.png)
![8.png](mde-pngs\8.png)
![9.png](mde-pngs\9.png)
![10.png](mde-pngs\10.png)
![11.png](mde-pngs\11.png)

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
