import csv
import os
file_name = "samplefile.csv"
base_path = os.getcwd()
file_path = os.path.join(base_path,file_name)


#Dialect helps in grouping together many specific formatting patterns like delimiter, skipinitialspace, quoting, escapechar into a single dialect name.
csv.register_dialect(
    'mydialect',
    delimiter= '\t',
    skipinitialspace = True,
    quoting = csv.QUOTE_NONE
)

with open(file_name,"r") as csv_file_handler:  
    csv_reader = csv.reader(csv_file_handler,dialect='mydialect')
    for row in csv_reader:
        print(row)
        
'''
o/p:
['SN', 'Name', 'Contribution']
['1', '"Linus Torvalds"', 'Linux Kernel']
['2', 'Tim Berners-Lee', 'World Wide Web']
['3', 'Guido van Rossum', 'Python Programming']
'''
#Read CSV files with csv.DictReader()
with open(file_path,"r") as file_handler:
    csv_file = csv.DictReader(file_handler,dialect="mydialect")
    print(csv_file)
    for row in csv_file:
        print(dict(row))

'''
o/p:
{'SN': '1', 'Name': '"Linus Torvalds"', 'Contribution': 'Linux Kernel'}
{'SN': '2', 'Name': 'Tim Berners-Lee', 'Contribution': 'World Wide Web'}
{'SN': '3', 'Name': 'Guido van Rossum', 'Contribution': 'Python Programming'}
'''