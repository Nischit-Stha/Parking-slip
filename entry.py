import datetime 
import sqlite3

def add_vehicle(username, phone, vehicle_no, vehicle_type):
    conn = sqlite3.connect('parking.db')
    cursor = conn.cursor()

    entry_time = datetime.datetime.now()
    cursor.execute(
        "INSERT INTO parking(username, phone_no, vehicle_no, entry_time, vehicle_type) VALUES(?, ?, ?, ?, ?)",
        (username, phone, vehicle_no, entry_time, vehicle_type)
    )
    conn.commit()
    slip_id = cursor.lastrowid
    conn.close()

    slip = f""" 
    Parking Slip
    -----------------------------
    ID            : {slip_id}
    Username      : {username}
    Phone Number  : {phone}
    Vehicle No.   : {vehicle_no}
    Entry Time    : {entry_time}
    Vehicle Type  : {vehicle_type}
    -------------------------------
    """
    with open("parking_slip.txt", "a") as file:
        file.write(slip + "\n")

    print("Vehicle added successfully. Slip has been generated.")
    print(slip)
