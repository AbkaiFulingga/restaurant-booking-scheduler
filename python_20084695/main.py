import os
import display_reservations
import reservation
import menu
 # imports modules which contain functions
reservation_file = 'reservation_20084695.txt'
staff_id = "YongYokeLeng"  # we love our programming lecturer
staff_pw = "Iloveprogrammingprinciples" # and our subject too <3


def clear_screen():  # this is just another function to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')  # if your os = nt (windows), it will apply cls, if its linux or macos, cls will become clear


while True:  # while loop is used here for the menu
    clear_screen()
    print("\n1. Make a reservation")  # this prints out in the form of a new line with \n, the menu and its options
    print("2. Cancel a reservation")
    print("3. Update a reservation")
    print("4. Select a random dish from the menu")
    print("5. Display all reservations")
    print("6. Exit")
    choice = input("Please enter your choice (1-6): ")  # the user will input thier choice and if they dont enter a number between 1 and 6, an error code will be output, as such as anything else as seen below

    if choice == '1':
        clear_screen()
        confirmation = input("Are you sure you want to make a reservation? (Y to continue, anything else to cancel): ")
        if confirmation.lower() == 'y':
            reservation.make_reservation() # this calls the make reservation function from the reservation module if y is pressed
        else:  # otherwise it will print "reservation cancelled" then prompt the user to press enter
            print("Reservation canceled.")
        input("Press Enter to continue!")
    elif choice == '2':
        clear_screen()
        confirmation = input("Are you sure you want to cancel a reservation? (Y to continue, anything else to cancel): ")
        if confirmation.lower() == 'y':
            reservation.cancel_reservation()  # this calls the cancel reservation function from the reservation module
        else:
            print("Cancellation canceled.")
        input("Press Enter to continue!")
    elif choice == '3':
        clear_screen()  # this calls the update reservation function from the module reservation
        confirmation = input("Are you sure you want to update a reservation? (Y to continue, anything else to cancel): ")
        if confirmation.lower() == 'y':
            reservation.update_reservation()
        else:
            print("Update canceled.")
        input("Press Enter to continue!")
    elif choice == '4':
        clear_screen()
        confirmation = input("Are you sure you want to select a random dish? (Y to continue, anything else to cancel): ")
        if confirmation.lower() == 'y':
            dish = menu.select_random_dish()
            if dish:
                print("Selected dish:", dish)
        else:
            print("Selection canceled.")
        input("Press Enter to continue!")
    elif choice == '5':
        confirmation = input("Are you sure you want to display all reservations? (Y to continue, anything else to cancel): ")
        if confirmation.lower() == 'y':
            while True:  # this is a basic login for our lecturer to use the provided username and password to display all the reservations
                username = input("Enter staff ID: ")
                if username == staff_id:
                    entered_password = input("Enter your password: ")
                    if entered_password == staff_pw:
                        clear_screen()
                        print("All Reservations:")
                        display_reservations.display_reservations()
                        input("Press Enter to continue!")
                        break
                    else:
                        print("Incorrect password.")
                        confirmation = input("Press B to abort and return to the main menu: ")
                        if confirmation.lower() == "b":  # this is to return to the main menu if the password is incorrect, or to try again
                            break
                else:
                    print("Invalid staff ID.")
                    confirmation = input("Press B to abort and return to the main menu: ")
                    if confirmation.lower() == "b": # this ensures that if a B or b is entered, it will always be a lower case to fufil the corresponding requirements to end the function
                        break
    elif choice == '6':
        confirmation = input("Are you sure you want to exit? Press B to confirm")
        if confirmation.lower() == "b":
            exit()  # this just ends the code
    else:
        print("Invalid choice. Please try again.")  # in the case of the input being anything other than a number between 1 and 6
        input("Press Enter to continue...")
