emp = []
class Employee():

    def __init__(self):
        self.__id = None
        self.__salary =  None
        self.name = None
        self.age = None

    def employee_data(self):
        global emp
        self.__id = int(input('Enter ID: '))
        self.name = input('Enter name: ')
        self.age = int(input('Enter age: '))
        self.__salary = int(input('Enter salary: '))
        emp.append({'id':self.__id,'name':self.name,'age':self.age,'salary':self.__salary})
        print(f'Employee {self.name} Updated')

    def display(self):
        if len(emp)>0:
            for i in emp:
                print(f'ID: {i['id']}, Name: {i['name']}, Age: {i['age']}, Salary: {i['salary']}')        
        else:
            print('Enter Data First...')

class Manager(Employee):
    def department(self):
        global emp
        if len(emp)>0:
            id = int(input('Enter id to assign dept: '))
            for i in emp:
                print(i['id'])
                if i['id'] == id:
                    dept = input('Enter Department name: ')
                    dict = {'dept':dept}
                    i.update(dict)
            print(f'Department assigned')
        else:
            print('Enter Employee data First...')
    
    def display(self):
        if len(emp)>0:
            id = int(input('Enter id to find Employee: '))
            for i in emp:
                if i['id'] == id:
                    print(f'ID: {i['id']}, Name: {i['name']}, Age: {i['age']}, Salary: {i['salary']}, Department: {i['dept']}')        
        else:
            print('Enter Data First...')

class Developer(Employee):
    def programming_language(self):
        global emp
        if len(emp)>0:
            id = int(input('Enter id to assign programming language: '))
            for i in emp:
                if i['id'] == id:
                    lan = input('Enter Programming language: ')
                    lang = {'lang':lan}
                    i.update(lang)
            print('Programming language Updated')
        else:
            print('Enter Employee data First...')
    
    def display(self):
        if len(emp)>0:
            id = int(input('Enter id to find Employee: '))
            for i in emp:
                if i['id'] == id:
                    print(f'ID: {i['id']}, Name: {i['name']}, Age: {i['age']}, Salary: {i['salary']},Language: {i['lang']}')        
        else:
            print('Enter Data First...')


print()
print('--- Python OOP project: Employee management system ---')

while True:
    print()
    print('Choose an option:')
    print('1. Create Employee')
    print('2. Assign Department')
    print('3. Update programming Languages')
    print('4. Show Details')
    print('5. Exit')
    print()
    choice = int(input('Enter your choice:'))

    match choice:
        case 1:
            e1 = Employee()
            e1.employee_data()
        case 2:
            d1 = Manager()
            d1.department()
        case 3:
            l1 = Developer()
            l1.programming_language()
        case 4:
            print()
            print("Choose Data to Show")
            print('1. Employee')
            print('2. Manager')
            print('3. Developer')
            print()
            choice = int(input('Enter Your choice: '))

            if choice == 1:
                e1.display()
            elif choice == 2:
                d1.display()
            elif choice == 3:
                l1.display()
            else:
                print('Enter valid choice...')
        case 5:
            print()
            print('Exiting the program...')
            break
        case _:
            print('Enter valid choice...')