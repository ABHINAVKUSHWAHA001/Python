# write a program to find the greatest of four number entered by the user.

a1 = int(input("Enter the number of 1:"))
a2 = int(input("Enter the number of 2:"))
a3 = int(input("Enter the number of 3:"))
a4 = int(input("Enter the number of 4:"))

if(a1 > a2 and a1 > a3 and a1 > a4):
    print("Greater no. is a1",a1)

elif(a2 > a1 and a2 > a3 and a2 > a4):
    print("Greater no. is a2",a2)

elif(a3 > a1 and a2 > a3 and a3 > a4):
    print("Greater no. is a3 ", a3)

else:
    print("Greater no. is a4", a4) 

print("Thank you!")