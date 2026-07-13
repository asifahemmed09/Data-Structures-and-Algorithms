n = 153
def is_armstrong_number(n):
    num = n
    digit_count = len(str(num))
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** digit_count
        num //= 10
    return total == n

print(is_armstrong_number(n))

"""
Time Complexity - O(log10(n))
Space Complexity - O(1)
"""


