import pandas as pd
import re
from typing import Dict


class ContactExtractor:
    def __init__(self, patterns: Dict[str, str]) -> None:
        self.patterns = patterns
        self.data = {
            'document_name': [],
            'contact_type': [],
            'contact_value': []
        }

    def find_data(self, file_name: str) -> Dict:
        f = open(file_name, mode='r', encoding='utf-8')
        text = f.read()
        f.close()
        for item in self.patterns.items():
            contact_type, contact_pattern = item
            contact_matches = re.findall(contact_pattern, text)
            if len(contact_matches) >= 1:
                print(f'Найдены данные типа "{contact_type}": {contact_matches}')
                self.data['document_name'] = self.data['document_name'] + [file_name] * len(contact_matches) # list[str]
                self.data['contact_type'] = self.data['contact_type'] + [contact_type] * len(contact_matches) # list[str]
                self.data['contact_value'] = self.data['contact_value'] + contact_matches # list[str]
            else:
                print(f'Данные типа "{contact_type}" не найдены.')
        return self.data

    def save_data_in_csv(self):
        if len(self.data['contact_value']) >= 1:
            df = pd.DataFrame(self.data)
            df.to_csv('file.csv')
        else:
            print('Нет сохранённых данных для записи.')