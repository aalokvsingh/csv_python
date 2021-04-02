import csv
import os

file_name= 'samplefile.csv'
base_path = os.getcwd()
file_path = os.path.join(base_path,file_name)
print(file_path)
#Dialect helps in grouping together many specific formatting patterns like delimiter, skipinitialspace, quoting, escapechar into a single dialect name.
csv.register_dialect(
    'mydialect',
    delimiter= '\t',
    skipinitialspace = True,
    quoting = csv.QUOTE_NONE,
    lineterminator='\n'
)

with open(file_path, "a",newline='\n',encoding='utf-8') as file_handler:
    writer = csv.writer(file_handler,dialect="mydialect")
    writer.writerow(['4', 'Guido', 'Python'])
    
    
#write a file usinf dictWriter
with open(file_path,"a",newline="\n",encoding="utf-8") as file_handler:
    heading = ['SN','Name','Contribution']
    writer = csv.DictWriter(file_handler,dialect="mydialect",fieldnames=heading)
    writer.writeheader()
    writer.writerow({'SN':'5',"Name":'Alok',"Contribution":"Python"})
    
    