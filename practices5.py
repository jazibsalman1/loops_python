class Employee:
    
    salary = int(input("Enter the salary: "))
    increment = int(input("Enter the percent: "))

    def salary_after_increment(self):
        return self.salary + (self.increment / 100) * self.salary

# Create an object
a = Employee()

# Display results
print(f"Original Salary: {a.salary}")
print(f"Increment Percent: {a.increment}%")
print(f"Salary After Increment: {a.salary_after_increment()}")
# This code defines a class `b` that inherits from class `a` and adds a new method `newjazzib` that prints a message when called.