def display_reservations():  # this is my function and it is called
    with open("reservation_20084695.txt", "r") as file:  # this is to read the text files
        reservations = file.readlines()  # this is for the program to read the file
        if not reservations:
            print("No reservations found.") # simple if not statement in case the reservation file is empty
        else:
            print("All Reservations:")
            print("------------------------------------------------------------------------------------------------------------------------")
            print("{:<20s} {:<5s} {:<15s} {:<20s} {:<15s} {:<15s} {:<30s}".format("Name", "Pax", "Session", "Time", "Date", "Phone Number", "Email"))
            print("------------------------------------------------------------------------------------------------------------------------")

            for reservation in reservations:
                components = reservation.strip().split(" \\ ")  # the \ is what the program understands as a split
                if len(components) >= 7:  # this is just an initial check
                    name = components[0]  # as there are normally 7 variables in the print, 0 represents the name variable at position 0 starting from the left
                    pax = components[1]
                    session = "Session: " + components[2].split(": ")[1].strip()  # this is just formatting and making the code look cleaner
                    time = components[3].split(": ")[1].strip()
                    date = components[4].split(": ")[1].strip()
                    phone_number = components[5].split(": ")[1].strip()
                    email = components[6].split(": ")[1].strip()
                    print("{:<20s} {:<5s} {:<15s} {:<20s} {:<15s} {:<15s} {:<30s}".format(name, pax, session, time, date, phone_number, email))  # this is to make a somewhat presentable tabulation of reservations
            print("------------------------------------------------------------------------------------------------------------------------")


