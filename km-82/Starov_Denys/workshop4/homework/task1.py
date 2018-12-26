import data
from data import dataset

def addCountry(user_num, country, price):
	if user_num in dataset:
		if country in dataset[user_num]:
			user_list = dataset[user_num][country]
			user_list.append(price)
		else:
			dataset[user_num][country] = [price]
	else:
		dataset[user_num] = {country: [price]}

print("Task 1")

addCountry("22-22-2222", "Ukraine", 6345.45)
addCountry("22-22-2222", "Poland", 1324.54)
addCountry("44-44-4444", "Germany", 5363.45)

print(dataset)
