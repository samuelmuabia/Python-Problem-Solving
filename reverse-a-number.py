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

#problem has time complexity of O(n) and space complexity of O(1)

# recursive method with time complexity of O(n) and space complexity of O(n) so not recommended
# def reverse_int(x):
#     if x < 10:
#         return x
#     else:
#         return int(str(x % 10) + str(reverse_int(x // 10)))

# print(reverse_int(123))

# simple way to solve this

# number = 123123
# numberToString= str(number)
# numberToString= numberToString[::-1]
# print(int(numberToString))
