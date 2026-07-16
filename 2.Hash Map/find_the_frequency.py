""""
Given an array arr of positive integers and an integer x. Return the frequency of x in the array.
1 ≤ arr.size() ≤ 10 ** 5
1 ≤ arr[i] ≤ 10 ** 5
1 ≤ x ≤ 10 ** 5
"""
arr = [1, 2, 3, 3, 2, 1]
x=2

def find_frequency(arr,x):
    count = 0
    for i in arr:
        if arr[i] == x:
            count += 1
    return count

print(find_frequency(arr,x))

"""
Time Complexity - O(n)
Space Complexity - O(1)
"""

