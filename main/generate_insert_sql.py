import json
import os
import sys
from pathlib import Path
parent_dir = Path('..')

db_file = open(os.path.join(parent_dir, "sql_scripts", "insert_data.sql"), 'w')
class_json_loc = os.path.join(parent_dir, "data_files", "class_json.txt")

with open(class_json_loc) as f:
    course_list = json.load(f)
for course in course_list:

    for index,option in enumerate(course):
        db_string ='INSERT INTO course_data\n VALUES\n(\n'
        if 'Class Nbr:' in option.keys():
            db_string += option['Class Nbr:']+',\n'
        else:
            db_string += '00000'+',\n'
        if len(option['Section #:'])>3:
            db_string += option['Section #:'][0:2]+',\n'
        else:
            db_string += option['Section #:']+',\n'
        db_string += '\''+option['Type:']+'\',\n'
        db_string += '\''+option['Campus:']+'\',\n'
        db_string += '\''+option['Status:']+'\',\n'
        db_string += 'make_date('+option['start_date']+'),\n'
        db_string += 'make_date('+option['end_date']+'),\n'
        db_string += '\''+option['name']+'\',\n'
        db_string += 'make_time('+option['start_time']+'),\n'
        db_string += 'make_time('+option['end_time']+'),\n'
        db_string += '\''+option['Meets:']+'\',\n'
        db_string += '\''+option['Instructor:']+'\'\n);\n'
        db_file.write(db_string)

db_file.close()
print("executed normally")