

#   IMport the loibrary  psycopg2
# connect database   # host, dbname , username, password and ports

# Create cursor object

# insert into db. table values ()

#connection.commit()

#close cursor
#close connection


import psycopg2

'''
writing a function to insert data into database
'''
def insert_data_into_db():
    database_name = "postgres"
    user_name = "postgres"
    host = "localhost"
    port = 5433
    password = 'root'

    connection = psycopg2.connect(dbname = database_name, user = user_name,
                                  password = password, host=host, port=port
                                )

    cursor = connection.cursor()



    #query to inser

    query_to_insert = " insert into public.user (username, email) values (%s, %s);"
    data_to_insert = ('kannan', 'kannan@gmail.com')


    cursor.execute(query_to_insert, data_to_insert)

    connection.commit()

    cursor.close()
    connection.close()



insert_data_into_db()



