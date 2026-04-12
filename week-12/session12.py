import sqlite3

conn = sqlite3.connect("northwind.db")
cursor = conn.cursor()

# show tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables:")
for i, t in enumerate(tables):
    print(i + 1, "-", t[0])

# choose table
choice = int(input("Select table number: "))
table_name = tables[choice - 1][0]

# show records
cursor.execute(f"SELECT * FROM {table_name}")
rows = cursor.fetchall()

print("\nData:")
for row in rows:
    print(row)

conn.close()