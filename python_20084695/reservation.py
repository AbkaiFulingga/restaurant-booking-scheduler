import os
import datetime

reservation_file = 'reservation_20084695.txt'
SESSIONS = {
    1: '12:00 pm - 02:00 pm',
    2: '02:00 pm - 04:00 pm',
    3: '06:00 pm - 08:00 pm',
    4: '08:00 pm - 10:00 pm'
}
max_reservations_per_session = 8
max_group_size = 4
min_advance_days = 5


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def validate_phone_number(phone_number):
    if len(phone_number) != 10 or not phone_number.startswith('0') or not phone_number.isdigit():
        return False
    return True


def validate_email(email):
    if '@' not in email or '.' not in email or email.count('@') > 1 or email.count('.') < 1:
        return False
    return True


def get_reserved_sessions(reservation_date):
    reserved_sessions = []
    if os.path.exists(reservation_file):
        with open(reservation_file, 'r') as file:
            reservations = file.readlines()
        for reservation in reservations:
            if reservation_date in reservation:
                session = int(reservation.split('\\')[2].strip().split()[1])
                reserved_sessions.append(session)
    return reserved_sessions


def count_reserved_sessions(session):
    count = 0
    if os.path.exists(reservation_file):
        with open(reservation_file, 'r') as file:
            reservations = file.readlines()
        for reservation in reservations:
            if str(session) in reservation:
                count += 1
    return count


def check_date_format(date_string):
    try:
        day, month, year = map(int, date_string.split("-"))
        if len(str(year)) != 4 or not (1 <= month <= 12) or not (1 <= day <= 31):
            raise ValueError
    except (ValueError, IndexError):
        print("Error: Invalid date format. Please use 'dd-mm-yyyy' format.")
        return False
    return True


def make_reservation():
    clear_screen()
    print("Welcome to the Charming Thyme Trattoria!")
    while True:
        name = input("Please enter your name: ")
        if name.replace(" ", "").isalpha():
            name = name.strip().capitalize()
            break
        else:
            print("Invalid input. Please enter a valid name.")
    while True:
        group_size = input("How many people are in your entourage?: ")
        if group_size.isdigit() and int(group_size) > 0:
            group_size = int(group_size)
            break
        else:
            print("Invalid input. Please enter a positive number.")

    if group_size > max_group_size:
        clear_screen()
        print("Sorry, we can only accommodate groups of up to", max_group_size, "people.")
        return

    session = int(input("Select a session (1-4):\n"
                        "1. 12:00 pm - 02:00 pm\n"
                        "2. 02:00 pm - 04:00 pm\n"
                        "3. 06:00 pm - 08:00 pm\n"
                        "4. 08:00 pm - 10:00 pm\n"))
    while session not in range(1, 5):
        print("Invalid input. Please select a session between 1 and 4.")
        session = int(input("Select a session (1-4):\n"
                            "1. 12:00 pm - 02:00 pm\n"
                            "2. 02:00 pm - 04:00 pm\n"
                            "3. 06:00 pm - 08:00 pm\n"
                            "4. 08:00 pm - 10:00 pm\n"))

        phone_number = input("Enter your phone number (10 digits starting with 0): ")
        while not validate_phone_number(phone_number):
            print("Invalid phone number format. Please enter a 10-digit number starting with 0.")
            phone_number = input("Enter your phone number (10 digits starting with 0): ")

        email = input("Enter your email address: ")
        while not validate_email(email):
            print("Invalid email format. Please enter a valid email address.")
            email = input("Enter your email address in the format of (alex@imail.com): ")

    session_time = SESSIONS[session]
    reservation_date = datetime.datetime.now() + datetime.timedelta(days=min_advance_days)
    reservation_date_formatted = reservation_date.strftime('%Y-%m-%d')

    while True:
        clear_screen()
        desired_date_str = input("Enter your desired reservation date in the format (dd-mm-yyyy): ")
        try:
            desired_date = datetime.datetime.strptime(desired_date_str, '%d-%m-%Y')
            if desired_date > reservation_date:
                break
            else:
                print("Reservations must be made at least", min_advance_days, "days in advance.")
        except ValueError:
            print("Invalid date format. Please enter the date in the format dd-mm-yyyy.")

    reserved_sessions = get_reserved_sessions(reservation_date_formatted)
    with open(reservation_file, 'r') as file:
        reservations = file.readlines()

    count = 1
    for reservation in reservations:
        components = reservation.split(" \\ ")
        if len(components) >= 6:
            if (
                    (components[4].split(": ")[1].strip()) == desired_date_str
                    and components[3].split(": ")[1].strip() == session_time ):

                count += 1

    if count <= max_reservations_per_session:
        reservation = f"{name} \\ {group_size} pax \\ Session: {session} \\ Time: {session_time} \\ Date: {desired_date_str} \\ Phone Number: {phone_number} \\ Email: {email}\n"
        with open(reservation_file, 'a') as file:
            file.write(reservation)
        clear_screen()
        print("Reservation successfully made!")
    else:
        print("Session is fully booked, please choose another date or another session")


