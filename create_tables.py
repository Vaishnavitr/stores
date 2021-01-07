import sqlite3

connection = sqlite3.connect('data.db')  # establish connection
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"  # query
cursor.execute(create_table) #run

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"  # query
cursor.execute(create_table)


connection.commit()
connection.close()