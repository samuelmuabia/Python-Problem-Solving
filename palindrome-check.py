# Write a program in Python to check whether a number is palindrome or not using iterative method.it can be done in multiple ways.

# using mathematical Operation
number = 121
numberForLoop = number
reversedNumber = 0
while numberForLoop:
    reversedNumber = numberForLoop%10 + reversedNumber*10
    numberForLoop //=10
if reversedNumber==number:
    print(f"The Number {number} is a palindrome")
else :
    print(f"The Number {number} is not a palindrome")

# using string

number = 1223221
numberToString = str(number)
newNumber = ''
for digit in range(len(numberToString)):
    newNumber = numberToString[digit]+newNumber
if int(newNumber)==number:
    print(f"The Number {number} is a palindrome")
else :
    print(f"The Number {number} is not a palindrome")

# another way to reverse

numberToString = numberToString[::-1]
if int(newNumber)==number:
    print(f"The Number {number} is a palindrome")
else :
    print(f"The Number {number} is not a palindrome")


# Using Recursive Method
def reverse(number):
    if number<10:
        return number
    else:
        return int(str(number%10) + str(reverse(number//10)))

def isPalindrome(number):
    reversedNumber = reverse(number)
    if reversedNumber==number:
        return True
    else:
        return False
number = 121
if isPalindrome(number):
    print(f"The Number {number} is a palindrome")
else :
    print(f"The Number {number} is not a palindrome")
