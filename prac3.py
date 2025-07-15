a = int(input("Enter a number: "))

for i in range(2, a):
  if (a%i ) == 0:
       print("number is not prime")
       break
  else:
     print("number is prime")
print("Check completed.")
# This code checks if a number is prime by testing divisibility from 2 to the number minus one. If it finds any divisor, it concludes that the number is not prime; otherwise, it declares the number as prime. The check is completed with a final print statement.
