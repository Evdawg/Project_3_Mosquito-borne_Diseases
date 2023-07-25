import psycopg2

conn = psycopg2.connect(dbname="Project_3", user="Evan", password="defaultpw", host="localhost", port="5432")

cur = conn.cursor()
cur.execute('SELECT * FROM "WestNile-Case-Counts-by-County"')

items = cur.fetchall()

for row in items:
    print("pkey = ", row[0], )
    print("val = ", row[1], "\n")

cur.close()
conn.close()