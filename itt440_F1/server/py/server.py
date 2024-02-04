import socket
from datetime import datetime
import mysql.connector

# MySQL Database Configuration
db_config = {
    'host': 'db',  # Update to match the MySQL container name
    'user': 'root',
    'password': 'itt440',  # Update with the MySQL root password
    'database': 'mydatabase',
}

# Function to update the database
def update_database(user, points):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Update the database table
        query = f"INSERT INTO mytable (user, points, datetime_stamp) VALUES ('{user}', {points}, NOW()) ON DUPLICATE KEY UPDATE points={points}, datetime_stamp=NOW();"
        cursor.execute(query)

        connection.commit()
        print(f"Database updated for user {user} with {points} points at {datetime.now()}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        cursor.close()
        connection.close()

# TCP Server Configuration
host = '0.0.0.0'
port = 5000  # Update to match the port specified

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print(f"Python Server listening on port {port}...")

while True:
    # Wait for a connection
    client_socket, client_addr = server_socket.accept()
    print(f"Connection from {client_addr}")

    # Receive data from the client
    data = client_socket.recv(1024).decode('utf-8')

    if data:
        # Split received data into user and points
        user, points = data.split(',')
        points = int(points)

        # Update the database
        update_database(user, points)

    # Close the connection with the client
    client_socket.close()
