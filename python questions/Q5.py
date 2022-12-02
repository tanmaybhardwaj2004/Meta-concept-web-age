# Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact
 
num = int(input())
print("Factorial of",num,"is",factorial(num))