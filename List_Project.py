print('Welcome to Student Management')
print()

students = []
while True:
    print('Choose an option:')
    print('1. Add Student Name')
    print('2. View Students')
    print('3. Update Student')
    print('4. Delete Student')
    print('5. Exit')
    print('='*30)

    choice = int(input('Enter your choice: '))

    match choice:
        case 1:
            print('='*30)
            stu = input('Enter Student Name:')
            students.append(stu)
        case 2:
            if len(students) > 0:
                for student in students:
                    print(student)
            else:
                print('Enter name first...')
        case 3:
            if len(students) > 0:
                print('='*30)
                print('Choose an option: ')
                print()
                print('1. Position Wise Update')
                print('2. Slice Wise Update')
                print('3. Insert Using insert()')
                
                choice = int(input('Enter your choice: '))

                if choice == 1:
                    position = int(input('Enter index Position to Update: '))
                    student = input('Enter Student Name: ')
                    students[position] = student
                    print("Updated Sucessfully!")
                
                elif choice == 2:
                    start = int(input('Enter Starting Index: '))
                    end = int(input('Enter Ending Index: '))
                    for i in range(start,end+1):
                        students[i] = input('Enter new Name: ')
                    print('='*30)
                    print('Updated Sucessfully!')
                    print('='*30)

                elif choice == 3:
                    pos = int(input('Enter position: '))
                    insert = input('Enter Student Name: ')

                    students.insert(pos, insert)
                    print('Updated Sucessfully!')
                    
                else:
                    print('Invalid choice!')
            else:
                print('Enter name first...')        
        case 4:
            if len(students) > 0:
                print('='*30)
                print()
                print('Choose an option')
                print('1. Deleted by Name')
                print('2. Deleted by Position')
                print('3. Deleted all Students')

                choice = int(input('Enter your Choice: '))

                if choice == 1:
                    name = input('Enter Name to Delete: ')

                    students.remove(name)
                    print('Deleted Sucessfully!')
                elif choice == 2:
                    index = int(input('Enter Position to Delete: '))

                    del students[index]

                    print('Deleted Sucessfully!')

                elif choice == 3:

                    del students
                    print('All Students Deleted Sucessfully!')

                else:
                    print('Invalid Choice!')
            else:
                print('Enter name first...')


        case 5: break   
        case _: 
            print('='*30)
            print('Invalid Choice!')
            print('='*30)         