# Write a program in Python to find prime factors of a given integer
def primeFactor(number):
    factor=[]
    if number==2:
        factor.append(2)

    while number%2==0:
        factor.append(2)
        number = number//2
    for i in range(3,int(number**0.5)+1,2):
        while number%i==0:
            factor.append(i)
            number=number//i
    if number>2:
        factor.append(number)
    print(factor)

primeFactor(39)

            

