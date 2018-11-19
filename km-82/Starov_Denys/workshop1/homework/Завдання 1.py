print("Введіть слова")

a = input()
b = input()
c = input()
d = input()
e = input()

# Дані вводяться в список
l = []
l.append(a)
l.append(b)
l.append(c)
l.append(d)
l.append(e)
print(l)

# Виводить список зі словами довжиною більше 3
result = []
for i in l:
    if len(i)>3:
        result.append(i)
print(result)
