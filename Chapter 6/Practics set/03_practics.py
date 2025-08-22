# A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "but now", "subscribe this", "click this". WAP to detect these spams.

p1 = "Make a lot of money"
p2 = "subscribe this"
p3 = "buy now"
p4 = "click this"

messege = input("Enter Your comment :")

if((p1 in messege) or (p2 in messege) or (p3 in messege) or (p4 in messege)):
    print("This comment is a spam")
else:
    print("This comment is not a spam") 