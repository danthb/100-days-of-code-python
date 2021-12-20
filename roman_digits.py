def giveDigit(position, digit):
    aux = ''
    roman_array = [['I', 'V'], ['X', 'L'], ['C', 'D'], ['M', None]]
    if (digit == '1' or digit == '2' or digit == '3'):
        for i in range(int(digit)):
            aux = aux + roman_array[position][0]
    elif(digit == '4'):
        aux = roman_array[position][0] + roman_array[position][1]
    elif(digit == '5'):
        aux = roman_array[position][1]
    elif (digit == '6' or digit == '7' or digit == '8'):
        aux = roman_array[position][1]
        for i in range(int(digit) - 5):
            aux = aux + roman_array[position][0]
    elif(digit == '9'):
        aux = roman_array[position][0] + roman_array[position+1][0]
    return aux


def solution(n):
    number_string = str(n)
    number_list = []
    number_list[:0] = number_string
    position = len(number_list)
    roman_number = ''
    for i in range(len(number_list)):
        position -= 1
        if(number_list[i] != '0'):
            roman_number = roman_number + giveDigit(position, number_list[i])
    return roman_number


print(solution(4))


""" def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman_string = ''
    for key in sorted(roman_numerals.keys(),reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string """
