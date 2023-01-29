# Suppose if someone gives input 123 and our program should give output 321.
def reverseAInteger(number):
    reversedNumber = 0
    while number:
        remainder = number%10
        number= number//10
        if remainder !=0:
            reversedNumber = remainder + reversedNumber*10
    return reversedNumber



reversedNumber=reverseAInteger(326456425)
print(reversedNumber)