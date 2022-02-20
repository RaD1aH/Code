# Create a function that takes 2 integers in form of a string #
# as an input, and outputs the sum (also as a string):        #
# Example: (Input1, Input2 -->Output)                         #

def sum_str(a, b):
    if a.isdigit() and b.isdigit():
        sum_ab = int(a) + int(b)
        result = str(sum_ab)
        return result
    elif a.isdigit() or b.isdigit():
        sum_ab = a.strip() + b.strip()
        result = str(sum_ab)
        return result
    else:
        return "0"