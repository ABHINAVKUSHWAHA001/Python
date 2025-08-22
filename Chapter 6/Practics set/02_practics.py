marks1 = int(input("Enter Marks1 :-"))
marks2 = int(input("Enter Marks2 :-"))
marks3 = int(input("Enter Marks3 :-"))

# check for total percentages:
total_percentage = 100*(marks1 + marks2 + marks3)/300
if(total_percentage >= 40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are Passed")
    print("Your Percentage is:", total_percentage)

else:
    print("You Failed , try again next year!! ")
    print("Your Percentage is:", total_percentage)