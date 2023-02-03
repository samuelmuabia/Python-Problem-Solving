


def checkBinary(number):
    isBinary=False
    remainingNumber=number
    while remainingNumber >0:
        remainder = remainingNumber % 10
        remainingNumber=remainingNumber//10
        # print (remainder)
        if remainder == 0 or remainder == 1 :
            isBinary = True
        else:
            isBinary = False
            break
    return isBinary

number = 10210
if checkBinary(number):
    print(f"{number} is a binary number.")
else :
    print(f"{number} is not a binary number.")


# The time complexity of this code is O(log n), where n is the value of the input number. The while loop runs as many times as the number of digits in the input number. So, for a number n, the loop runs log n times, making the time complexity O(log n).

def checkBinary(number):
    numberToString = str(number)
    for digit in numberToString:
        if digit != "0" and digit != "1" :
            return False
            break
    return True
number = 10120
if checkBinary(number):
    print(f"{number} is a binary number.")
else :
    print(f"{number} is not a binary number.")            
        