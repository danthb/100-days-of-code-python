# Binary search implementation
numberList = [0,1,4,6,8,25,67,78,89,100,110,115,116,117,118,119,120, 600, 120000000, 34555555555]
numberToFind = 4


def findNumber(numberList, numberToFind): #camelCase
    low = 0
    high = len(numberList) - 1
    while(low <= high):
        mid = (low + high) // 2
        guess = numberList[mid]
        if ( numberToFind == guess): return mid
        elif (numberToFind < guess): high = mid - 1
        else: low = mid + 1
    return None
    
print(findNumber(numberList, numberToFind))