# Medica Data Extraction
An OCR project to extract information about Patient and Prescription details from PDF Documents.
Also this project involved creation of a backend server which will process data extraction requests.

## Demo
https://youtu.be/Hf9ha8cl6tw
<video src="mde.mp4" width="560" height="315" controls></video>
<iframe width="560" height="315" src="https://www.youtube.com/embed/Hf9ha8cl6tw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
[![alt text](https://img.youtube.com/vi/Hf9ha8cl6tw/0.jpg)](https://www.youtube.com/watch?v=Hf9ha8cl6tw)

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