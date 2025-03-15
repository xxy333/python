import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="appdb",
    user="postgres",
    password="5HnJc1XNYIdFUEZBXpJ4",
    host="localhost",
    port="5432"  # Default PostgreSQL port
)

# Create a cursor to perform database operations
cursor = conn.cursor()

# Execute an SQL query
cursor.execute("SELECT * FROM appdb.app_db_scheme.app_db;")

# Fetch results
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
