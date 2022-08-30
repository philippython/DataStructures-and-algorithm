# from random import random
# from webbrowser import get
# from data import data 
# """
# Question 1a.
#     using data from data.py

# """

# def statistics(key, dictionary):
#     # using key parameter to get data to be calculated
    
#     all_data = dictionary[:key]
#     sum = 0
#     actcost_list = []
#     for data in all_data:
#         sum += data["act_cost"]
#         actcost_list.append(data["act_cost"])

    
#     mean = sum // len(all_data)

#     print(len(actcost_list), actcost_list)
#     # if len(actcost_list) % 2 :
#     #     nth = len(actcost_list) / 2 
#     #     median = nth + 1 // 2
#     # else :
 

#     median = len(actcost_list) % 2

# rand_list = ["I>E", "M>I", "A>M", "D>A", "E>N"]
# random_dict = { n[0]:n[-1] for n in rand_list}
# print(random_dict)
# def getword(random_dict):
#     new = []
#     for k, v in random_dict.items() :
#         if k not in list(random_dict.values()):
#             new.append(k)
#             random_dict[k] = k
# while len(new) < len(rand_list):
#     getword(random_dict)
#     if len(new) < len(rand_list):
#         print(new)
#         break

# getword(random_dict)
# # statistics(8, data)


# def rgb(r, g, b):
#     round = lambda x: min(255, max(x, 0))
#     return ("{:02X}" * 3).format(round(r), round(g), round(b))


# name = "Alice"

# "Hello %s" % name
# "Hello {0}".format(name)
# f"Hello {name}"

# # Using named arguments:
# "Hello %(kwarg)s" % {'kwarg': name}
# "Hello {kwarg}".format(kwarg=name)
# f"Hello {name}"

class Developer:        
    age = 18
    def __init__(self, name, exp):
        self.name = name
        self.exp = exp

    
    def set_base_info(self, lang, company):
        self.__company = company
        self.__lang = lang

    def get_base_info(self):
        return "I am a %s developer @%s" % (self.__lang, self.__company)

    @classmethod
    def express(cls, name):
        return cls(name, len(name))

    def __str__(self) -> str:
        return self.name

class Rank(Developer):
    def __init__(self, name, age):
        super().__init__(name, age)

# dev = Developer("philip", 0)
# dev.set_base_info("python", "apple")
# dev.age = 20
new_dev = Developer.express("philip")
print(new_dev)

