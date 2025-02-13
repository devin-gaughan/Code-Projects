import sqlite3

# Connect to SQLite database (or creates it if it doesn't exist)
conn = sqlite3.connect('feeds.db')
cursor = conn.cursor()

# Create Categories table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Categories (
        id INTEGER PRIMARY KEY AUTO INCREMENT,
        name TEXT NOT NULL UNIQUE
)
''')

# Create Feeds table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Feeds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT NOT NULL UNIQUE,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES Categories(id)
)
''')

# Create Articles table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Articles (
    id INTEGER PRIMARY AUTOINCREMENT,
    feed-id INTEGER,
    title TEXT NOT NULL,
    summary TEXT,
    read_status INTEGER DEFAULT 0,  -- 0 for unread, 1 for read
    FOREIGN KEY (feed_id) REFERENCES Feeds(id)
)
''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Database and tables created successfully.")