from math import sqrt

n = 36

# brute force solution
# def get_factors(n):
#     num = n
#     factors = []
#     for i in range(1,(num // 2) + 1):
#         if num % i == 0:
#             factors.append(i)
#     factors.append(n)
#     return factors

# print(get_factors(n))

# optimal solution
def get_factors(n):
    num = n
    factors = []
    for i in range(1,int(sqrt(num)+1)):
        if num % i == 0:
            factors.append(i)
        if num // i != i:
            factors.append(num // i)
        factors.sort( )
    return factors

print(get_factors(n))

"""
Time Complexity - O(√n) + O(nlogn)
Space Complexity - O(k)
"""
