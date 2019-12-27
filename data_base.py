import psycopg2
from psycopg2.extras import NamedTupleCursor
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
# data to plot
n_groups = 4
means_frank = (90, 55, 40, 65)
means_guido = (85, 62, 54, 20)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8

rects1 = plt.bar(index, means_frank, bar_width,
alpha=opacity,
color='b',
label='Frank')

rects2 = plt.bar(index + bar_width, means_guido, bar_width,
alpha=opacity,
color='g',
label='Guido')

plt.xlabel('Day')
plt.ylabel('Time')
plt.title('Schedule')
plt.xticks(index + bar_width, ('M', 'T', 'W', 'Th', 'F'))
plt.legend()

plt.tight_layout()
plt.show()
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "brianrocks",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "course_options")

    cursor = connection.cursor(cursor_factory=NamedTupleCursor)
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT * from course_data WHERE start_time BETWEEN '09:00:00' AND '15:00:00' AND open_status='Open' AND lec_type = 'LEC' AND course_name='CSCI 2400';")
    rows= cursor.fetchall()
    for row in rows:
        print(row.course_name)
        print(row.start_time)
    
    cursor.execute("SELECT * from course_data WHERE meet_days='online';")
    rows= cursor.fetchall()

    for row in rows:
        print(row.course_name)
        print(row.start_time)

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


