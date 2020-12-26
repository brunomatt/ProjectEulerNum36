# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)
upper_limit = 1000000
decimal_palindromes = []
dual_base_palindromes = []
answer = 0

def convert_binary(num):
    return bin(num).replace("0b", "")

def palindrome_check(num):
    if str(num)[::] == str(num)[::-1]:
        return True
    else:
        return False

for k in range(1, upper_limit):
    if palindrome_check(k) is True:
        decimal_palindromes.append(k)

for num in decimal_palindromes:
    if palindrome_check(convert_binary(num)) is True:
        dual_base_palindromes.append(num)

answer = sum(i for i in dual_base_palindromes)

print(answer)