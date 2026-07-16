"""
Constraints
1 <= n[i] <= 10
n can have 10 ** 8 elements
m can have 10 ** 8 elements
"""
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

hash_list = [0] * 11

for i in n:
    hash_list[i] += 1

for j in m:
    if j < 1 or j > 10:
        print(j,0,sep=':')
    else:
        print(j,hash_list[j],sep=":")

"""
Time Complexity - O(n)
Space Complexity - O(1)
"""

# using dictionary

frequent_dict = {}

for i in n:
    if i in frequent_dict:
        frequent_dict[i] += 1
    else:
         frequent_dict[i] = 1

for j in m:
    if j not in frequent_dict:
        print(j,0,sep='-')
    else:
        print(j,frequent_dict[j],sep='-')


"""
Time Complexity - O(n)
Space Complexity - O(1)
"""
