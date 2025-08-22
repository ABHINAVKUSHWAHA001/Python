class Employee():
    salary = 23423
    language = "java"

    def __init__(self):  # dunder method which is automatically called
        print("I am creating an object:")

    def getInfo(self): # create function and given the language and salary.
        print(f"The language is {self.language}. The salary is{self.salary}")
        
    @staticmethod # this method is used to given without objects
    def greet(): 
        print("good morning")

abhi = Employee() # this is object
abhi.name = "Abhinav"  # inherite language
print(abhi.name, abhi.salary)

 