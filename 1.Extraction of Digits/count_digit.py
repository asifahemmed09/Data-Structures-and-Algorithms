# count total number of digits
n = 5467379

num = n
count = 0
while num > 0:
    count += 1
    num = num // 10

print(count)

"""
Time Complexcity - Big O(log10(n))
Space Complexcity - Big O(1)
"""
