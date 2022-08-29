from random import random
from webbrowser import get
from data import data 
"""
Question 1a.
    using data from data.py

"""

def statistics(key, dictionary):
    # using key parameter to get data to be calculated
    
    all_data = dictionary[:key]
    sum = 0
    actcost_list = []
    for data in all_data:
        sum += data["act_cost"]
        actcost_list.append(data["act_cost"])

    
    mean = sum // len(all_data)

    print(len(actcost_list), actcost_list)
    # if len(actcost_list) % 2 :
    #     nth = len(actcost_list) / 2 
    #     median = nth + 1 // 2
    # else :
 

    median = len(actcost_list) % 2

rand_list = ["I>E", "M>I", "A>M", "D>A", "E>N"]
random_dict = { n[0]:n[-1] for n in rand_list}
print(random_dict)
def getword(random_dict):
    new = []
    for k, v in random_dict.items() :
        if k not in list(random_dict.values()):
            new.append(k)
            random_dict[k] = k
while len(new) < len(rand_list):
    getword(random_dict)
    if len(new) < len(rand_list):
        print(new)
        break

getword(random_dict)
# statistics(8, data)




