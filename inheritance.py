class a:
    def jazib(self):
        
        print("jazib")
    def jazib2(self):
        print ("jazib2")  
class b(a):
    def newjazzib(self):
        print("new jazib")                
# This code defines a class `a` with a method `jazib` that returns the string "jazib" when called. The print statement is unreachable because it comes after the return statement
# This code defines a class `a` with a method `jazib` that prints a message when called.
c=a()
d=b()
d.newjazzib()