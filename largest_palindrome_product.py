'''
Docstring for largest_palindrome_product

<p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
<p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>

'''

import math, time
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
    
start_time = time.perf_counter()
for i in range(999999, 10000, -1):
    list = find_multipliers(i)
    if is_palindrome(i) and list:
        print(str(i) + " can be written as " + str(list[0]) + " * " + str(list[1]))
        break
end_time = time.perf_counter()
print(f"Execution Time: {(end_time - start_time) * 1000:.4f} ms")

''' The most efficient way by Gemini

def is_palindrome(n):
    """
    Checks if a number is a palindrome using string slicing.
    This is faster than mathematical reversal for Python integers.
    """
    s = str(n)
    return s == s[::-1]

def solve_euler_4_optimized():
    """
    Finds the largest palindrome from the product of two 3-digit numbers
    using search pruning and the Modulo 11 mathematical property.
    """
    largest_palindrome = 0
    
    # Iterate x downwards from 999
    for x in range(999, 99, -1):
        
        # Pruning 1:
        # The largest possible product with the current x is x * 999.
        # If this is smaller than the palindrome we've already found, 
        # we can't possibly find a larger one with this x or any smaller x.
        # We can stop completely.
        if x * 999 <= largest_palindrome:
            break
            
        # Optimization: Modulo 11 Check
        # A 6-digit palindrome (abccba) is always divisible by 11.
        # P = 100001a + 10010b + 1100c = 11 * (9091a + 910b + 100c)
        # Since P = x * y is divisible by 11, either x or y must be divisible by 11.
        
        if x % 11 == 0:
            # If x is divisible by 11, y can be anything.
            start_y = 999
            step_y = 1
        else:
            # If x is NOT divisible by 11, y MUST be divisible by 11.
            # Start at the largest multiple of 11 <= 999
            start_y = 990 
            step_y = 11

        # Iterate y downwards
        for y in range(start_y, x - 1, -step_y):
            product = x * y
            
            # Pruning 2:
            # Since y is decreasing, if the current product is smaller than
            # the largest found so far, no subsequent y will work for this x.
            if product <= largest_palindrome:
                break
                
            if is_palindrome(product):
                largest_palindrome = product
                # We found the largest palindrome for this specific x.
                # Since y is decreasing, we won't find a larger one with this x.
                break 

    return largest_palindrome

if __name__ == "__main__":
    start_time = time.perf_counter()
    result = solve_euler_4_optimized()
    end_time = time.perf_counter()
    
    print(f"Largest Palindrome: {result}")
    print(f"Execution Time: {(end_time - start_time) * 1000:.4f} ms")'''