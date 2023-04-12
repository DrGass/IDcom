import json
import sqlite3

conn = sqlite3.connect("IDcom.db")

c = conn.cursor()

# c.execute(
#     """CREATE TABLE gallery (
#             Photo INTEGER,
#             Letter varchar(32)
#     )"""
# )


# c.execute("INSERT INTO gallery VALUES (1,'A')")
# c.execute("INSERT INTO gallery VALUES (2,'B')")
# c.execute("INSERT INTO gallery VALUES (3,'C')")

c.execute("SELECT * FROM gallery")

conn.commit()

rows = json.dumps(c.fetchall())
print(rows)

conn.close()
