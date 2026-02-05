'''
Docstring for sum_square_difference
<p>The sum of the squares of the first ten natural numbers is,</p>
$$1^2 + 2^2 + ... + 10^2 = 385.$$
<p>The square of the sum of the first ten natural numbers is,</p>
$$(1 + 2 + ... + 10)^2 = 55^2 = 3025.$$
<p>Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.</p>
<p>Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.</p>
'''

def sum_of_the_squares(number):
    sum = number * (number + 1) * (2 * number + 1) / 6
    return int(sum)
def squares_of_the_sum(number):
    sum = int(number * (number + 1) / 2)
    return sum * sum
    
def sum_square_difference(number):
    return squares_of_the_sum(number) - sum_of_the_squares(number)
    
print(sum_square_difference(100))