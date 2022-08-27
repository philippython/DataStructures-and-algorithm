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



statistics(8, data)