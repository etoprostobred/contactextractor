# Contact extractor
___
Look through text-documents, extract data like phone number and address according to certain patterns and save it to csv.


# Usage
1. Copy text-documents into directory “input”.
2. Start the program.
3. Get csv-file named in format “YYYY-MM-DD_file.csv” in directory “output” containing structured by columns data:

| document_name | contact_type | contact_value |
| ----------- | ----------- | ----------- |
| doc1.txt    | address | ул. Название, д.11 |
| doc2.txt    | phone_number | +7 (999) 999-99-99 |

# Settings

Default settings include patterns, which can find two data types:

- Address (format: “ул. Название, д.11”, “ул. Название, дом 11”)
- Phone number (format: “+7 (999) 999-99-99”, “8(999)999-99-99”, “+79999999999”, “89999999999”)

To customize search query add your regex in file “patterns.csv”.
