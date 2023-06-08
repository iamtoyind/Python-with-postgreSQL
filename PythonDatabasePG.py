import json
import psycopg2

hostname = "127.0.0.1"
db = "apache_age"
username = "postgres"
pwd = "Admin"
port_id = "5432"
conn = None
cur = None


def create_connection():
    conn = psycopg2.connect(database=db,
                            user=username,
                            password=pwd,
                            host=hostname,
                            port=port_id)
    print("Opened database successfully")
    return conn


def create_db_table(conn):
    cur = conn.cursor()
    # Dropping EMPLOYEE table if already exists.
    cur.execute("DROP TABLE IF EXISTS STAFF_RECORD")

    # Create table
    sql = """CREATE TABLE STAFF_RECORD(
        USER_ID SERIAL PRIMARY KEY,
        NAME CHAR(20) NOT NULL,
        AGE INT,
        PHONE CHAR(20)
        )"""
    cur.execute(sql)
    print("Table created successfully........")


def insert_data_into_db():
    try:
        conn = create_connection()
        cur = conn.cursor()
        create_db_table(conn)
        insert_query = """ INSERT INTO STAFF_RECORD (NAME,AGE,PHONE) VALUES (%s,%s,%s)"""
        records = [("Jenny", 34, "091128282"), ("Tom", 29,
                                                "1-800-123-1234"), ("John", 28, None)]

        for record in records:
            cur.execute(insert_query, record)
            print(f"Record for {record[0]}........ was created successfully")
        conn.commit()
        return get_result_in_json(cur)
    except (Exception, psycopg2.Error) as err:
        print("Failed to insert record into staff record table", err)
    finally:
        if conn is not None:
            cur.close()
            conn.close()
            print("Connection is closed")


def query_db(cur, query, args=()):
    cur.execute(query, args)
    result = [dict((cur.description[i][0], value)
                   for i, value in enumerate(row)) for row in cur.fetchall()]
    return result


def get_result_in_json(cur):
    query_result = query_db(cur, "SELECT * FROM public.staff_record")
    json_output = json.dumps(query_result)
    return json_output


if __name__ == "__main__":
    print(insert_data_into_db())
