"""
JSwart DAT129 Week 7

Peer tutorial exercise using python without lambdas.
This is written using regular python functions, but it does highlight caching and memoization 
to reduce the memory usage and increase the speed at which the script runs.

At the current range of numbers in the sequence, this script runs in roughly 0.1s, and while using 
a range of 501 numbers the runtime took 0.5s.

"""

#fibonacci program to highlight caching and memoization

fibonacci_cache = {}

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
        
    fibonacci_cache[n] = value
    return value

for n in range(1,101):
    print(n, ":", fibonacci(n))