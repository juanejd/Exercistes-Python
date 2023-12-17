# Create a function that takes an integer as an argument and returns 
#"Even" for even numbers or "Odd" for odd numbers.

from random import *

def even_or_odd(number):
    return 'even' if number % 2 == 0 else 'odd'

num = even_or_odd(-2)

print(num)