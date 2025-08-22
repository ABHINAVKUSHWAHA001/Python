#  Self refers to the instance of the class. it is automatically passed with a functin call from an object;
class Employee():
    salary = 23423
    language = "java"

    def getInfo(self): # create function and given the language and salary.
        print(f"The language is {self.language}. The salary is{self.salary}")
        
    @staticmethod # this method is used to given without objects
    def greet(): 
        print("good morn ing")

abhi = Employee() # this is object
abhi.language = "python"  # inherite language
abhi.greet()
abhi.getInfo()  # call the function/
