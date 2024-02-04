#include <stdio.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int clientSocket;
    char buffer[1024];
    struct sockaddr_in serverAddr;

    // Create socket
    clientSocket = socket(AF_INET, SOCK_STREAM, 0);

    // Set up server address
    serverAddr.sin_family = AF_INET;
    serverAddr.sin_port = htons(8080);
    serverAddr.sin_addr.s_addr = inet_addr("127.0.0.1");

    // Connect to server
    connect(clientSocket, (struct sockaddr *)&serverAddr, sizeof(serverAddr));

    // Send data to server
    send(clientSocket, "Hello Server!", sizeof("Hello Server!"), 0);

    // Receive data from server
    recv(clientSocket, buffer, sizeof(buffer), 0);
    printf("Server response: %s\n", buffer);

    // Close socket
    close(clientSocket);

    return 0;
}