# Swap two variables without using the third variable in Python

def swapVariable(firstNumber, secondNumber):
    secondNumber = secondNumber + firstNumber
    firstNumber = secondNumber - firstNumber
    secondNumber = secondNumber - firstNumber
    print(firstNumber, secondNumber)

swapVariable(4,123)

# Python Program to swap two number using third variable
firstNumber = 4
secondNumber = 123
temporary = secondNumber
secondNumber = firstNumber
firstNumber = temporary
print(firstNumber,secondNumber)
