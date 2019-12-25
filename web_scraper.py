from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from dateutil import parser
import pandas as pd
from datetime import datetime
from pprint import pprint
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




courses  = open("degree_audit.txt").read()
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
            
        else:
            course_name=subject+' '+course_number
            final_string.append(course_name)



driver = webdriver.Chrome()
wait = WebDriverWait(driver, 1)



#opens browser


#hard code class values for now
course_list = []
course_sel = final_string

#TEST ARRAY = course_sel = ['CSCI 3002', 'CSCI 3753', 'MATH 1150']

#after for loop array with each element being an array of class objects is available
for index,sel in enumerate(course_sel):

    driver.get("https://classes.colorado.edu/")

    subj= sel.split()


    #gets text box to search for classes
    inputElement = driver.find_element_by_id("crit-keyword")

    #can begin loop here to loop for multiple classes
    #sends a string to it
    inputElement.send_keys(subj[0])

    #submits the form
    inputElement.submit()

    #give ajax time to load
    try:
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "result__code")))
    except:
        pass

    getNodes = 'var results =document.getElementsByClassName("result__code");\n'
    loop = 'for(var i=0;i<results.length;i++){\n'
    loop = loop+'var course = results[i];\n'+'if(course.innerHTML=="'+sel+'"){\n'
    loop= loop+'course.parentElement.parentElement.click();\n'+'break;\n'+'}\n'+'}'
    js = getNodes+loop

    #search classes for selection
    driver.execute_script(js)

    #give ajax time to load
    #if timeout exception is thrown just continue loop
    try:
        table= wait.until(EC.presence_of_element_located((By.CLASS_NAME, "course-sections")))        
    except:
        table = None

    #table = driver.execute_script('var a = document.getElementsByClassName("course-sections")[0];\n return a;')

    if(table != None):
    
        table= table.get_attribute('outerHTML')
        soup=BeautifulSoup(table, 'html.parser')


        #anchor tags have all course info, is an array
        courses = soup.find_all("a")

        #array to hold course dictionaries
        course_array = []

        #go through one class
        for course in courses:
            course_dict = dict()
            #loop though row of anchor tag
            for child in course.contents:
                #get inner HTML of row and split
                parse=child.get_text().split("  ")
                #add key,value pair of course data to dictionary
                course_dict[parse[0]]=parse[1]
            #add dictionary to course array
            course_dict['name']=sel
            course_array.append(course_dict)

        #SAMPLE course_dict
        #{'Class Nbr:': '38664', 'Section #:': '581', 'Type:': 'LEC', 'Campus:': 'CE', 'Meets:': 'Meets online', 
        # 'Instructor:': 'D. Shaulis', 'Status:': 'Open', 'Dates:': '01-21 to 05-01'}
        #
        #{'Class Nbr:': '23529', 'Section #:': '005', 'Type:': 'LEC', 'Campus:': 'Main', 'Meets:': 'MTWF 1-1:50p',
        #  'Instructor:': 'Hallowell/Lotfi', 'Status:': 'Open', 'Dates:': '01-13 to 04-30'}

        #loop through course array add time and change meets format
        for course in course_array:
            #split on meets, you get days and the time
            #split on - to get times
            #append last letter of split string to first part
            #now have start and end time
            meets = course['Meets:'].split()
            meet_days= meets[0]
            meet_time =meets[1].split("-")

            #splits date to be used in date time later
            dates = course['Dates:'].split()

            #online do not have to parse time
            if(meet_time[0]=='online'):
                meet_start='online'
                meet_end='online'
                #add start/end time to course dictionary
                course['start_time']="online"
                course['end_time']="online"
            #parse time
            else:
                course['Meets:']=meet_days
                meet_start = meet_time[0]
                meet_end = meet_time[1]
                #if start time is only one number add 0 before and colon and zeroes after
                if(len(meet_start)<2):
                    am_pm= meet_end[-1]
                    meet_start= '0'+meet_start+':00'+am_pm
                #if start time has 2 digits just add colon and zeroes
                elif(len(meet_start)<3):
                    am_pm= meet_end[-1]
                    meet_start= meet_start+':00'+am_pm
                #just add am/pm to start time
                else:
                    if(meet_start[-1]=='a' or meet_start[-1]=='p'):
                        meet_start=meet_start
                    else:
                        am_pm= meet_end[-1]
                        meet_start= meet_start+am_pm

                #convert time to datetime object
                #start_time = parser.parse(dates[0]+" "+meet_start)
                #end_time = parser.parse(dates[2]+" "+meet_end)

                #add start/end time to course dictionary
                course['start_time']=meet_start
                course['end_time']=meet_end
                
        course_list.append(course_array)


driver.close()



#HAVE CLASS DATA
#
#
#
#
#BRAINSTORM
#first class selection determined by scarcity, display options for least dependent class then 
#do this over and over again.
class_file= open("test.txt", "w")

for course in course_list:

    for index,option in enumerate(course):
        if(index == 0):
            class_string= '['+str(option)
            class_string= class_string+',\n' 
        elif(index==(len(course)-1)):
            class_string= str(option)
            class_string= class_string+'\n' 
        else:

            class_string = str(option)
            class_string= class_string+',\n'        
        class_file.write(class_string)
    class_file.write('],\n')
    



class_file.close()
    
    


print("executed normally")







