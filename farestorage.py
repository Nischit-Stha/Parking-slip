import sqlite3
import faretable


def fare_database(id, total_price, fare_price):

    faretable.fare_table()

    conn=sqlite3.connect('parking.db')
    cursor=conn.cursor()

    cursor.execute(
        "INSERT INTO faretable (id, total_price, fare_price) VALUES (?, ?, ?, ?)",
        (id,total_price, fare_price)
    )
    conn.commit()
    conn.close()
    