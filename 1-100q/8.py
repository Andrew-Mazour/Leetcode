def myAtoi(s: str) -> int:
    s = s.lstrip()
    
    if not s:
        return 0

    # Determine sign
    sign = 1
    if s[0] == '-':
        sign = -1
        s = s[1:]
    elif s[0] == '+':
        s = s[1:]

    # Convert the number
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break

    # Apply sign
    result *= sign
    
    max = 2**31 - 1
    min = -2**31

    if result > max:
        return max
    if result < min:
        return min

    return result
