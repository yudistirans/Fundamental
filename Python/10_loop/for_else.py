employee_name = 'John'

marks = {'James': 20, 'Jules': 35, 'Arthur': 27}

for student in marks:
    if student == employee_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')