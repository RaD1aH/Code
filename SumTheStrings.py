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