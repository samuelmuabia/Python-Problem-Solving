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