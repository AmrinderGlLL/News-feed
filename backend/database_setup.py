import sqlite3

def setup_database():
    conn = sqlite3.connect('news_feed.db')
    cursor = conn.cursor()

    # Table for saved articles
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS saved_articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL
        )
    ''')

    # Table for user preferences
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_preferences (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
