def row_sum_odd_numbers(n):
    num = 0
    i = 1
    lista=[]
    suma = 0
    for i in range(n):
        i += 2
        for j in range(n+1):
            num += 1
            if num % 2 != 0:
                lista.append(num)
    for z in range(-1, -(n+1), -1):
        suma = suma + lista[z]
    return suma

row_sum_odd_numbers(13)
