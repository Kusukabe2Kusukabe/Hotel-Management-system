# Initialize hotel details
hotel_name = "Grand Hotel"
total_rooms = 5
booked_rooms = {}

while True:
    print("\nWelcome to", hotel_name)
    print("1. Check Availability")
    print("2. Book Room")
    print("3. Checkout Room")
    print("4. View Booked Rooms")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        available_rooms = total_rooms - len(booked_rooms)
        print(f"Available Rooms: {available_rooms}")

    elif choice == '2':
        guest_name = input("Enter guest name: ")
        if len(booked_rooms) < total_rooms:
            room_number = len(booked_rooms) + 1
            booked_rooms[room_number] = guest_name
            print(f"Room {room_number} booked for {guest_name}.")
        else:
            print("No rooms available.")

    elif choice == '3':
        room_number = int(input("Enter room number to checkout: "))
        if room_number in booked_rooms:
            guest_name = booked_rooms.pop(room_number)
            print(f"{guest_name} has checked out from room {room_number}.")
        else:
            print("Room not found.")

    elif choice == '4':
        if not booked_rooms:
            print("No rooms are currently booked.")
        else:
            print("Booked Rooms:")
            for room_number, guest_name in booked_rooms.items():
                print(f"Room {room_number}: {guest_name}")

    elif choice == '5':
        print("Exiting the system.")
        break

    else:
        print("Invalid option. Please try again.")
