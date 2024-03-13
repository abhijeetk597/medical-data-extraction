import abc


class MedicalDocParser(metaclass=abc.ABCMeta):

    def __init__(self, text):
        self.text = text

    @abc.abstractmethod
    def parse(self):
        pass