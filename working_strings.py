winners = ["Ashley","Dylan","Reese"]
for index,person in enumerate(winners):
    print("{} - {}".format(index + 1, person))


contact = [("Alex Condrado","alexcondrado@gmail.com"),("Juan Condrado","juanondrado@gmail.com"),("Juan Condrado","juanondrado@gmail.com")]
def get_contact(contact_book):
    for name, email in contact_book:
        print("{0} <{1}>".format(name, email))

get_contact(contact)

def odd_numbers(n):
	return [x for x in range(1,n+1) if x%2!=0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []


filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_extension = ".h"
newfilenames = []
for index,filename in enumerate(filenames):
    if filename.endswith(".hpp"):
        i = filename.find(".hpp")
        new_filename = filename[:i] + new_extension
        newfilenames.insert(index, new_filename)
    else:
        newfilenames.insert(index, filename)

print(newfilenames) 