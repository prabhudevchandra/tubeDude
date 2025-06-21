
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))

import math

n = int(input("Enter a number: "))
sq = math.sqrt(n)
lo = math.log(n)
si = math.sin(n)

print(f"Square root: {sq}")
print(f"Logarithm: {lo}")
print(f"Sine: {si}")
