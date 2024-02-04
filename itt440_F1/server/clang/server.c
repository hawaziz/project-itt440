#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <mysql/mysql.h>

#define DB_HOST "localhost"
#define DB_USER "root"
#define DB_PASSWORD "itt440"
#define DB_NAME "Sir"

MYSQL *connection;

// Function to connect to the MySQL database
int connect_to_database() {
    connection = mysql_init(NULL);
    if (connection == NULL) {
        fprintf(stderr, "Error initializing MySQL connection: %s\n", mysql_error(connection));
        return 0;
    }

    if (mysql_real_connect(connection, DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, 0, NULL, 0) == NULL) {
        fprintf(stderr, "Error connecting to MySQL server: %s\n", mysql_error(connection));
        mysql_close(connection);
        return 0;
    }

    printf("Connected to MySQL database\n");
    return 1;
}

// Function to add or replace a record in the database
int add_or_replace_record() {
    const char *query = "REPLACE INTO UserPoints (username, points) VALUES ('example_user', 100)";

    if (mysql_query(connection, query) != 0) {
        fprintf(stderr, "Error executing MySQL query: %s\n", mysql_error(connection));
        return 0;
    }

    printf("Record added/replaced successfully\n");
    return 1;
}

// Function to close the database connection
void close_connection() {
    if (connection != NULL) {
        mysql_close(connection);
        printf("MySQL connection closed\n");
    }
}

int main() {
    // Connect to the MySQL database
    if (!connect_to_database()) {
        exit(EXIT_FAILURE);
    }

    // Add or replace a record in the database
    if (!add_or_replace_record()) {
        close_connection();
        exit(EXIT_FAILURE);
    }

    // Close the database connection
    close_connection();

    return 0;
}
