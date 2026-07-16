nums =  [5,6,7,7,1,9,111,1,1,5,1,1]

def get_frequency(nums,n):
    frequency_map = {}
    for i in range(0,len(nums)):
        if nums[i] in frequency_map:
            frequency_map[nums[i]] += 1
        else :
            frequency_map[nums[i]] = 1
    return frequency_map[n]

print(get_frequency(nums,5))

"""
Time Complexity - O(n)
Space Complexity - O(n)
"""

def get_frequency_method2(nums,n):
    hash_map = {}
    for i in range(0,len(nums)):
        hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
    return hash_map[n]


print(get_frequency_method2(nums,5))
