# WAP find whether a given number is prime or not.

# prime num wo hota hai jo divide hone par uske factor me 1 aaye ya wo khud aaye. as like, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23 etc.

n = int(input("Enter a number :"))

for i in range(2, n):
    if(n%i) == 0:
        print("Number is not prime")
        break

else:
    print("Number is prime. Thanks!")