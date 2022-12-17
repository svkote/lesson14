import sqlite3

with sqlite3.connect('netflix.db') as conn:
    cursor = conn.cursor()
    cursor.execute('')
