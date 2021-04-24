wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}

for ext, color in wardrobe.items():
	for color_ind in color :
		print("{} {}".format(color_ind, ext))


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




def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for i,user in enumerate(users):
			if user not in user_groups:
			# Now add the group to the the list of
				user_groups[user] = []
			user_groups[user].append(group)
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

def email_list(domains):
	emails = []
	for group,users in domains.items():
	  for user in users:
	    emails.append(user + "@"+group)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for cost in basket.values():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += cost
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
print(wardrobe.update(new_items))