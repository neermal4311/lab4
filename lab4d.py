#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(s):
    """
    Returns the first five characters of the given string.

    Args:
        s (str): The input string.

    Returns:
        str: A substring containing the first five characters of `s`.
    """
    return s[:5]

def last_seven(s):
    """
    Returns the last seven characters of the given string.

    Args:
        s (str): The input string.

    Returns:
        str: A substring containing the last seven characters of `s`.
    """
    return s[-7:]

def middle_number(n):
    """
    Returns a string containing the second and third characters of the given number.

    Args:
        n (int or float): The input number.

    Returns:
        str: A string containing the second and third characters of the number's string representation.
    """
    num_str = str(n)
    # Ensure that the number has at least three characters
    if len(num_str) >= 3:
        return num_str[1:3]
    elif len(num_str) == 2:
        return num_str[1]
    else:
        return num_str

def first_three_last_three(s1, s2):
    """
    Combines the first three characters of `s1` with the last three characters of `s2`.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.

    Returns:
        str: A new string consisting of the first three characters of `s1` and the last three characters of `s2`.
    """
    return s1[:3] + s2[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))
