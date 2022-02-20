# Write a function that checks if a given string (case insensitive) is a palindrome. #

def is_palindrome(s):
    rev_string = ''.join(reversed(s))
    if rev_string.casefold() == s.casefold():
        return True
    else:
        return False