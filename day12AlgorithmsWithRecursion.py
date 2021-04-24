def sum(list_to_sum):
    if list_to_sum == []: return 0
    return list_to_sum[0] + sum(list_to_sum[1:])


print(sum([1,2,4,6]))

def number_elements(list_1):
    if list_1 == []: return 0
    return 1 + number_elements(list_1[1:])


print(number_elements([1,2,4,6]))



def max_number(list_1):
    if len(list_1) == 2: 
        return list_1[0] if list_1[0] > list_1[1] else list_1[1]
    sub_max = max_number(list_1[1:])
    return list_1[0] if list_1[0]> sub_max else sub_max
print(max_number([1,2,14,6]))



numberList = [0,1,4,6,8,25,67,78,89,100,110,115,116,117,118,119,120]
numberToFind = 25
low = 0
high = len(numberList) - 1

def findNumber(numberList, low, high, numberToFind):
    
    if high >= low:
        mid = (low + high) // 2
        if numberToFind == numberList[mid]: return mid
        elif numberToFind < numberList[mid]: high = mid - 1 
        else: low = mid +1 
        return findNumber(numberList, low, high, numberToFind) 
    else: return -1

print(findNumber(numberList, low, high, numberToFind))



