import socket
import mysql.connector
from mysql.connector import Error

# Function to connect to the MySQL database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='Sir',
            user='root',
            password='itt440'
        )
        if connection.is_connected():
            print("Connected to the database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Create a cursor to execute SQL queries
def create_cursor(connection):
    if connection:
        return connection.cursor()
    else:
        return None

# Close the cursor and connection
def close_connection(cursor, connection):
    if cursor:
        cursor.close()
    if connection and connection.is_connected():
        connection.close()
        print("Connection to the database closed")

# Your server code
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 8080))
serverSocket.listen(5)

# Connect to the database
db_connection = connect_to_database()
cursor = create_cursor(db_connection)

while True:
    clientSocket, addr = serverSocket.accept()
    print("Connection from:", addr)

    message = clientSocket.recv(1024)
    print("Received from client:", message.decode())

    # Insert your database queries here using cursor.execute()

    # Insert a new user
insert_query = "INSERT INTO UserPoints (username, points) VALUES (abu, 45)"
user_data = ("example_user", 100)
cursor.execute(insert_query, user_data)
db_connection.commit()
print("User added successfully")


    # Retrieve points for a specific user
select_query = "SELECT points FROM UserPoints WHERE username = %s"
username_to_select = "example_user"
cursor.execute(select_query, (username_to_select,))
result = cursor.fetchone()
if result:
    points = result[0]
    print(f"{username_to_select} has {points} points")
else:
    print(f"{username_to_select} not found")


    clientSocket.send("Hello Client!".encode())

    clientSocket.close()

# Close the database connection when the server is done
close_connection(cursor, db_connection)

