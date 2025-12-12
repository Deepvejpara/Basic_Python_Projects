print('Welcome to the Pattern Genrator and Number Analyzer!')
print()

while True:
    print('Select an option')
    print('1. Generate a pattern')
    print('2. Analyze a Range of Numbers')
    print('3. Exit')

    choice = int(input('Enter your choice: '))

    if choice == 1:
        print()
        n = int(input('Enter the Number of rows for the pattern: '))

        for i in range(1,n+1):
            for j in range(1,i+1):
                print('*',end=" ")
            print()

    elif choice == 2:
        print()
        start = int(input('Enter the Start of the Range: '))
        end = int(input('Enter the End of the Range: '))
        sum = 0
        for i in range(start,end+1):
            if i%2==0:
                print(f"Number {i} is Even")
            else:
                print(f"Number {i} is Odd")
            sum = sum + i
        print(f'Sum of all Number from {start} to {end} is {sum}')

    elif choice == 3:
        print('Exiting the Programm!')
        break
    
    else:
        print('Invalid Choice!')