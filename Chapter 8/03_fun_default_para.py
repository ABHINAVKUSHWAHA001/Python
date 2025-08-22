# Default parameters:
# Default para tab used hota hai jab func calling ke time koi arugment nahi diya jata, to hum function me value dete hai
def cal_prod(a , b = 2):
    print(a*b)
    return a*b
cal_prod(2)  # this is only access (a) in func, because given the value b = 2, so it is access only a paramters.



# Yaha par hum bina argument ke hi func ko call kar rhe hai, kyuki hum function me (a & b) ka value pahle se diya gaya hai.
# isse hum Default parameter kahate hai.
def cal_prod(a = 3, b = 2):
    print(a*b)
    return a*b
cal_prod() 