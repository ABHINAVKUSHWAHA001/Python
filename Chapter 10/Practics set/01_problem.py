#  Create a class " Programmer" for storing information of few programmer working at microsoft

# class programmer:
#     name = "abhinav"
#     id = 3423
#     salary = 323232
#     company = "Microsoft"
#     print("The programmer is working in Microsoft")

# employee = programmer()
# print(employee.name, employee.id, employee.salary, employee.company)

class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin 

p = programmer("Abhinav", 3423232, 2323245)
print(p.name, p.salary, p.pin, p.company)
        
