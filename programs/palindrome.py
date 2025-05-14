"""
check give string is palindrome or not
"""


def is_palindrome(test_string):
    string = test_string.lower().replace(" ", "")
    return string == string[::-1]


print(is_palindrome("Madam"))
print(is_palindrome("hello"))