import sqlite3
import datetime
from farestorage import fare_database

def checkout_vehicle(vehicle_number, hourly_rate_two_wheeler=20, hourly_rate_four_wheeler=50) :
    conn= sqlite3.connect('parking.db')
    cursor = conn.cursor()
    additional_fare_two_wheeler=5
    additional_fare_four_wheeler=10

    cursor.execute(
        "SELECT id, entry_time, vehicle_type FROM parking Where vehicle_no =? ",
        (vehicle_number,)

    )
    row =cursor.fetchone()
    if row:
        slip_id, entry_time_str, vehicle_type= row
        entry_time = datetime.datetime.fromisoformat(entry_time_str)
        exit_time = datetime.datetime.now()

        duration =(exit_time - exit_time).total_seconds()/3600

        if vehicle_type =='Two wheeler':
            price_initial = round(duration * hourly_rate_two_wheeler, 2)
            fare=round(additional_fare_two_wheeler*duration,2)
            price= price_initial+fare
        else:
            price_initial = round(duration * hourly_rate_four_wheeler, 2)
            fare=round(additional_fare_four_wheeler*duration,2)
            price= price_initial+fare

        cursor.execute(
            "UPDATE parking SET exit_time=?, total_price=? WHERE id =?",
            (exit_time, price, slip_id)
        )
        conn.commit()
        conn.close()

        slip = f"""
        Vehicle Exited
        ---------------------------
        ID            : {slip_id}
        Vehicle No.   : {vehicle_number}
        Entry Time    : {entry_time}
        Exit Time     : {exit_time}
        Duration      : {duration:.2f} hours
        Addition Fare : {fare:.2f}NPR
        Price         : {price:.2f} NPR
        ---------------------------
        """
        with open('parking_slip_exit.txt','a') as file:
         file.write(slip+"\n")
        print("Vehicle checked out successfully.")
        print(slip)
        fare_database(slip_id,price,fare)
    else:
       print("Vehicle not found or already checked out.")
