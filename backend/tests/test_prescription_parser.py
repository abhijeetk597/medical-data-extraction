from backend.src import parser_prescription

# Tests only work in PyCharm. In vs-code I get ModuleNotFoundError.

def test_get_name():
    pp = parser_prescription.PrescriptionParser(document_text_1)
    assert pp.get_field("patient_name") == "Marta Sharapova"

    pp = parser_prescription.PrescriptionParser(document_text_2)
    assert pp.get_field("patient_name") == "Virat Kohli"

def test_get_address():
    pp = parser_prescription.PrescriptionParser(document_text_1)
    assert pp.get_field("patient_address") == "9 tennis court, new Russia, DC"

    pp = parser_prescription.PrescriptionParser(document_text_2)
    assert pp.get_field("patient_address") == "2 cricket blvd, New Delhi"



document_text_1 = """
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Sharapova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

Prednisone 20 md
Lialda 2.4 gram

Directions:
Prednisone, Taper 5 mg every 3 days,
Finish in 2.5 weeks 7
Lialda - take 2 pill everyday for 1 month

Refill: _2_times"""

document_text_2 = """
Dr John Smith, M.D

2 Non-Important street,
New York, Phone (900)-12123- ~2222

Name:  Virat Kohli Date: 2/05/2022

Address: 2 cricket blvd, New Delhi

| Omeprazole 40 mg

Directions: Use two tablets daily for three months

Refill: 3 times"""