def magic_trick():
    # (a) 
    # Ask user to pick a number between 1 and 9
    print("Pick a number between 1 and 9: ")
    
    # The number the user picks
    original_number = int(input())

    # (b) 
    # Multiply result by 2
    result = original_number * 2

    # (c)
    # Add result by 5
    result += 5

    # (d)
    # Multiply result by 50
    result *= 50

    # (e) 
    # Ask user if their birthday passed yet
    print("Have you already had your birthday this year? (yes/no): ")

    # Capture if the birthday has passed
    birthday_passed = input().strip().lower()
    
    # Add 1750 if birthday has already passed, else add 1749
    if birthday_passed == 'yes':
        result += 1750  # Add 1750 if birthday has passed
    else:
        result += 1749  # Add 1749 if birthday hasn't passed

    # (f)
    # Ask the user what year is it
    print("What is the current year? (e.g., 2022) ")
    
    # User inputs the current year
    current_year = int(input())
    
    # Take the last 2 digits of the year
    last_two_digits_of_year = str(current_year)[-2:]
    
    # Add the last digits of the current year
    result += int(last_two_digits_of_year)

    #(g)
    # Ask user what year are they born in
    print("Enter the year you were born (e.g., 1984): ")
    
    # The user inputs their birth year
    birth_year = int(input())
    
    # Subtract the year you were born
    result -= birth_year

    #(h)
    # Output the result:
    # It should be a 3-digit number. The first digit is your original number and the next two numbers are your age
    print(f"Your magic number is: {result}")

# Run the magic trick
magic_trick()



