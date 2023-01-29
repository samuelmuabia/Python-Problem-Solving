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
    