# Create a function with two arguments that will return an array of the first n multiples of x.
# Assume both the given number and the number of times to count will be positive numbers greater than 0.

def count_by(x, n):
    return [i * x for i in range(1, n + 1)]

def count_by2(x, n):
    lst = []
    for i in range(1, n+1):
        lst.append(i*x)
    return lst