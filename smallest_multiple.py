'''
Docstring for smallest_multiple

<p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
<p>What is the smallest positive number that is <strong class="tooltip">evenly divisible<span class="tooltiptext">divisible with 
no remainder</span></strong> by all of the numbers from $1$ to $20$?</p>

'''

# 80 is the lowest common multiple of 20 and 16
# This code finds it in 24 iterations
number = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
while number:
    if  number % 9 == 0 and number % 80 == 0:
        print(number)
        break
    else:
        number += 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19

'''
    Gemini Solution
import math
from functools import reduce

def lcm(a, b):
    # Standard formula for LCM using GCD
    return abs(a * b) // math.gcd(a, b)

def solve_euler_5(limit):
    # reduce applies the lcm function cumulatively to the range
    return reduce(lcm, range(1, limit + 1))

answer = solve_euler_5(20)
print(f"The smallest multiple is: {answer}")
'''