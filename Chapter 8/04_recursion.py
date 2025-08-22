# Recursion function 
# def show(n):
#     if(n == 0): # The function will going to the 0, so it will be return
#         return
#     print(n)
#     show(n-1)
# show(4)


# factorial in recursion
def fact(n):
    if(n == 1):
        return 1

    return fact(n - 1) * n
print("Your factorial num is: ",(fact (5) ))