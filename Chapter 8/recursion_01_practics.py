def cal_sum(n):
    if(n== 0):
        return 0
    return cal_sum(n-1) + n
sum = cal_sum(5)
print(sum)
# n =   5
# 5-1 = 4 
# 4-1 = 3
# 3-1 = 2
# 2-1 = 1   5+4+3+2+1 = 15 