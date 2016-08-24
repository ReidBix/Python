__author__ = 'Reid'

import psycopg2, csv


def load_course_database(db_name):
    # NOTE: before running this program, you must create the database named below from
    # the command-line (i.e. outside of Python or psql).
    # E.g. for the values of the constants below, you'd type:
    #     createdb -U postgres mydb1
    # and give the password: wombat

    PG_USER = "postgres"
    PG_USER_PASS = "password"
    PG_DATABASE = db_name
    PG_HOST_INFO = ""  # use "" for OS X or Windows

    studentDict = {}

    # Connect to an existing database
    conn = psycopg2.connect("dbname=" + PG_DATABASE + " user=" + PG_USER + " password=" + PG_USER_PASS + PG_HOST_INFO)
    print("** Connected to database.")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM coursedata;")
    while(True):
        i = cur.fetchone()
        if i == None:
            break
        teacher = i[6]
        studentNum = int(i[4])
        if teacher in studentDict:
            studentDict[teacher] = studentDict[teacher] + studentNum
        else:
            studentDict[teacher] = studentNum
    print(studentDict)

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()
    print("** Closed connection and database.  Bye!.")
    return 0

def instructor_numbers(db_name, dept_id):
    # NOTE: before running this program, you must create the database named below from
    # the command-line (i.e. outside of Python or psql).
    # E.g. for the values of the constants below, you'd type:
    #     createdb -U postgres mydb1
    # and give the password: wombat

    PG_USER = "postgres"
    PG_USER_PASS = "password"
    PG_DATABASE = db_name
    PG_HOST_INFO = ""  # use "" for OS X or Windows

    studentDict = {}

    # Connect to an existing database
    conn = psycopg2.connect("dbname=" + PG_DATABASE + " user=" + PG_USER + " password=" + PG_USER_PASS + PG_HOST_INFO)
    print("** Connected to database.")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Query the database and obtain data as Python objects
    cur.execute("SELECT * FROM coursedata;")
    while(True):
        i = cur.fetchone()
        if i == None:
            break
        teacher = i[6]
        studentNum = int(i[4])
        id = i[0]
        if id != dept_id:
            pass
        else:
            if teacher in studentDict:
                studentDict[teacher] = studentDict[teacher] + studentNum
            else:
                studentDict[teacher] = studentNum
    print(studentDict)

    # Make the changes to the database persistent
    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()
    print("** Closed connection and database.  Bye!.")
    return 0


def main():
    load_course_database("mydatabase")
    instructor_numbers("mydatabase","CE")

if __name__ == "__main__":
    main()
