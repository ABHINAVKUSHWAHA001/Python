# kisi files ko jaise file.txt ak new file create kiye usme (a = "A veru long string with emails") ye dala 
# abb 01_file.py me pichle file ko access kiya ja sakta hai. is method ke jariye.
'''
a = "dfdfdsagafgfd"

emails = []
3 seconds
'''

f = open("file.txt", "r") #file.txt jo hum pahale hi file bana chuke hai usko yaha se open kar rha hai
data = f.read()
print(data)
f.close()