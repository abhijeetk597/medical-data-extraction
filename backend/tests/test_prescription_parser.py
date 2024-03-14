from backend.src.parser_prescription import PrescriptionParser
import pytest
# Tests only work in PyCharm. In vs-code I get ModuleNotFoundError.

@pytest.fixture()
def doc_1_maria():
    document_text = """
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
    return PrescriptionParser(document_text)

def test_get_name(doc_1_maria):
    assert doc_1_maria.get_field("patient_name") == "Marta Sharapova"

def test_get_address(doc_1_maria):
    assert doc_1_maria.get_field("patient_address") == "9 tennis court, new Russia, DC"




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