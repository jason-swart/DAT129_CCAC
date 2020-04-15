"""
JSwart DAT129 Week 7
Peer tutorial exercise on Lambda functions.
These are two different examples of creating the Fibonacci sequence using reduce() and map() functions with lambdas.

To see how the Fibonacci sequence could be run in python normally without lambdas, see python_fibo.py.

"""

from functools import reduce
from pprint import pprint


#Using lambda with the reduce() function imported to create the Fibonacci sequence.
fibonacci = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
	range(n-2), [0, 1])

#Pretty printing the result so all the numbers in a sequence appear neatly instead of a giant blob.
pprint(fibonacci(101))

#This same exercise can be done using the built-in map() function
def fibonacci2(count):
	fiboList = [0, 1]

	any(map(lambda _: fiboList.append(sum(fiboList[-2:])),
		range(2, count)))

	return fiboList[:count]
pprint(fibonacci2(101))