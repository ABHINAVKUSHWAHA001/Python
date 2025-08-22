# write a rcursive fuction to calculate the sum of list n natural number: use list & index as parameter.
def print_list(list, index = 0):
    if(index == len(list)):
        return
    print(list [index])
    print_list(list, index +1)

name = ["Abhi","Sohan", "Mohan", "Ram"]
print_list(name)