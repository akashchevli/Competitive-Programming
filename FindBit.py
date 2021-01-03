"""
    Write a program to find out the bits of the given number

    Input
        Enter number:7
        How many bits want:4

    Output
        0111

    Description
        The original bits of number 7 is 111, but the user want 4 bits so you have added zeros in front of the bits

    Input
        Enter number:12
        How many bits want:2

    Output:
        Actual bits is greater than the bits you want

    Description
        The original bits of number 12 is 1100, but the user enters 2 bits which is less than the length of the original bits
        that's why it will be thrown an error

"""

result = ''
negative = False


def getBit(n):
    global result, negative

    if str(n)[0] == '-':
        n = str(n)[1:]
        negative = True

    n = int(n)
    if n == 0 or n == 1:
        return str(n).zfill(bits)

    next_n = n // 2
    rem = n % 2
    result += str(rem)
    if next_n == 1:
        result = str(next_n) + result[::-1]
        size = len(result)
        if bits < size:
            return "Actual bits is greater than the bits you want"
        if negative:
            return '-' + result.zfill(bits)
        return result.zfill(bits)
    return getBit(next_n)


n = int(input("Enter number:"))
bits = int(input("How many bits want:"))
print(getBit(n))