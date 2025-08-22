# Ye base class hai jisme Employee ka basic detail diya gaya hai
class Employee:
    company = "ITC"                   # Class variable: sabhi employees ka company same
    name = "Default name"             # Default name diya gaya hai

    def show(self):
        # Employee ka naam aur company print karega
        print(f"The name of the Employee is {self.name} and the company is {self.company}")


# Ye second base class hai jisme programming language ka knowledge hai
class Coder:
    language = "Python"               # Default programming language

    def printLanguages(self):
        # Programming language print karega
        print(f"Out of all the languages, here is your language: {self.language}")


# Ye derived class hai jo Employee aur Coder dono ko inherit karti hai
class Programmer(Employee, Coder):
    company = "ITC InfoTech"          # Is class ka company name alag hai

    def showLanguage(self):
        # Company aur language dono print karega
        print(f"The name is {self.company} and they are good with {self.language} language")


# Object banaye gaye
a = Employee()     # a ek normal employee object hai
b = Programmer()   # b ek programmer object hai jo employee + coder dono ka feature rakhta hai

# Programmer class ke object ke through methods call kiye gaye
b.show()              # Employee class ka method (inherited)
b.printLanguages()    # Coder class ka method (inherited)
b.showLanguage()      # Programmer class ka apna method



## Base class 1
# class Father:
#     def skills(self):
#         print("Father knows gardening and cooking")

# # Base class 2
# class Mother:
#     def more_skills(self):
#         print("Mother knows painting and teaching")

# # Child class that inherits both Father and Mother
# class Child(Father, Mother):   #  Yaha ho raha hai multiple inheritance
#     def own_skill(self):
#         print("Child knows Python programming")


# # Object of Child class
# c = Child()

# # Calling methods from both parent classes and its own
# c.skills()          # From Father class
# c.more_skills()     # From Mother class
# c.own_skill()       # Child class method