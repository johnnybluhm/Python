courses  = open("degree_audit.txt").read()
split=courses.split("\n")
class_array=[]
for course in split:
    class_array.append(course.split(","))

print(class_array)
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

f = open("array_of_classes.txt", "w")
f.write(str(final_string))
f.close


def: