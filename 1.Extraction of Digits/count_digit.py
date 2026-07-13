n = 5467379

num = n
count = 0
while num > 0:
    count += 1
    num = num // 10

print(count)

"""
Time Complexity - O(log10(n))
Space Complexity - O(1)
"""