def cancel_reservation():   # change here
    clear_screen()
    print("Cancel a Reservation")
    name = input("Enter your name: ")

    # Read all reservations from the file
    with open(reservation_file, 'r') as file:
        reservations = file.readlines()
    count1 = 1
    # Find matching reservations
    matching_reservations = []
    for index, reservation in enumerate(reservations, start=1):
        if name.strip().lower() == reservation.split("\\")[0].strip().lower():
            matching_reservations.append((count1, reservation))
            count1 += 1

    if not matching_reservations:
        print("No matching reservations found.")
        return

    # Function to print the updated matching reservations with refreshed numbering
    def print_matching_reservations():
        print("Matching Reservations:")
        for index, reservation in enumerate(matching_reservations, start=1):
            print(f"{index}. {reservation[1].strip()}")

    print_matching_reservations()

    # Prompt for reservation removal
    while True:
        choice = input("Enter the reservation number to cancel or 'done' to exit: ")
        if choice.lower() == 'done':
            break
        try:
            choice = int(choice)
            if 1 <= choice <= len(matching_reservations):
                removed_reservation = matching_reservations[choice - 1][1]
                reservations.remove(removed_reservation)
                print(removed_reservation)
                print("Reservation canceled successfully.")
                matching_reservations.pop(choice - 1)
                print_matching_reservations()  # Print the updated list after cancellation
            else:
                print("Invalid reservation number. Please try again.")
                print_matching_reservations()  # Show the list again after an invalid input
        except ValueError:
            print("Invalid input. Please enter a valid reservation number or 'done'.")

    # Write the updated list of reservations back to the file
    with open(reservation_file, 'w') as file:
        file.writelines(reservations)


def update_field(field_value, field_name):
    while True:
        new_value = input(f"Enter new {field_name} (or press Enter to keep the same): ")
        if new_value:
            if field_name == "name" and (not new_value.replace(" ", "").isalpha()):  # updated here
                print(f"Invalid {field_name}. Please enter alphabets only.")
            elif field_name == "group size" and (not new_value.isdigit() or int(new_value) > max_group_size):
                print(f"Invalid {field_name}. Please enter a positive number up to {max_group_size}.")
            elif field_name == "session" and (not new_value.isdigit() or int(new_value) not in range(1, 5)):
                print("Sessions:")
                print("1: '12:00 pm - 02:00 pm'")
                print("2: '02:00 pm - 04:00 pm'")
                print("3: '06:00 pm - 08:00 pm'")
                print("4: '08:00 pm - 10:00 pm'")
                print(f"Invalid Session. Please enter a session number between 1 and 4.")
            elif field_name == "date":
                if not new_value:
                    return field_value
                if not check_date_format(new_value):
                    continue
                try:
                    new_date = datetime.datetime.strptime(new_value, "%d-%m-%Y")
                    if new_date < datetime.datetime.now() + datetime.timedelta(days=min_advance_days):
                        print(f"Reservations must be made at least {min_advance_days} days in advance.")
                    else:
                        return new_date.strftime("%d-%m-%Y")
                except ValueError:
                    print("Invalid date. Please enter a valid date in the format dd-mm-yyyy.")
                    continue

            elif field_name == "phone number" and (not new_value.startswith("0") or len(new_value) != 10 or not new_value.isdigit()):
                print(f"Invalid {field_name}. Please enter a 10-digit number starting with 0.")
            elif field_name == "email" and (not "@" in new_value or not ".com" in new_value):
                print(f"Invalid {field_name}. Please enter a valid email address.")
            else:
                return new_value.capitalize()
        else:
            return field_value


def update_fields(reservation):
    updated_name = update_field(reservation.split("\\")[0].strip(), "name")
    updated_group_size = update_field(reservation.split("\\")[1].strip().split()[0], "group size")
    updated_session = update_field(reservation.split("\\")[2].strip().split(":")[1].strip(), "session")
    updated_date = update_field(reservation.split("\\")[4].strip().split(":")[1].strip(), "date")
    updated_phone_number = update_field(reservation.split("\\")[5].strip().split(":")[1].strip(), "phone number")
    updated_email = update_field(reservation.split("\\")[6].strip().split(":")[1].strip(), "email")

    updated_reservation = f"{updated_name} \\ {updated_group_size} pax \\ Session: {updated_session} \\ Time: {SESSIONS[int(updated_session)]} \\ Date: {updated_date} \\ Phone Number: {updated_phone_number} \\ Email: {updated_email}\n"
    return updated_reservation


def update_reservation():
    clear_screen()
    print("Update/Edit Reservation(s)")
    while True:
        name = input("Please enter the name of the initial reservation: ")
        if name.strip().replace(" ", "").isalpha():  # Updated here
            name = name.strip().capitalize()
            break
        else:
            print("Invalid input, please enter a name containing only alphabets.")

    with open(reservation_file, 'r') as file:
        reservations = file.readlines()

    matching_reservations = []
    for index, reservation in enumerate(reservations, start=1):
        if name.lower() == reservation.split("\\")[0].strip().lower():
            matching_reservations.append((index, reservation))  # Store both the index and the reservation

    if not matching_reservations:
        print("No matching reservations found.")
        return

    print("Matching Reservations:")
    for index, reservation in enumerate(matching_reservations, start=1):
        print(f"{index}. {reservation[1].strip()}")

    while True:
        choice = input("Enter the number of the reservation to update: ")
        try:
            choice = int(choice)
            if 1 <= choice <= len(matching_reservations):
                selected_reservation = matching_reservations[choice - 1][1]
                updated_reservation = update_fields(selected_reservation)
                index = matching_reservations[choice - 1][0] - 1  # Get the original index
                reservations[index] = updated_reservation
                print("Reservation updated successfully.")
                break
            else:
                print("Invalid reservation number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid reservation number or 'done'.")

    # Write updated reservations to the file
    with open(reservation_file, 'w') as file:
        file.writelines(reservations)

