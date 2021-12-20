def valid_parentheses(string):
    arr = []
    arr[:0] = string
    counter_open = 0
    counter_close = 0
    for i in range(len(arr)):
        if(arr[i] == "("):
            counter_open += 1
            if (counter_close > counter_open):
                return False
        elif(arr[i] == ")"):
            counter_close += 1
            if(counter_close > counter_open):
                return False
    if(counter_open != counter_close):
        return False
    if(counter_open == counter_close):
        return True


print(valid_parentheses("  ("))

""" test.assert_equals(valid_parentheses("  ("),False)
test.assert_equals(valid_parentheses(")test"),False)
test.assert_equals(valid_parentheses(""),True)
test.assert_equals(valid_parentheses("hi())("),False)
test.assert_equals(valid_parentheses("hi(hi)()"),True) """
