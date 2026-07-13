n = 1234


def check_palindrome_number():
    num = n
    result = 0
    while num > 0:
        last_digit = num % 10
        result = (result * 10) + last_digit
        num = num // 10
    return result == n


is_palindrome = check_palindrome_number()
print(is_palindrome)

"""
Time Complexity - O(log10(n))
Space Complexity - O(1)
"""
