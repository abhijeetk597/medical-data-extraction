import re
from parser_generic import MedicalDocParser

class PatientDetailsParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return{
            "patient_name": self.get_field("patient_name"),
            "phone_no": self.get_field("phone_no"),
            "vaccination_status": self.get_field("vaccination_status"),
            "medical_problems": self.get_field("medical_problems"),
            "has_insurance": self.get_field("has_insurance")
        }
    
    def get_field(self, field_name):
        pattern_dict = {
            "patient_name": {"pattern": "Date\n+([a-zA-Z]+\s+[a-zA-Z]+).\D{3}"},
            "phone_no": {"pattern": "(\(\d{3}\).\d{3}.\d{4}).+Weight"},
            "vaccination_status": {"pattern": "vaccination\?\n+(Yes|No)"},
            "medical_problems": {"pattern": "headaches\):\n+(\D+?)\n"},
            "has_insurance": {"pattern": "insurance\?\n+(Yes|No)"}
        }

        pattern_object = pattern_dict.get(field_name)
        if pattern_object:
            matches = re.findall(pattern_object["pattern"], self.text)
            if len(matches) > 0:
                return matches[0].strip()
            
        
if __name__ == "__main__":
    text_1 = """
17/12/2020

Patient Medical Record

Patient Information Birth Date
Jerry Lucas May 2 1998
(279) 920-8204 " Weight:
4218 Wheeler Ridge Dr $7
anaes 14201 Height:

In Case of Emergency
meee

Joe Lucas 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles:

IMMUNE NOT IMMUNE
Have you had the Hepatitis B vaccination?
Yes ,

List any Medical Problems (asthma, seizures, headaches):
N/A

abc"""

    text_2 = """
17/12/2020

Patient Medical Record

Patient Information Birth Date

Kathy Crawford May 6 1972

(737) 988-0851 Weight’

9264 Ash Dr 95

New York City, 10005 ‘

United States Height
190

In Case of Emergency
ee
Simeone Crawford 9266 Ash Dr
H New York City, New York, 10005
ome phone United States
(990) 375-4621
Work phone
Genera! Medical History
_

eS I ee

ne

a enna

Chicken Pox (Varicella): Measies:

IMMUNE IMMUNE

Have you had the Hepatitis B vaccination?

No

List any Medical Problems (asthma, seizures, headaches):

Migraine

abc"""

    pdp_1 = PatientDetailsParser(text_1)
    pdp_2 = PatientDetailsParser(text_2)

    print(pdp_1.parse())
    print(pdp_2.parse())
