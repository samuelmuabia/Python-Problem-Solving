# Find a peak element which is not smaller than its neighbours
def findPeakElement(listOfArray):
    for i in range(1,len(listOfArray)-1):
        if listOfArray[i]>listOfArray[i-1] and listOfArray[i]>listOfArray[i+1]:
            print (listOfArray[i],end=" ")


findPeakElement([10, 20, 15, 2, 23, 90, 67])