'''
<p>If we list all the natural numbers below $10$ that are multiples of $3$ or $5$, we get $3, 5, 6$ and $9$. The sum of these multiples is $23$.</p>
<p>Find the sum of all the multiples of $3$ or $5$ below $1000$.</p>
'''

sum = 0
for x in range(5, 1000, 5):
    sum += x

for x in range(3, 1000, 3):
    if(x % 5 != 0):
        sum += x
print(sum)

'''
Most Efficient Way which will work with large numbers

def sum_multiples(target, n):
    """Calculates the sum of multiples of n below target."""
    m = (target - 1) // n
    return n * m * (m + 1) // 2

def solve(limit):
    return (sum_multiples(limit, 3) + 
            sum_multiples(limit, 5) - 
            sum_multiples(limit, 15))

# Execution
limit = 1000
print(f"The sum is: {solve(limit)}")

'''