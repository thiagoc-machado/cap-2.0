import sqlite3

def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE "user" (
            "id"	INTEGER NOT NULL UNIQUE,
            "username"	TEXT NOT NULL UNIQUE,
            "email"	TEXT NOT NULL UNIQUE,
            "password"	TEXT NOT NULL,
            PRIMARY KEY("id" AUTOINCREMENT)
        );
    ''')

#create_table()