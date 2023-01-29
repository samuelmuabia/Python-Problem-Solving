# Write a program in Python to check whether an integer is Armstrong number or not
# What is Armstrong Number?
# It is a number which is equal to the sum of cube of its digits.
# For eg: 153, 370 etc. 1^3 + 5^3 + 3^3 = 153
def checkArmstrong(number):
    numberForLoop = number
    sumOfCube=0
    while numberForLoop:
        firstDigit = numberForLoop%10
        numberForLoop //= 10
        sumOfCube = firstDigit*firstDigit*firstDigit+sumOfCube
    if sumOfCube == number:
        return True

number = 153
if(checkArmstrong(number)):
    print(f"Yes,The number {number} is an Armstrong Number") 
else:
    print(f"No,The number {number} is not an Armstrong Number") 

# Better and Optimized solution for this is usinf str
number = 153
numberToString = str(number)
sumOfCube = 0
for digit in numberToString:
    digitToInteger = int(digit)
    sumOfCube = digitToInteger*digitToInteger*digitToInteger+sumOfCube
if sumOfCube == number:
    print(f"Yes,The number {number} is an Armstrong Number")
else:
    print(f"No,The number {number} is not an Armstrong Number")

# Both solutions have the same time complexity of O(n), where n is the number of digits in the input number, because both solutions iterate through each digit of the input number once.

# Both solutions also have the same space complexity of O(1), because both solutions use only a constant amount of additional memory.

# The reason the second solution is more efficient than the first one is because it avoids the overhead of using the modulus and integer division operations. In the first solution, you are using modulus operator to get the rightmost digit and then you are dividing the number by 10 to remove the rightmost digit. These operations can be computationally expensive and time-consuming, especially for large input numbers. 
