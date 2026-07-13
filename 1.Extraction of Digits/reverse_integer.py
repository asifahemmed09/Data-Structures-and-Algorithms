n = -123


def reverse_number(n):
    sign = -1 if n < 0 else 1
    num = abs(n)
    reversed_num = 0
    while num > 0:
        last_digit = num % 10
        reversed_num = (reversed_num * 10) + last_digit
        num = num // 10
    if reversed_num < -(2**31) or reversed_num > 2**31 - 1:
        return 0
    return reversed_num * sign


print(reverse_number(n))

"""
Time Complexity - O(log10(n))
Space Complexity - O(1)
"""
