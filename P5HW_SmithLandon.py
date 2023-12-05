#This is a Math Quiz using some info from the library.
#12/4/2023
#CTI-110 P5HW - Math Quiz
#Landon Smith





import random

def generate_numbers():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def add_numbers():
    num1, num2 = generate_numbers()
    result = num1 + num2

    while True:
        try:
            user_guess = int(input(f"What is {num1} + {num2}? "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_guess == result:
            print("Congratulations! You guessed it right.")
            break
        elif user_guess < result:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

def subtract_numbers():
    num1, num2 = generate_numbers()
    result = num1 - num2

    while True:
        try:
            user_guess = int(input(f"What is {num1} - {num2}? "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        if user_guess == result:
            print("Congratulations! You guessed it right.")
            break
        elif user_guess < result:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

def display_menu():
    print("MENU")
    print("1. Add numbers and guess the result")
    print("2. Subtract numbers and guess the result")
    print("3. Quit")

def get_user_choice():
    try:
        choice = int(input("Enter your choice (1/2/3): "))
        return choice
    except ValueError:
        return -1  # Invalid input

def execute_menu_choice(choice):
    if choice == 1:
        add_numbers()
    elif choice == 2:
        subtract_numbers()
    elif choice == 3:
        print("Goodbye!")
        return False  # Terminate the program
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
    return True

def play_math_quiz():
    while True:
        display_menu()
        user_choice = get_user_choice()

        if not execute_menu_choice(user_choice):
            break

if __name__ == "__main__":
    play_math_quiz()