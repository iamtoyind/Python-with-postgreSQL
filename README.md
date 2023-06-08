# Python-with-postgreSQL


This code snippet is a Python script that interacts with a PostgreSQL database using the psycopg2 library. It performs the following tasks:

Imports the necessary modules: json for JSON serialization and psycopg2 for connecting to and interacting with the PostgreSQL database.

Defines the database connection parameters: hostname, db, username, pwd, and port_id.

Defines the conn and cur variables to store the connection and cursor objects, respectively. These variables will be used throughout the script.

Defines a function named create_connection() that establishes a connection to the PostgreSQL database using the provided connection parameters. It returns the connection object.

Defines a function named create_db_table(conn) that creates a table named STAFF_RECORD in the database. If the table already exists, it is dropped first. The table has four columns: USER_ID, NAME, AGE, and PHONE.

Defines a function named insert_data_into_db() that inserts records into the STAFF_RECORD table. It creates the table if it doesn't exist. The function uses a list of records to be inserted, and each record is a tuple containing the values for NAME, AGE, and PHONE columns.

Inside the insert_data_into_db() function, a loop iterates over the records and executes an insert query using the cur.execute() method. The function also prints a success message for each record inserted.

After inserting the records, the function commits the changes to the database. Then, it calls the get_result_in_json() function to retrieve the contents of the STAFF_RECORD table as a JSON string.

The script defines a function named query_db(cur, query, args=()) that executes a SQL query with optional parameters. It fetches the result using cur.fetchall() and transforms it into a list of dictionaries, where each dictionary represents a row from the query result.

The get_result_in_json(cur) function calls query_db() to retrieve the contents of the STAFF_RECORD table and converts the result into a JSON string using the json.dumps() function.

Finally, the script checks if it is being run directly (not imported) and calls the insert_data_into_db() function. The result is printed as output.

Overall, this code sets up a connection to a PostgreSQL database, creates a table, inserts records into the table, retrieves the data in JSON format, and prints the JSON output.
