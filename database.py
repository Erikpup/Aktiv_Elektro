import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS objects(
   object_id INT PRIMARY KEY,
   name TEXT);
""")
user = (2, 'test')
cur.execute("INSERT INTO objects VALUES(?, ?);", user)
conn.commit()
cur.execute("SELECT * FROM objects")
rows = cur.fetchall()
print(rows)
conn.close()
