from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import datetime


driver = webdriver.Chrome()

#opens browser
driver.get("https://classes.colorado.edu/")

#gets text box to search for classes
inputElement = driver.find_element_by_id("crit-keyword")

#sends a string to it
inputElement.send_keys("MATH")

#submits the form
inputElement.submit()

#give ajax time to laod
time.sleep(1)

getNodes = 'var results =document.getElementsByClassName("result__code");\n'
loop = 'for(var i=0;i<results.length;i++){\n'
loop = loop+'var course = results[i];\n'+'if(course.innerHTML=="MATH 1150"){\n'
loop= loop+'course.parentElement.parentElement.click();\n'+'break;\n'+'}\n'+'}'
js = getNodes+loop

#search classes for selection
driver.execute_script(js)

#give ajax time to load
time.sleep(3)

#gets table of course info for course
table = driver.execute_script('var a = document.getElementsByClassName("course-sections")[0];\n return a;').text

class_list = table.split("\n")

course_options = []
for course in class_list:
    course_options.append(course.split())
    
print(course_options)



key_list = course_options[0]

course_dict = []
for index in range(6):
    index=index+1
    course_dict.append({
        'number' : course_options[index][0],
        'section' : course_options[index][1],
        'type': course_options[index][2],
        'campus':course_options[index][3],
        'days': course_options[index][4],
        'time': course_options[index][5],
        'status' : course_options[index][8]

        })

print(course_dict)





    
    
    
    
    
    
    #for value,j in range(6):
     #   course_options[i]={
      #      key_list[j] : value
       # }






driver.close()
print("executed normally")




#content = driver.page_source

#soup = BeautifulSoup(content, 'html5lib')

#print(soup.prettify())





