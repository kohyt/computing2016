# recursive factorial function
def factorial(n):
    
    # anything multiply by 0 is 0
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = n * factorial(n-1)
    return result

print(factorial(0))
print(factorial(50))

# iterative factorial function
def factorial_2(n):
    result = 1
    for x in range(n):
        result *= x + 1

    return result

print(factorial_2(1000))
