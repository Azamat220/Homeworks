import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)

    return connection


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_student(conn, student):
    try:
        sql = '''INSERT INTO students 
        (full_name, mark, hobby, birth_date, is_married) 
        VALUES (?, ?, ?, ?, ?)
        '''
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_students(conn):
    try:
        sql = '''SELECT * FROM students'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_students_by_mark_limit(conn, limit):
    try:
        sql = '''SELECT * FROM students WHERE mark >= ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (limit,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def update_student(conn, student):
    try:
        sql = '''UPDATE students SET mark = ?, is_married = ?
        WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_student(conn, id):
    try:
        sql = '''DELETE FROM students WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


sql_create_students_table = '''
CREATE TABLE students (
id INTEGER PRIMARY KEY AUTOINCREMENT,
full_name VARCHAR(200) NOT NULL, 
mark DOUBLE(5, 2) NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
birth_date DATE NOT NULL,
is_married BOOLEAN DEFAULT FALSE
)
'''

connection = create_connection('hw.db')
if connection is not None:
    print('Connected successfully')
    create_table(connection, sql_create_students_table)
    insert_student(connection,
                   ('Turdaliev Iskhak', 99.88, 'Programming', '2000-09-12', True))
    insert_student(connection, ("Mark Daniels", 77.12, "Football", "1999-01-02", False))
    insert_student(connection, ("Alex Brilliant", 77.12, None, "1989-12-31", True))
    insert_student(connection, ("Diana Julls", 99.3, "Tennis", "2005-01-22", True))
    insert_student(connection, ("Michael Corse", 100.0, "Diving", "2001-09-17", True))
    insert_student(connection, ("Jack Moris", 50.2, "Fishing and cooking", "2001-07-12", True))
    insert_student(connection, ("Viola Manilson", 41.82, None, "1991-03-01", False))
    insert_student(connection, ("Joanna Moris", 100.0, "Painting and arts", "2004-04-13", False))
    insert_student(connection, ("Peter Parker", 32.0, "Travelling and bloging", "2002-11-28", False))
    insert_student(connection, ("Paula Parkerson", 77.09, None, "2001-11-28", True))
    insert_student(connection, ("George Newel", 93.0, "Photography", "1981-01-24", True))
    insert_student(connection, ("Miranda Alistoun", 87.55, "Playing computer games", "1997-12-22", False))
    insert_student(connection, ("Fiona Giordano", 66.12, "Driving fast", "1977-01-15", True))

    select_all_students(connection)

    select_students_by_mark_limit(connection, 50)
    update_student(connection, (76.1, True, 2))
    delete_student(connection, 2)
    select_all_students(connection)
    print('DONE')
    connection.close()
