import sqlite3

try:
    conn = sqlite3.connect('baza_danych.db')
    c = conn.cursor()
    print("Baza danych został podlłączona")

    query = """
    CREATE TABLE IF NOT EXISTS developers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    salary REAL NOT NULL);
    """
    insert = """
    INSERT INTO developers (id,name,salary) VALUES (1,'Radek','10000');
    """
    # c.execute(query)
    # conn.commit()
    c.execute(insert)
    conn.commit()
except sqlite3.Error as e:
    print("Bład bazy danych", e)
finally:
    if conn:
        conn.close()
        print("Połączenie zostało zamknięte")
# Baza danych został podlłączona
# Połączenie zostało zamknięte
