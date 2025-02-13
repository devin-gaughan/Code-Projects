import sqlite3

class DBManager:
    def __init__(self, db_name='feeds.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        
    # Category Operations
    def add_category(self, name):
        try:
            self.cursor.execute("INSERT INTO Categories (name) VALUES (?)", (name,))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"Category '{name}' already exists.")
            
    def delete_category(self, category_id):
        self.cursor.execute("DELETE FROM Categories WHERE id = ?", (category_id,))
        self.conn.commit()
    
    def get_categories(self):
        self.cursor.execute("SELECT * FROM Categories")
        return self.cursor.fetchall()
    
    # FEED Operations
    def add_feed(self, url, category_id=None):
        try:
            self.cursor.execure("INSERT INTO Feeds (url, category_id) VALUES (?, ?)", (url, category_id))
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"Feed '{url}' already exists.")
            
    def delete_feed(self, feed_id):
        self.cursor.execute("DELETE FROM Feeds WHERE id = ?", (feed_id,))
        self.conn.commit()
        
    def get_feeds_by_category(self, category_id):
        self.cursor.execute("SELECT * FROM Feeds WHERE category_id = ?", (category_id,))
        return self.cursor.fetchall()
    
    # Article Operations
    def add_article(self, feed_id, titlem summary):
        self.cursor.execute(
            "INSERT INTO Articles (feed_id, title, summary) VALUES (?, ?, ?)",
            (feed_id, title, summary)
        )
        self.conn.commit()
    
    def mark_as_read(self, article_id):
        self.cursor.execute("UPDATE Articles SET read_status = 1 WHERE id = ?", (article_id,))
        self.conn.commit()