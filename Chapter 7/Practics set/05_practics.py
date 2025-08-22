# WAP print the following star pattern.for n = 3
'''
    *
   ***
  *****

 '''

# n = int(input("Enter the number:"))
# for i in range(1, n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end ="")
#     print("")
 

n = int(input("Enter the number:"))
for i in range(1, n+1):
    print(" "* (n-1), end="")
    print("*"* i, end ="")
    print("")
 
