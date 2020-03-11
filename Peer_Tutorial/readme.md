Lambda functions in Python
Lambdas are anonymous functions in Python (meaning they are not named themselves, but a function included in other functions*) that have roots in "Lambda Calculus" as invented by Alonzo Church.

*Note that since Lambda functions are expressions, they can be named directly. For example, a lambda to add two numbers could be written as:
addingOne = lambda x: x+1
addingOne(2)

This would return the result as "3". This is the equivalent to otherwise writing the function as:

def addingOne(x):
   return x+1
This effectively takes simple functions and reduces them to a single line
