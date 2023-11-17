import sqlite3
conn = sqlite3.connect("student_info.db")
c = conn.cursor()
c.execute("UPDATE ")
c.execute("SELECT * FROM student ")
print(c.fetchall())
conn.commit()
conn.close()