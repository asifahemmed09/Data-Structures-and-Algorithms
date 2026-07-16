"""
Constraints
'a' <= s[i] <= 'z'
"""

s = "azyxyyxaaaa"
q = ["d","a","y","x"]
hash_list = [0] * 26

for i in s:
    ascii_value = ord(i)
    index = ascii_value - 97
    hash_list[index] += 1


for j in q:
    ascii_value = ord(j)
    index = ascii_value -97
    print(j,hash_list[index],sep="-")

"""
Time Complexity - O(n)
Space Complexity - O(1)
"""
