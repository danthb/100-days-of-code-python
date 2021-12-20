def is_prime(number):
    countDivisor = 0
    incrementDivisor = 0
    if number >= -1 and number <=1:
        return False
    while  (incrementDivisor <= number) :
        incrementDivisor += 1
        if number % incrementDivisor==0:
            countDivisor +=1
        if countDivisor == 3:
            break
            
    if countDivisor == 2:
        return True
    else:
        return False

