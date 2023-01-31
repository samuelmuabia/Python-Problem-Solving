
def numberCounter(arrayOfNumbers):
    count ={}
    for number in arrayOfNumbers:
        if number in count:
            count[number]+=1
        else:
            count[number]=1
    return count
def sumOfTwo(arrayOfNumbers,targetSum):
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




arrayOfNumbers=[1,-2,4,-5,6]
print(sumOfTwo(arrayOfNumbers,-7))