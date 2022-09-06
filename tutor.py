# string formatting
# list ,creation, iteration , comprehension, slicing, 
# dictionaries, creation , iteration, comprehension, keys, value, items()
# tuples
# sets
# coding challenge
# prices = 7000
# age = 27
# name = "john"
# print(name.endswith('n'))
# #  f string 
# format = f'my friend is {age} years old \n has {prices} in his account'
# purchase = "my friend is {} years old and has {} in his account ".format(age, prices)
# # my friend is 27 years old
# purchase_new = 'my friend is %s years old and has %s in his account ' % (age, prices)
# print(format)
# print(purchase)
# print(purchase_new)
# # name.replace('j', 'b')
# # print(name)
# print(dir(name))
new_list = [3, 4, 6]
extension = [8, 9, 45]
developers = ["john", "james", "peter", "paul", 9, 20, True, False, 78.9]
# print(dir(developers))
# developers.append(new_list)
# developers.extend(extension)
# developers.insert(1, "philip")
# print(developers)
print(len(developers))
# developers[start:stop:step]

first_item = developers[2:-1:2]
print(first_item)
"""
is a list mutable
mutability is the ability to change contents of a data structure after it has been defined

john is a string type 
james is string type
9 is an integer
78.9 is a floating
true and false are booleans
"""