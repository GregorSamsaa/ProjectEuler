'''
Docstring for largest_palindrome_product

<p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
<p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>

'''

import math
def is_palindrome(number):
    list = str(number)
    length = len(list)
    loop = length / 2
    i = 1
    while i <= loop:
        if list[i-1] == list[length-i]:
            # print(list[i-1], " = ", list[length - i])
            i += 1
        else:
            return False
    return True

def find_multipliers(number):
    root = int(math.sqrt(number))
    for i in range(root, 99, -1):
        if number % i == 0:
            multiplier = int(number / i)
            if multiplier < 1000:
                return i, multiplier
    

for i in range(999999, 10000, -1):
    list = find_multipliers(i)
    if is_palindrome(i) and list:
        print(str(i) + " can be written as " + str(list[0]) + " * " + str(list[1]))
        break

