# Example usage of the walrus operator (:=) in Python 3.8+

# # Read input and check if it's not empty using the walrus operator
while (user_input := input("Enter something (or 'exit' to quit): ")) != 'exit':
    print(f"You entered: {user_input}")
else:
    print("Exiting the loop.")