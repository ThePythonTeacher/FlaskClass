import MySQLdb

# Configure MySQL
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_DB = 'bala'

# Establish a connection to the MySQL database
def connect_to_db():
    return MySQLdb.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        passwd=MYSQL_PASSWORD,
        db=MYSQL_DB
    )

def login(name, age):
    # Create a connection and a cursor
    db_connection = connect_to_db()
    cursor = db_connection.cursor()

    try:
        # Execute the query
        cursor.execute('''INSERT INTO info_table (name, age) VALUES (%s, %s)''', (name, age))
        db_connection.commit()
        cursor.close()
        db_connection.close()
        return "Done!!"
    except Exception as e:
        print(e)

    finally:

        print("calling final functon ")



def gte_the_details():
    # Create a connection and a cursor
    db_connection = connect_to_db()
    cursor = db_connection.cursor()

    try:
        # Execute the query
        cursor.execute('''select * from info_table''')
        db_connection.commit()

        myresult = cursor.fetchall()

        # Print each row
        cursor.close()
        db_connection.close()
        return myresult
    except Exception as e:
        print(e)

    finally:

        print("calling final functon ")

def search_name(name):
    # Create a connection and a cursor
    db_connection = connect_to_db()
    cursor = db_connection.cursor()

    try:
        # Execute the query
        # cursor.execute('''select * from info_table where name=%s''', (name))

        # cursor.execute('''SELECT * FROM info_table WHERE name=%s''', (name,))
        cursor.execute('''SELECT * FROM info_table WHERE name=%s''', (name,))
        result = cursor.fetchall()

        for i in result:
            print(i)

            db_connection.commit()
        cursor.close()
        db_connection.close()
        return result
    except Exception as e:
        print(e)

    finally:

        print("calling final functon ")


# Example usage
if __name__ == "__main__":
    # result = login("Bala", 25)
    # result = gte_the_details()

    result = search_name("Bala")
    print(result)
