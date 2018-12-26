from data import dataset
from task1 import *

def recPrice(user_num, country_list, money = 0):

    if country_list == []:
        return money

    current_money = dataset[user_num][country_list[0]]
    money = sum(current_money)

    return recPrice(user_num, country_list[1:], money)

def recByUser(user_nums = list(dataset.keys()), result_dict = dict()):
    
    if user_nums == []:
        return result_dict

    user_num = user_nums[0]
    country_list = list(dataset[user_num].keys())
    allMoney = recPrice(user_num, country_list)
    result_dict[user_num] = allMoney

    return recByUser(user_nums[1:], result_dict)

result = recByUser()
print(result)