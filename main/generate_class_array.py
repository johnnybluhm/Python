import json
import os
from pathlib import Path

parent_dir = Path('..')
degree_audit_loc = os.path.join(parent_dir, "data_files", "degree_audit.txt")
class_array_loc = os.path.join(parent_dir, "data_files", "array_of_classes2.txt")


courses  = open(degree_audit_loc).read()
split=courses.split("\n")
class_array=[]
for course in split:
    class_array.append(course.split(","))

final_string=[]

for courses in class_array:
    subject=courses[0][0:4]
    for index, course_number in enumerate(courses):
        if(index==0):
            course_name = subject+' '+courses[0][4:8]
            final_string.append(course_name)
            print(course_name)
        else:
            course_name=subject+' '+course_number
            final_string.append(course_name)

f = open(class_array_loc, "w")
f.write(str(final_string))
f.close


