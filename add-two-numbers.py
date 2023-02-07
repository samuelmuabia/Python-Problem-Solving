# a program to add two numbers without using + operator
def addTwo(firstNumber,secondNumber):
    while secondNumber!=0:
        temp = firstNumber & secondNumber
        print("temp->",temp)
        firstNumber= firstNumber ^ secondNumber
        print("firstNumber -> ",firstNumber)
        secondNumber = temp<< 1
        print("secondNumber -> ",secondNumber)
    print(firstNumber)

addTwo(25,10)

# nedd to learn about ^ & << operator moreeeeeee