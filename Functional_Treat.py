array = []
def Create():
    global array
    print('Enter 1D Array Elements (Separated by spaces ):')
    arr = input()
    arry = arr.split()
    for i in arry:
        array.append(int(i))
    print('Data has been stored successfully!')


def Summary():
    total = sum(array)
    maximun = max(array)
    minimun = min(array)
    lenth = len(array)
    average = total/lenth
    print()
    print('Data Summary')
    print(f'Total elements: {lenth}')
    print(f'Minimun value: {minimun}')
    print(f'Maximum value: {maximun}')
    print(f'Sum of all values: {total}')
    print(f'Average value: {average:.2f}')

def factorial(n):
    if n <= 0:
        return 1
    elif n == 1:
        return 1
    return n * factorial(n-1)

def lambda_filter(n):
    return list(filter(lambda x:x > n,array))

def sorting():
    print()
    print('Choose soring option:')
    print('1. Ascending')
    print('2. Descending')
    print()
    choice = int(input('Enter Your choice: '))

    if choice == 1:
        array.sort()
        print(array)
    elif choice == 2:
        array.sort(reverse=True)
        print(array)
    else:
        print('Invalid choice...')

def stat():
    sum = 0
    len = 0
    max = array[0]
    min = array[0]

    for i in array:
        sum += i
        len += 1
        if i > max:
            max = i
        if i < min:
            min = i
    mean = sum/len
    return sum,mean,max,min



print('Welcome to Data Analyzer and Transformer Program')
print()
while True:
    print("Main Menu:")
    print('1. Input Data')
    print('2. Display Data Summary (Built-in Functions)')
    print('3. Calculate Factorial (Recursion)')
    print('4. Filter Data by Threshold (Lambda Function)')
    print('5. Sort Data')
    print('6. Display Dataset Statistics (Return Multiple Values)')
    print('7. Exit Program')
    print()
    choice = int(input('Enter Your Choice: '))

    match choice:
        case 1:
            Create()
        case 2:
            Summary()
        case 3:
            print()
            num = int(input('Enter number to calculate its factorial: '))
            print(f"Factorial of {num} is {factorial(num)}")
        case 4:
            print()
            val = int(input("Enter a threshold value to filter out data above this value:\n"))

            result = lambda_filter(val)
            print()
            print(f'Filterd data (values >= {val})')
            print(result)
        case 5:
            sorting()
        case 6:
            sum,mean,max,min=stat()
            print()
            print('Dataset Statistics:')
            print(f'- Maximum value: {max}')
            print(f'- Minimum value: {min}')
            print(f'- Sum of all values: {sum}')
            print(f'- Average value: {mean:.2f}')
            print()
        case 7:
            break
        case _:
            print('Invalid choice...')