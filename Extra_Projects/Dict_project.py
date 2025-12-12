students = []

print()
print('Welcome to student library...')
while True:
    print()
    print('Choose an option...')
    print('='*30)
    print('1. Add a student')
    print('2. View a student details')
    print('3. View all student details')
    print('4. Update a students')
    print('5. Delete a student')
    print('6. Delete all students')
    print('0. Exit')
    print('='*30)

    choice = int(input('Enter your choice: '))

    match choice:
        case 1:
            id = int(input('Enter student id: '))
            for stu in students:
                if stu['id'] == id:
                    print('Id already exist..')
                    break
            else:
                name = input('Enter student name: ')
                age = int(input('Enter student age: '))
                city = input('Enter city name: ')

                student = {"id":id,"name":name,"age":age,"city":city}
                students.append(student)
        case 2:pass
        case 3:
            for stu in students:
                print('='*45)
                print(f'ID ->{stu['id']}, Name -> {stu['name']}, Age -> {stu['age']}, City -> {stu['city']}')
                print('='*45)
        case 4:pass
        case 5:pass
        case 6:pass
        case 0: 
            print()
            print('Exiting library...')
            print()
            break
        case _:
            print()
            print('Invalid choice...')