class Employee:  
    language = "python"  # This is a class attribute
    salary = 323323

abhi = Employee()  
abhi.name = "Abhinav"  # This is a class attribute (abhi is a object )
print(abhi.name, abhi.salary, abhi.language) # call the class

# as like , create a many object in class

raju = Employee()
raju.name = "Rajan"
print(raju.name, raju.salary, raju.language)