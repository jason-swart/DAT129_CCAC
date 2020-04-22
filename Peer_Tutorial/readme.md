### Lambda functions in Python

Lambdas are anonymous functions in Python (meaning they are not named themselves, but a function included in other functions) that have roots in "Lambda Calculus" as invented by Alonzo Church.

Note that since Lambda functions are expressions, they can be named directly. For example, a lambda to add two numbers could be written as:  
addingOne = lambda x: x+1  
addingOne(2)
  
This would return the result as "3". This is the equivalent to otherwise writing the function as:
  
def addingOne(x):  
   return x+1  
This effectively takes simple functions and reduces them to a single line
  
Lambdas can also be combined with other built-in functions such as reduce() or map() to further expand its capabilites to perform equations or sort.
  
Multiple examples of the uses of lambdas in Python can be found in the lambda_practice.py script. Please review that script then try it yourself with the following exercises:
  
Exercise 1) Create a Fibonacci sequence using any length of numbers in the sequence; I used 101 and 501 in my version. My example for this using regular Python functions (for comparison) can be found in python_fibo.py and uses memoization and caching. The lambda version can be found in lambda_exercise.py.
  
Exercise 2) Create a list of dictionaries (I used authors and the number books they've written), be sure to include at least two categories in your dictionaries, and then use lambdas to sort your list by at least one category. My example for this can be found in lambda_exercise2.py.
  
https://docs.python.org/3/reference/expressions.html#lambda

Socratica YouTube Channel https://www.youtube.com/watch?v=25ovCm9jKfA (Highly recommend this channel in general.)
<hr>
# Peer tutorial challenges:  

Added the OOP peer teaching challenge from Taichi.
My own examples of lambdas highlight recursion.
