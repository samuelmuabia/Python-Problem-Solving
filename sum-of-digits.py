# Write a program in Python to find sum of digits of a number using recursion?

def sumOfDigits(number):
    if number==0:
        return 0
    else:
        return number%10+sumOfDigits(number//10)
print(sumOfDigits(12345))