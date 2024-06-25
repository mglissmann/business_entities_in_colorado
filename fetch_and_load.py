import requests
import sqlite3

# Define the API endpoint URL
api_url = "https://data.colorado.gov/resource/4ykn-tg5h.json"
batch_size = 1000  # Number of records per batch
offset = 0  # Starting point

# Connect to SQLite database (or create it)
conn = sqlite3.connect('data_colorado.db')
cursor = conn.cursor()

# Fetch one record to determine the structure of the data
response = requests.get(api_url, params={'$limit': 1})
if response.status_code == 200:
    sample_data = response.json()
    if sample_data:
        columns = sample_data[0].keys()
        # Create table based on the keys in the data
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS data (
            {', '.join([f'{col} TEXT' for col in columns])}
        )
        ''')
        conn.commit()
else:
    print(f"Failed to retrieve data: {response.status_code}")
    exit()

while True:
    # Fetch a batch of data
    params = {
        '$limit': batch_size,
        '$offset': offset
    }
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        
        if not data:
            # No more data to fetch
            break

        # Prepare insert statement
        placeholders = ', '.join(['?'] * len(columns))
        insert_statement = f'''
        INSERT OR IGNORE INTO data ({', '.join(columns)})
        VALUES ({placeholders})
        '''
        
        # Process and insert data into the database
        for item in data:
            values = tuple(item.get(col) for col in columns)
            cursor.execute(insert_statement, values)
        
        # Commit changes to the database
        conn.commit()
        
        # Increment offset for the next batch
        offset += batch_size
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        break

# Close the database connection
conn.close()
