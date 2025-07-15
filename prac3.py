a = int(input("Enter a number: "))

for i in range(2, a):
  if (a%i ) == 0:
       print("number is not prime")
       break
  else:
     print("number is prime")
print("Check completed.")
# This code checks if a number is prime by testing divisibility from 2 to the number minus one. If it finds any divisor, it concludes that the number is not prime; otherwise, it declares the number as prime. The check is completed with a final print statement.

n = int(input("Enter a number: "))
i=1
sum = 0
while (i <= n):
    sum+=i
    i+=1
print(sum)
# This code calculates the sum of all integers from 1 to n using a while loop. It initializes a sum variable to zero and iterates from 1 to n, adding each integer to the sum. Finally, it prints the total sum.