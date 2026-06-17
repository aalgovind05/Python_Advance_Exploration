import sqlite3

conn = sqlite3.connect('youtube_manager.db')

cursor= conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXITS videos(
               id INTEGER PRIMARY KEY
               name TEXT NOT NULL
               time TEXT NOT NULL
               )
 ''')

def main()
    pass

if __name__ == '__main__':
    main()