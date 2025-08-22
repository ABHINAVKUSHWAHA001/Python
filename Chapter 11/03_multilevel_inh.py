# Sabse pehle Grandparent class
class Grandfather:
    def house(self):
        print("Grandfather has a big house")

# Grandfather se inherit karke Parent class
class Father(Grandfather):
    def car(self):
        print("Father has a car")

# Father se inherit karke final Child class
class Son(Father):
    def laptop(self):
        print("Son has a laptop")

s = Son()

s.house()    # From Grandfather
s.car()      # From Father
s.laptop()   # From Son
