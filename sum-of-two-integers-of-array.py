
def numberCounter(arrayOfNumbers):
    count ={}
    for number in arrayOfNumbers:
        if number in count:
            count[number]+=1
        else:
            count[number]=1
    return count
def sumOfTwo(arrayOfNumbers,targetSum):
    if len(arrayOfNumbers)>2:
        listOfNumberCount= numberCounter(arrayOfNumbers)
        for num,items in listOfNumberCount.items():
            firstNumber = num
            secondNumber = targetSum - firstNumber
            try:
                listOfNumberCount[secondNumber]
                return [firstNumber,secondNumber]
            except:
                pass
            print(num,"->",items)
    elif len(arrayOfNumbers)==1:
        if arrayOfNumbers[0]==targetSum:
            return [targetSum]
    else:
        if targetSum == arrayOfNumbers[0]+arrayOfNumbers[1]:
            return [arrayOfNumbers[0],arrayOfNumbers[1]]




arrayOfNumbers=[1,-2,4,-5,6]
print(f"The target sum can be obtain from summation of this two numbers : {sumOfTwo(arrayOfNumbers,-7)}")