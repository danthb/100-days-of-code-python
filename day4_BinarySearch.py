# Binary search implementation
numberList = [0,1,4,6,8,25,67,78,89,100,110,115,116,117,118,119,120]
numberToFind = 25
low = 0
high = len(numberList) - 1

def findNumber(numberList, low, high, numberToFind):

    while(low <= high):
        mid = (low + high) // 2
        guess = numberList[mid]
        if ( numberToFind == guess): return mid
        elif (numberToFind < guess): high = mid - 1
        else: low = mid + 1
    return -1
    
print(findNumber(numberList, low, high, numberToFind))