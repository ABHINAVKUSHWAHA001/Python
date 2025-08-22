#  Type and TypeCasting.

#  Type ()function is used to find the dayta type of a given variable in python

# <class 'int'>
a = 5
# a = '5'   # this is a string because using (' '), its a string.
t = type(a)
print(t)


# <class 'str'>
b = "abhi"
# b = 'abhi'  ('') these are using in string.
t = type(b)
print(t)


# <class 'float'>
c = 0.423
t = type(c)
print(t)
# Note :- Yadi hum (a = "343.543") Jo ki string hai usse hum string se float me kar sakte yaise.
a = "343.543"
b = float(a)  # a is string but these will be change as a float like this.
t = type(b)
print(t)


# <class 'bool'>
d = True
a = False 
t = type(d)
t = type(a)
print(t)

