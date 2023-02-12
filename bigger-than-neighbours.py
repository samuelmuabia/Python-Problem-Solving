# Find a peak element which is not smaller than its neighbours
def findPeakElement(listOfArray):
    max = listOfArray[1]
    if listOfArray[len(listOfArray)-1]>listOfArray[len(listOfArray)-2]:
        print (listOfArray[len(listOfArray)])
    for i in range(1,len(listOfArray)-1):
        if listOfArray[i]>max:
            max = listOfArray[i]
        if listOfArray[i]>listOfArray[i-1] and listOfArray[i]>listOfArray[i+1]:
            print (listOfArray[i],end=" ")
    if listOfArray[0]>listOfArray[1]:
        print (listOfArray[0])
   
    if listOfArray[len(listOfArray)-1]>max:
            max = listOfArray[len(listOfArray)-1]
    if max ==listOfArray[1]:
        print(max)
findPeakElement([30, 30,50,30])