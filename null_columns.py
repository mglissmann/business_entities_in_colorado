import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('business_entities.db')
cursor = conn.cursor()

# Fetch column names
cursor.execute("PRAGMA table_info(colorado);")
columns = [row[1] for row in cursor.fetchall()]

# Identify columns with more than 50% null values
threshold = 0.5
columns_to_keep = []

for column in columns:
    cursor.execute(f"SELECT COUNT(*) FROM colorado WHERE {column} IS NULL;")
    null_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM colorado;")
    total_count = cursor.fetchone()[0]
    
    if null_count / total_count < threshold:
        columns_to_keep.append(column)

print(f"Columns to keep: {columns_to_keep}")

conn.close()
