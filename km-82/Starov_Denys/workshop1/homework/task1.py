import re

def num_val_int():

    user_input = input("Enter int number: ")

    if (re.match(r"^\d+$", user_input)):
        return user_input
    else:
        return False

def num_val_float():

    user_input = input("Enter float number: ")

    if (re.match(r"^\d+\.\d+$", user_input)):
        return user_input
    else:
        return False

def inputInt():
    intNum = num_val_int()
    while not intNum:
        print("Error")
        intNum = num_val_int()
    return intNum

def inputFloat():
    floatNum = num_val_float()
    while not floatNum:
        print("Error")
        floatNum = num_val_float()
    return floatNum

if  __name__ == "__main__":
    inputInt()
    inputFloat()
