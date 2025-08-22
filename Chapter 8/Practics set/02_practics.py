# WAF to print the elements of a list in a single line.(list is the parameter)


heroes = ["Iranman", "Superhero", "Captain America", "Spiderman"]


def print_list(list):
    for item in list:
        print(item, end=" ")  # end=" " uses next line me print na karake same line me output continue karwana hota hai.

print_list(heroes)
print()


# end=" " uses
print("Hello",end=" ")
print("World" )