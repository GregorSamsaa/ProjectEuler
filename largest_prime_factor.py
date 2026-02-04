'''
Docstring for largest_prime_factor

<p>The prime factors of $13195$ are $5, 7, 13$ and $29$.</p>
<p>What is the largest prime factor of the number $600851475143$?</p>

'''
def is_prime(number):
    x = 2
    if number > 2:
        x = int(number / 2)
    for i in range(2, x):
        if number % i == 0:
            return False
    return True

def find_the_largest_prime_factor(number):
    i = 2
    while i < number:
        if number % i == 0 and is_prime(i):
            number = number / i
        else:
            i += 1
    return number

print(find_the_largest_prime_factor(600851475143))

'''
    Better way Gemini
def largest_prime_factor(n):
    divisor = 2
    
    while divisor * divisor <= n:
        if n % divisor == 0:
            # If it divides perfectly, shrink n
            n //= divisor
        else:
            # Move to the next potential factor
            # (After 2, we could technically just skip to odd numbers)
            divisor += 1
            
    return n

target = 600851475143
print(f"The largest prime factor is: {largest_prime_factor(target)}")
'''