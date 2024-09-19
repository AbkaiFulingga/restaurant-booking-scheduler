import random  # this is to generate a random option from the text file

def read_menu(): # this function reads the items residing inside the menu
    with open('MenuItems_20084695.txt', 'r') as file:  # this opens and reads the the menu text
        menu = file.readlines()
    if menu:
        return [dish.strip() for dish in menu]  # this returns the iteration of all the items in the menu
    else:
        print("Error no menu items")  # in the event of no items residing in the menu

def select_random_dish():  # this is to select a random dish from the presets in the text file
    menu = read_menu()
    if menu:
        return random.choice(menu)   # this utilises the random module and picks a random dish
    else:
        print("Error no menu items")
