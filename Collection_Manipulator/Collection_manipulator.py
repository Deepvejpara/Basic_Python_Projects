print()
print('Welcome to Student data Organizer!')

students = []
subjects = set()
birthdate = ()
while True:
    print()
    print('Select an option')
    print('1. Add Student')
    print('2. Display all Students')
    print('3. Update Student Information')
    print('4. Delete Student')
    print('5. Display Subjects Offred')
    print('6. Exit')

    choice = int(input('Enter Your choice: '))

    match choice:
        case 1:
            print("="*30)
            id = int(input('Enter Student ID: '))
            for stu in students:
                if stu['id'] == id:
                    print('ID already Exist..')
                    break
            else:
                name = input('Enter Name: ')
                age = int(input('Enter Age: '))
                grade = input('Enter Grade: ')
                dob = input('Enter Birth Date(YYYY-MM-DD): ')
                subject = input('Enter Subjects (Comma-separated): ')
                print('='*30)

                student = {'id':id,'name':name,'age':age,'grade':grade}
                birthdate = (id,dob)
                sub = subject.split(',')
                subjects.update(sub)
                students.append(student)
        case 2:
                if len(students)>0:
                    for stu in students:
                        print()
                        print('='*30)
                        print(f'Student ID: {stu['id']},\nName: {stu['name']}, \nAge: {stu['age']}, \nGrade: {stu['grade']},')
                        
                    else:
                        
                        print(f'Subjects: {subjects}')
                        print('='*30)
                else:
                    print('Enter Student data first...')
        case 3:
            if len(students)>0:
                print()
                print('Choose an option to Update')
                print()
                print('1. Only Name')
                print('2. Name,Age')
                print('3. only Grade')
                print('4. Add Subject')
                print('='*30)
                choice = int(input('Enter your Choice: '))
                print()
                if choice == 1:
                    id = int(input('Enter Student ID to Update Info: '))

                    for stu in students:
                        if stu['id'] == id:
                            name = input('Enter new Name: ')
                            stu['name'] = name
                    else:
                        print('Updated Successfully...')
                elif choice == 2:        
                    id = int(input('Enter Student ID to Update Info: '))

                    for stu in students:
                        if stu['id'] == id:
                            name = input('Enter new Name: ')
                            age = int(input('Enter new Age: '))
                            dob = input('Enter Birthdate(YYYY-MM-DD): ')

                            stu['name'] = name
                            stu['age'] = age
                            stu['dob'] = dob
                    else:
                        print('Updated Successfully...')
                elif choice == 3:
                    id = int(input('Enter Student ID to Update Info: '))

                    for stu in students:
                        if stu['id'] == id:
                            grade = input('Enter new Grade: ')
                            stu['grade'] = grade
                    else:
                        print('Updated Successfully...')
                
                    birthdate
                elif choice == 4:
                    sub = input('Enter Subject: ')

                    subjects.update([sub])
                else:
                    print('Invalid Choice...')
            else:
                print('Enter Student first...')
        case 4:
            if len(students)>0:
                confirm = input('Are you Sure you want to delete(y/n): ')
                if confirm.lower() == 'y':
                    id = int(input('Enter Student ID to Delete: '))

                    for stu in students:
                        if stu['id'] == id:
                            students.remove(stu)
                    else:
                        print('='*30)
                        print('Student Removed Sucessfully...')
                        print('='*30)
                elif confirm.lower() == 'n':
                    continue
                else:
                    print('Enter Valid choice...')
            
            else:
                print('Enter Student first...')

        case 5:
            if len(subjects) > 0:
                
                
                print()
                print('='*30)
                print('All Subjects: ')
                for i in subjects:
                    print(i)
                print('='*30)
            else:
                print('Enter subjects first...')

        case 6:
            print()
            print('Exiting The Programm...')
            print()
            break
        case _: 
            print("="*30)
            print('Invalid Choice..')
            print("="*30)