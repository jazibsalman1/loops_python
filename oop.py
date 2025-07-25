class employee :
    name = "Jazib"
    age = 19
    salary = 10000000000000
    def info(self): #by default pa ya object ko as a argument pass krta hai
        print("My Name is:", self.name, "and my Age is:", self.age, "and my Salary is:", self.salary)


jazib = employee()
jazib.info()
jazib.brother = "Aaban"
print(jazib.name ,jazib.age, jazib.salary,jazib.brother)

# This code defines a class `employee` with attributes for name, age, and salary. It creates an instance of the class and prints the attributes of that instance, which are initialized with specific

def getinfo():
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        salary = int(input("Enter your salary: "))
        print("My Name is:",name , "and my Age is:", age, "and my Salary is:", salary)
        
getinfo()     
#values. The `getinfo` function prompts the user for their name, age, and salary, and then prints that information.