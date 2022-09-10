# string formatting
"""
we have 4 major types of data structures in python
data structures are ways our datas can be order or sorted depending on 
list
dictionaries
tuples 
sets
key ->  value
boy -> a boy is  a male 

is a list mutable or immutable

"""
variable = "laptop" #lapto
new_list = [5, 6, 7]
# print(dir(variable))
new_list.append(100)
# print(new_list)
variables = variable + "s"


# list, dictionary 0, 1, strings
#  dictionaries in python clear(), copy()
"""
e_commerce = {"laptop":500, "phone": 120, (9, 7, 8): "class", "cooker": 800,"false": {"large": 70, "small": 50}, "orders":[23, 67, 89]}
e_commerce_copy = e_commerce.copy()
print(e_commerce.get("laptop"))
print(e_commerce["false"])
e_commerce["footballer"] = ["messi", "de bruyne", "mane"]

print(e_commerce)
"""
class MyDict:
    def __init__(self, dict):
        self.diction = dict

    def gets(self, key, *args):
        """OOP error handling"""
        try:
            self.diction[key]
        except KeyError:
            return args[0] if args else None
        else:
            return self.diction[key]

new_dict = MyDict({"key":"value"})
print(new_dict.gets("ke", ))

#  getting , adding , iterating(looping), deleting, 
# print(dir(e_commerce))
# school = dict()
# print(dir(e_commerce))
# print(e_commerce)
# print(school)
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
# new_list = [3, 4, 6]
# extension = [8, 9, 45]
# developers = ["john", "james", "peter", "paul", 9, 20, True, False, 78.9]
# print(dir(developers))
# developers.append(new_list)
# developers.extend(extension)
# developers.insert(1, "philip")
# print(developers)
# print(len(developers))
# [start:stop:step]

second_list = [ 8, 9, 4, 78, 99,True, 100, 23]
multiple_list = []

for item in second_list:
    if item > 10:
        multiple_list.append(item)
    else:
        pass
# print(multiple_list)

# list comprehension 
new_list = [num  for num in second_list if num >  10 ]
print(new_list)

# indexing = [1, 2, 3, 4, 5, 6, 7 ,8] 
# print(second_list[0])
# print(second_list[1])
# [start:stop:step]
# print(len(second_list))
# print(second_list[start:stop:step])
"""
print(indexing[:2]) 
print(indexing[2:])
print(indexing[::-2])
#  whenever the a single colon is before a number then we are specifying the stopping index
#  whenever the a single colon is after a number then we are specifying the starting index 
print(indexing[2:-1:1])
['talabi', 'dare', 9]
# acccesing items of a list
# talabi 0
# sani 1
#  dare 2

is a list mutable
mutability is the ability to change contents of a data structure after it has been defined

john is a string type 
james is string type
9 is an integer
78.9 is a floating
true and false are booleans
"""