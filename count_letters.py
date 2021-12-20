file_counts = {"jpg":10 ,"txt":14}
for  extension in file_counts:
    print(extension)

for ext, amount in file_counts.items():
    print("There are {}  of {}".format(amount, ext))

print(file_counts.keys())
print(file_counts.values())


def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


print(count_letters("aaaaa"))