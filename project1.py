import random
number_to_guess = random.randint(1, 50)
attempts = 0

while True:
    guess = input("Guess the number between 1 and 50: ")
    try:
     guess = int(guess)
    except ValueError:
        print("Please enter a valid integer.")x
        continue
    attempts += 1
    if guess < number_to_guess:
        print("Go higher!")
    elif guess > number_to_guess:
        print("Go lower!")
    else:
        print(f"Congratulations! You guessed the number in {attempts} tries.")
            
        break 