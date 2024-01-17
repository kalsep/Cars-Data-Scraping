
import mysql.connector
def get_database_connection():
    # Replace these values with your MySQL server details
    host = "localhost"
    user = "root"
    password = "Pravin@1995"
    database = "cardekho"

    # Connect to MySQL
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        cursor = connection.cursor()
        return connection,cursor
    except mysql.connector.Error as error:
        return None