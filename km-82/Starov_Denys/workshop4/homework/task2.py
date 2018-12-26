from data import dataset

from python_lib import num_validator
from python_lib import country_val
from python_lib import price_val

from task1 import addCountry

def addUserCountry():
        user_num = num_validator()
        while not user_num:
                print("Try again")
                user_num = num_validator()

        country = country_val()
        while not country:
                print("Try again")
                country = country_val()

        price = price_val()
        while not price:
                print("Try again")
                price = price_val()


        addCountry(user_num, country, price)

addUserCountry()
print(dataset)
