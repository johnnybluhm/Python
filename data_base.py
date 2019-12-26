import psycopg2

try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "brianrocks",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "course_options")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT * from course_data WHERE start_time BETWEEN '12:00:00' AND '13:00:00' AND open_status='Open';")
    rows= cursor.fetchall()
    print(rows)


except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")