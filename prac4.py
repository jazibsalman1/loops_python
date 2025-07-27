class programmer:
    company = "Google"
    a="jazib"
    b=100000000000000

jazib = programmer()
print("Company:", jazib.company," and Name:", jazib.a, " and Salary:", jazib.b)    
#another way of doing this is
class programmers:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
object = programmers("Jazib", 100000000000000000)        
print("Name:", object.name, " and Salary:", object.salary)


#problem no 2
class calculator:
    def __init__(self, a):
        self.a = a
        
    # This is a constructor that initializes the attributes a for the calculator class.
    def square(self):
        return self.a * self.a
# This method calculates the square of the attribute a.
    # It returns the square of the value stored in a.
    def cube(self):
        return self.a * self.a * self.a
    def squareroot(self):
        return self.a ** 0.5
    # This method calculates the cube of the attribute a.
    # It returns the cube of the value stored in a.
j=calculator(4)
print("Square of 5 is:", j.square())
print("Cube of 5 is:", j.cube())
print("Square root of 5 is:", j.squareroot())
# This code defines a constructor that prints a message when an instance of the class is created. It does not take any parameters and does not belong to any class.

   
        