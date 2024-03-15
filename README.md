# medical-data-extraction
An OCR project to extract information about patient and prescription details.

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
│   │       app.py               //Streamlit App
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
│           8803aa35-fb35-4517-b1eb-cccf2696bf9c.pdf
│           test.pdf
│
├───Notebooks
│       patient_details_parser.ipynb
│       prescription_parser.ipynb
│       RegEx.ipynb
│    
└───reference
        tesseract_papar_by_google.pdf
```