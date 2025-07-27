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