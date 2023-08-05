def isPalindrome(s):
    return s == s[::-1]

def binaryPalin(num):
    binary = bin(num)
    binary = binary[2:]
    return isPalindrome(binary)

num = 9

if binaryPalin(num):
    print("Yes")
else:
    print("No")
