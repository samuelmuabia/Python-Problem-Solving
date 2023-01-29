# Write a program in Python to check given number is prime or not.

def checkPrime(number):
    isPrime= True
    if number<2:
        isPrime = False
    for i in range(2,number//2):
        if number%i==0:
            isPrime = False
            break
    if isPrime:
        return True
    print(isPrime)
    return False

number = 13
if(checkPrime(number)):
    print(f"The number {number} is a Prime Number")
else:
    print(f"The number {number} is not a Prime Number")

# The time complexity of this solution is O(n/2) where n is the input number. Because for each number in the range of 2 to number//2 you are checking if the input number is divisible by that number.

# The space complexity of this solution is O(1) because you are only using a single variable isPrime to keep track of whether the input number is prime or not.

number = 13

isPrime = True
if number <2 :
    isPrime=False
else:
    for i in range (2,int(number**(0.5))+1):
        if number%i==0:
            isPrime==False
            break
if isPrime :
    print(f"The number {number} is a Prime Number")
else:
    print(f"The number {number} is not a Prime Number")
# Here, the time complexity is O(sqrt(n)) as well.
# The space complexity is still O(1).
# better solution