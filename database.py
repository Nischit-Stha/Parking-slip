import sqlite3

def database_initializer():
    conn = sqlite3.connect("parking.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS parking(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            phone_no TEXT NOT NULL,
            vehicle_no TEXT NOT NULL,
            entry_time TEXT,
            exit_time TEXT,
            total_price INTEGER,
            vehicle_type VARCHAR
        )
        """
    )
    conn.commit()
    conn.close()



