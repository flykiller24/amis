stud_list = [
		{
			'name': 'Bob',
			'age': 18,
			'marks': {
				'Math': 87,
				'English': 95
				}
		},
		{
			'name': 'Boba',
			'age': 21,
			'marks': {
				'Python': 78,
				'Math': 89
				}
		}
]

maxAge = 0

def max_age_f(stud_list, len_stud_list, max_age):
	global maxAge

	if len(stud_list) == len_stud_list:
		return max_age
	elif len_stud_list == 0:
		max_age = int(stud_list[0]['age'])
		maxAge = max_age
		max_age_f(stud_list, len_stud_list+1, max_age)

	if len(stud_list[len_stud_list]['age']) > max_age:
		max_age = stud_list[len_stud_list]['age']
		maxAge = max_age
	max_age_f(stud_list, len_stud_list+1, maxAge)

	return maxAge

def addMark(stud_list, name, subject, mark):
	for elm in range(len(stud_list)):
		if stud_list[elm]['name'] == name1:
			stud_list[elm]['marks'][subject] = mark

def getName(stud_list):
	name_list = []
	for elm in range(len(stud_list)):
		name_list.append(stud_list[elm]['name'])
	return name_list

name1 = str(input("Enter student name: "))
subject1 = str(input("Enter subject name: "))
mark1 = str(input("Enter mark: "))

addMark(stud_list, name1, subject1, mark1)
print(getName(stud_list))
print(max_age_f(stud_list, 0, 0))
