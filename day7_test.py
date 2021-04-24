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



def pig_latin(text):
  say = ""
  new_sentence = []
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    new_string = word[1:] + word[0] +"ay "
    new_sentence.append(new_string)
    say = "".join(new_sentence)
    # Turn the list back into a phrase
  return say
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

def octal_to_string(octal):
 result = ""
 value_letters = [(4,"r"),(2,"w"),(1,"x")]
 # Iterate over each of the digits in octal
 for i in [int(n) for n in str(octal)]:
    # Check for each of the permissions values
    for value, letter in value_letters:
        if i >= value:
            result += letter
            i -= value
        else:
            result += '-'
 return result
    
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------


def group_list(group, users):
  members = ', '.join(users)
  return "{}: {}".format(group, members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


def guest_list(guests):
	for guest in guests:
		name = guest[0]
		age = guest[1]
		career = guest[2]
		print("{} is {} years old and works as {}".format(name, age, career))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""