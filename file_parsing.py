from abc import ABC, abstractmethod
import csv
import json

class IParseFiles(ABC):
    @abstractmethod
    def parse(self, file_path):
        """
        Parse the given file and return its content.
        What to return depends on the file type:
        - CSV → list of dictionaries (one per row)
        - JSON → Python object (dict or list)
        - TXT → list of lines (strings)
        """
        pass


    @abstractmethod
    def file_type(self) -> str:
        """
        Return the file type handled by the parser (e.g., 'CSV', 'JSON', 'TXT').
        """
        pass


class CSVParser(IParseFiles):
    def parse(self, file_path):
        with open(file_path, mode = 'r', newline = '') as csvfile:
            reader = csv.DictReader(csvfile)
            return [row for row in reader]

    def file_type(self) -> str:
        return "CSV"
    

class JSONParser(IParseFiles):
    def parse(self, file_path):
        with open(file_path, mode = 'r') as jsonfile:
            return json.load(jsonfile)

    def file_type(self) -> str:
        return "JSON"


class TXTParser(IParseFiles):
    def parse(self, file_path):
        with open(file_path, mode = 'r') as txtfile:
            return [line for line in txtfile.readlines()]


    def file_type(self) -> str:
        return "TXT"
