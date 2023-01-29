# Write a program in Python to print the Fibonacci series using iterative method.

def fibonacciSeries(number):
    if number <=0:
        print("Invalid Input")
    elif number==2:
        print(0,end=" ")
        print(1,end=" ")
        return
    elif number==1:
        print(0,end=" ")
        return
    elif number>2:
        firstNumber =0
        secondNumber = 1
        print(firstNumber,end=" ")
        print(secondNumber,end=" ")
        for i in range (3,number+1):
            thirdNumber = firstNumber+secondNumber
            firstNumber = secondNumber
            secondNumber = thirdNumber
            print(thirdNumber,end=" ")

fibonacciSeries(7)

# The time complexity of this code is O(n) , as it goes through a loop n times.
# The space complexity is O(1) as it uses only a constant amount of memory to store the variables 'firstNumber', 'secondNumber' and 'thirdNumber'.
# Write a program in Python to print the Fibonacci series using recursive method.



def fibonacciSeries(number,fibonacciList=[]):
    
    if number<=0:
        print("Invalid Input")
    elif number ==1:
        fibonacciList.append(0)
        return fibonacciList
    elif number==2:
        fibonacciList.append(0)
        fibonacciList.append(1)
        return fibonacciList
    elif number>2:
        fibonacciSeries(number-1,fibonacciList)
        fibonacciList.append(fibonacciList[-1]+fibonacciList[-2])
        return fibonacciList
print(fibonacciSeries(7))

# The time complexity of this solution is O(n) and space complexity is O(n) as you are creating a list with n values. This solution is better than the previous one as it is a more elegant solution which uses less memory and more efficient in terms of space.



#better solution
import math

def fibonacci_series_formula(number):
    for n in range(number):
        fib = int(((1 + math.sqrt(5)) ** n - (1 - math.sqrt(5)) ** n) / (2 ** n * math.sqrt(5)))
        print(fib, end=" ")

fibonacci_series_formula(7)

# This method will give you the same output as the previous methods, but it will be faster than the recursive method, and it's time complexity will be O(n) and space complexity will be O(1).