# Does the user want to keep going
keep_going = 'y'

while keep_going.lower()[0] == 'y':

    # Ask the user to input their first name
    first_name = input("Please enter your first name: ")

    # Ask the user to input their surname
    surname = input("Please enter your surname: ")

    confirmation = ' '

    # Respond based on the user's confirmation
    while confirmation.lower()[0] != 'y' and confirmation.lower()[0] != 'n':
        # Confirm the full name with the user
        confirmation = input(f"Is your name {first_name} {surname}? (yes/no): ")
        if confirmation.lower()[0] == 'y':
            print("Thank you for confirming your name.")
        elif confirmation.lower()[0] == 'n':
            print("Please try to get the correct name next time.")
        else:
            print("Please enter 'yes' or 'no'")
    keep_going = input("Would you like to keep going? (yes/no): ")
    while keep_going.lower()[0] != 'y':
        if keep_going.lower()[0] == 'n':
            print("Goodbye!")
            break
        elif keep_going.lower()[0] != 'y':
            print("Please enter 'yes' or 'no'")
            keep_going = input("Would you like to keep going? (yes/no): ")
    
        
