# Write a program in Python to find sum of digits of a number using recursion?


# using recursion
def sumOfDigits(number):
    if number==0:
        return 0
    else:
        return number%10+sumOfDigits(number//10)
print(sumOfDigits(12345))

#using loop

number = 12345
sum = 0
while number>0:
    sum = sum + number%10
    number = number//10
print (sum) 

# learning 
# The time complexity of the recursive implementation is O(log(n)), where n is the number of digits in the input number. This is because, in each recursive call, the number of digits in the input number is reduced by a factor of 10, and so the total number of calls is proportional to log(n).

# The time complexity of the loop-based implementation is also O(log(n)), because it has a similar structure to the recursive implementation. In each iteration, the number of digits in the input number is reduced by a factor of 10, and so the total number of iterations is proportional to log(n).

# The space complexity of the recursive implementation is O(log(n)), because in each recursive call, a new function call is added to the call stack, and so the total memory usage is proportional to log(n).

# The space complexity of the loop-based implementation is O(1), because it uses a single variable sum to store the intermediate results, and so the total memory usage is constant, regardless of the size of the input number.

# In conclusion, both implementations have the same time complexity of O(log(n)), but the loop-based implementation has a lower space complexity of O(1), compared to the recursive implementation's space complexity of O(log(n)).