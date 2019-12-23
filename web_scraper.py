from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from dateutil import parser
import pandas as pd
from datetime import datetime
from pprint import pprint



driver = webdriver.Chrome()
driver.implicitly_wait(10)

#opens browser


#hard code class values for now
course_list = []
course_sel = ['CSCI 2400', 'MATH 1150','ITAL 1020']

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

    #give ajax time to laod
    time.sleep(2)

    getNodes = 'var results =document.getElementsByClassName("result__code");\n'
    loop = 'for(var i=0;i<results.length;i++){\n'
    loop = loop+'var course = results[i];\n'+'if(course.innerHTML=="'+sel+'"){\n'
    loop= loop+'course.parentElement.parentElement.click();\n'+'break;\n'+'}\n'+'}'
    js = getNodes+loop

    #search classes for selection
    driver.execute_script(js)



    #give ajax time to load
    time.sleep(2)


    #gets table of course info for course
    table = driver.execute_script('var a = document.getElementsByClassName("course-sections")[0];\n return a;').get_attribute('outerHTML')


    time.sleep(2)

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
                am_pm= meet_end[-1]
                meet_start= meet_start+am_pm

            #convert time to datetime object
            start_time = parser.parse(dates[0]+" "+meet_start)
            end_time = parser.parse(dates[2]+" "+meet_end)

            #add start/end time to course dictionary
            course['start_time']=start_time
            course['end_time']=end_time
            
    course_list.append(course_array)


driver.close()
pprint(course_list)


#HAVE CLASS DATA
#
#
#
#


print("executed normally")







