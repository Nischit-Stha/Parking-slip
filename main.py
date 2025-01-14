import database
import entry
import price

def main():
    database.database_initializer()  
    response = 'y'
    
    try:
        while response.lower() == 'y':
            user_name = input("Enter your name: ")
            phone_no = input("Enter your phone number: ") 
            vehicle_no = input("Enter the vehicle number: ")
            vehicle_type_shortcut = input("Press '2' for two-wheeler and '4' for four-wheeler: ")
            
            if vehicle_type_shortcut == '2':
                vehicle_type = 'Two wheeler'
            elif vehicle_type_shortcut == '4':
                vehicle_type = 'Four wheeler'
            else:
                print("Invalid input! Please try again.")
                continue
            
            entry.add_vehicle(user_name, phone_no, vehicle_no, vehicle_type)
            response = input("Do you want to continue (y/n): ")
    
    except Exception as e:
        print("There was an error:", e)

    checkout = input("Do you want to checkout? (Press 'y' for Yes and 'n' for No): ")
    try:
        if checkout.lower() == 'y':
            vehicle_no = input("Enter the vehicle number to checkout: ")
            price.checkout_vehicle(vehicle_no)
    except Exception as e:
        print("There was an error:", e)


if __name__ == "__main__": 
    main()







