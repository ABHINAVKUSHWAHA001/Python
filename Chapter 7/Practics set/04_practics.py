#  WAP calculate the factorial of a given number using for loop
# 5! = 1 X 2 X 3 X 4 X 5

n = int(input("Enter Your Numbers: "))
product = 1

for i in range(1, n+1):
    product = product * i

# print("The factorial is:", product)
print(f"The factorial of {n} is {product}")
