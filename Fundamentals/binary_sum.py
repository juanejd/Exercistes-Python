# Implement a function that adds two numbers together and returns their sum in binary. 
#The conversion can be done before, or after the addition.

# The binary number returned should be a string.

# Examples:(Input1, Input2 --> Output (explanation)))

# def add_binary(a, b):
#     return bin(a + b)[2:]

# print(add_binary(1, 1))

def add_binary(a, b):
    num = a + b
    if num <= 0 :
        return 0
    
    binary = ''

    # Mientras el numero ingresado sea mayor a 0, seguiremos dividiendo entre 2
    while num > 0:
        # Sacamos el residuo del numero ingresado
        res = int(num % 2)
        # Ahora el numero ingresado lo dividimos entre 2 y volvemos al while con el nuevo numero. 
        num = int(num // 2)
        binary = str(res) + binary
        print(binary)
    return binary

print(add_binary(2, 7))