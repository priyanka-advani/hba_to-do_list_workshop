"""This is a Terminal-based program that allows a user to create and edit a to-do list.

The stub of each function has been provided. Read the docstrings for what each 
function should do and complete the body of the functions below.

You can run the script in your Terminal at any time using the command:

    >>> python todo_list.py

"""

def add_to_list(my_list):
    """Takes user input and adds it as a new item to the end of the list."""

    new_task = raw_input("What do you want to add to your list? ")
    list_number = int(raw_input("Where do you want to put this item in your list? ")) - 1
    my_list.insert(list_number, new_task)
    # print my_list[0]
    # print my_list
    return my_list


def view_list(my_list):
    """Print each item in the list."""
    
    for task in my_list:
        print task


def display_main_menu(my_list):
    """Displays main options, takes in user input, and calls view or add function."""

    user_options = """
    \nWould you like to:
    A. Add a new item to your list
    B. View list
    C. Quit the program
    D. Remove first item in list
    >>> """

    while True:
        # Collect input and include your if/elif/else statements here.
        user_choice = raw_input(user_options)
        if user_choice == "A":
            add_to_list(my_list)
        elif user_choice == "B":
            view_list(my_list)
        elif user_choice == "C":
            break
        elif user_choice == "D":
            del my_list[0]
        else:
            print "Sorry! That's not a valid choice."

#-------------------------------------------------

my_list = []
display_main_menu(my_list)

