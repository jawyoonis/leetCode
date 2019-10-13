def smallest_difference(arrOne, arrTwo):
    arrOne.sort()
    arrTwo.sort()
    indexOne, indexTwo=0,0
    smallest=float("inf")
    current=float("inf")
    smallestPair=[]

    while indexOne< len(arrOne) and indexTwo< len(arrTwo):
        firstNum= arrOne[indexOne]
        secondNum= arrTwo[indexTwo]
        if firstNum < secondNum:
            current= secondNum-firstNum 
            indexOne+=1
        elif firstNum > secondNum:
            current= firstNum-secondNum
            indexTwo+=1
        else:
            return [firstNum, secondNum]
        if smallest > current:
            current= smallest 
            smallestPiar=[firstNum, secondNum]
    return smallestPiar







one=[1,3,4,5,7]

two=[9,10,12,2]


print(smallest_difference(one, two))
