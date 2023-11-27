import psycopg2
from dotenv import load_dotenv
import os

# Path to the directory containing the .env file
# env_file_path = r'dirpathWhere.envIs present'

# Load environment variables from the specified .env file
# load_dotenv(dotenv_path=os.path.join(env_file_path, '.env'))

# Load environment variables from the .env file
""" i have setup working directory as HospitalMngtSystem so it will load from that"""
load_dotenv()

# Access the password using the PASSWORD key
password = os.getenv("PASSWORD")
dbName = os.getenv("DATABASE")

# Use the password as needed
print("Password:", password)
print("Password:", dbName)

def getCursor():
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            database=dbName,
            host="localhost",
            user="postgres",
            password=password,
            port="5432"
        )

        # Create a cursor object to interact with the database
        cursor = conn.cursor()
    except Exception as e:
        # Print any exceptions that occur
                 print("Error In creating connection :", e)

    # finally:
    #     # Close the cursor and connection in the finally block to ensure it happens regardless of success or failure
    #     if cursor:
    #         cursor.close()
    #     if conn:
    #         conn.close()
    return [cursor , conn] # always close the cursor when you call this function

    ''' FOR Reference '''

    # Define the table creation SQL query
    # table_query = '''
    #     CREATE TABLE IF NOT EXISTS user_data (
    #         id SERIAL PRIMARY KEY,
    #         name VARCHAR(30) NOT NULL,
    #         password VARCHAR(30) NOT NULL
    #     );
    # '''

    # # Execute the table creation query
    # cursor.execute(table_query)
    #
    # # Commit the changes to the database
    # conn.commit()
    #
    # print("SUCCESSFULLY CREATED")
    #
    # # Fetch and print the list of tables in the current database
    # cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    # tables = cursor.fetchall()
    # print("Tables: ", tables)


if __name__ == "__main__":
    getCursor()

# print("end")
