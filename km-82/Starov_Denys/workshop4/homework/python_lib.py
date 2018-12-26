import re

def num_validator():

	user_input = input("Enter user number:\n")

	if (re.match(r"^\d{2}-\d{2}-\d{4}$", user_input)):
		return user_input
	else:
		return False

def country_val():

	user_input = input("Enter name country:\n")

	if (re.match(r"^[A-Z][a-z]{1,5}$", user_input)):
		return user_input
	else:
		return False

def price_val():

	user_input = input("Enter price:\n")

	if (re.match(r"^\d{4}\.\d{2}$", user_input)):
		return user_input
	else:
		return False