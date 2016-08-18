"""
A program for grade collection and statistics 
"""

from  statistics import mean as m 

admins = {'Python':'Pass123@', 'Sadie':'Pass2'}

studentDict = {'Jess': [78, 88, 93],
					'Sam': [99, 90, 63]
					}

def enterGrades():
	nameToEnter = input('Student Name: ')
	gradeToEnter = input('Grade: ')

	if nameToEnter in studentDict:
		print('Adding Grade...')
		studentDict[nameToEnter].append(gradeToEnter)
	else:
		print('Student does not exist! ')
		answer = input('Would you like to add the student? [Y/N]')
		if answer.upper() == 'Y':
			studentDict[nameToEnter] = [int(gradeToEnter)]
			print(studentDict)
		elif answer.upper() == 'N':
			main()
		else:
			print('Invalid input')
	
	
def removeStudent():
	nameToRemove = input('What student do you want to remove?: ')
	if nameToRemove in studentDict:
		print('removing studnent...')
		del studentDict[nameToRemove]


def studentAVGS():
	for eachStudent in studentDict:
		gradeList = studentDict[eachStudent]
		avgGrade = m(gradeList)
		
		print(eachStudent, ' has an average grade of ', avgGrade)

		
def main():
	print("""
	Welcome to Grade Central
	
	[1] - Enter Grades
	[2] - Remove Student
	[3] - Student Average Grade
	[4] - Exit
	""")
	
	action = input('Welcome! What would you like to do today? (Enter a number) ')
	
	if action == '1' :
		enterGrades()
	elif action == '2':
		removeStudent()
	elif action == '3':
		studentAVGS()
	elif action == '4':
		exit()
	else:
		print('Not a valid choice, try again')

		
		
login = input('Username: ')
passw = input('Password: ')

if login in admins and admins[login] == passw:
	print('Welcome,' , login)
	while True:
		main()
else:
	print('Invalid Credentials')