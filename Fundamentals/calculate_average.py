# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0

def find_average(numbers):
    return sum(numbers) / len(numbers) if len(numbers) else 0

def find_average(numbers):
    if len(numbers):
        return sum(numbers) / len(numbers)
    else: 
        return 0
    
print(find_average([1, 2, 3]))