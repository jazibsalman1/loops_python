try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number!")
except TypeError:
    print("A type error occurred!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("No exceptions occurred.")