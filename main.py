#import csv
import os
from src.contactextractor import ContactExtractor


if __name__ == "__main__":
    # with open('patterns.csv', 'r') as file:
    #     reader = csv.DictReader(file)
    #     list_of_patterns = {row for row in reader}
    #     patterns = {}
    #     for i in list_of_patterns:
    #         patterns.update(i)
    # print(type(patterns))
    # print(patterns)

    f = open("patterns1.csv", mode='r')
    text = f.read()
    f.close()
    # print(text)
    lines = text.split('\n')
    # print(lines)
    keys = lines[0].split(',,')
    values = lines[1].split(',,')
    # print(keys)
    # print(values)
    # d = {}

    patterns = dict(zip(keys, values))
    print(patterns)
    extractor = ContactExtractor(patterns)

    for file_name in os.listdir('input'):
        extractor.find_data('input' + '/' + file_name)
        extractor.save_data_in_csv()


    # for key in keys:
    #     d[key] = []
    #
    # print(d)
    #
    #
    # for i in range(1, len(lines)):
    #     values = lines[i].split(',,')
    #     print(values)
        # for j in range(len(keys)):
        #     print(values[j], '->', keys[j])
        #     d[keys[j]].append(values[j])

    #print(d)







# Чистовик без дублирующихся строк, с циклом для паттернов и с переменной contact_type
#import pandas as pd
#import re
#import os

#from typing import Dict
#from src.ContactExtractor import ContactExtractor

#if __name__ == "__main__":





# patterns = {'phone_number' : '(\+7\d{10}|8\d{10}|\+7\(\d{3}\)\d{7}|\+7\s\S\d{3}\S\s\d{3}-\d{2}-\d{2}|8\(\d{3}\)\d{3}-\d{2}-\d{2})',
#             'adress' : 'ул.\s[А-Я]{1}[а-я]+,\sдом\s\d+|ул.\s[А-Я]{1}[а-я]+,\sд.\d+'}
# extractor = ContactExtractor(patterns)
#
# for file_name in os.listdir('directory1'):
#     extractor.find_data('directory1' + '/' + file_name)
# extractor.save_data_in_csv()

# import csv
#
# with open('patterns.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     patterns = [row for row in reader]
#
# print(patterns)


# f = open('data.csv', mode='r', encoding='utf-8')
# patterns = f.read()
# f.close()
# data_dict = [row for row in patterns]
# print(data_dict)
