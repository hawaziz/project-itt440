import socket

def start_client():
    host = 'server_container_ip'  # Replace with the actual IP of the server container
    port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Implement your client logic here

    client_socket.close()

#if _name_ == "_main_":
    # start_client()