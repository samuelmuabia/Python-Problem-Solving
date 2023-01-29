# Write a program in Python to check given number is prime or not.

def checkPrime(number):
    isPrime= True
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