import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname = "task_manager",
    user="postgres",
    password="Password4242"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM tasks")

rows = cursor.fetchall()

print(rows)

cursor.close()
conn.close()