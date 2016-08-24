__author__ = 'Reid'

import psycopg2, csv


def load_course_database(db_name, csv_filename):
    # NOTE: before running this program, you must create the database named below from
    # the command-line (i.e. outside of Python or psql).
    # E.g. for the values of the constants below, you'd type:
    #     createdb -U postgres mydb1
    # and give the password: wombat

    PG_USER = "postgres"
    PG_USER_PASS = "password"
    PG_DATABASE = db_name
    PG_HOST_INFO = ""  # use "" for OS X or Windows

    # Connect to an existing database
    conn = psycopg2.connect("dbname=" + PG_DATABASE + " user=" + PG_USER + " password=" + PG_USER_PASS + PG_HOST_INFO)
    print("** Connected to database.")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table, but first removes it if it's there already
    cur.execute("DROP TABLE IF EXISTS coursedata;")
    cur.execute("CREATE TABLE coursedata (deptID text, courseNum int, semester int, meetingType text, seatsTaken int, seatsOffered int, instructor text);")

    with open(csv_filename, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cur.execute(
                "INSERT INTO coursedata (deptid, coursenum, semester, meetingtype, seatstaken, seatsoffered, instructor) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    # Pass data to fill a query placeholders and let Psycopg perform
    # the correct conversion (no more SQL injections!)
    print("** Executed SQL INSERT into database.")

    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM coursedata;")
    print("** Output from SQL SELECT: ", cur.fetchone())
    print("** Output from SQL SELECT: ", cur.fetchone())


    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()
    print("** Closed connection and database.  Bye!.")
    return 0

def main():
    load_course_database("mydatabase","seas-courses-5years.csv")

if __name__ == "__main__":
    main()
