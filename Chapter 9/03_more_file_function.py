f = open("file.txt")

lines = f.readlines()
# readlines() ak list ko create karta hai jo file.txt me list hai usko isme access karke list banata hai

print(lines, type(lines))
f.close()