import datetime
import os
class FileOperator:
    def __init__(self):
        self.file = "journal.txt"

    def new_entry(self):
        book = open(self.file,'a')
        entry = input('Enter Your journal entry:\n')
        now = datetime.datetime.now()
        format = f"[ {now.strftime('%d/%m/%Y %H:%M:%S')} ]"
        book.write(format)
        book.write("\n")
        book.write(f"{entry} \n")
        book.write('\n')
        print()
        print('Entry added succesfully...')
        book.close()

    def read_entry(self):
        book = open(self.file,'r')
        contant = book.read()
        if len(contant)>0:
            print('Your journal entries:')
            print('='*30)
            print(contant)
            book.close()
        else :
            print('Enter data first....')
    
    def find_entry(self):
        with open(self.file,'r') as file:
            entry = file.readlines()
            if len(entry)>0:
                found = 0
                print()
                find = input('Enter key word to find:')
                for i in entry:
                    sentance = i.split('.')
                    for j in sentance:
                        word = j.split(' ')
                        for k in word:
                            if find == k:
                                print('Entry found:')
                                print(i)
                                found = 1
                                break
                if found == 0:
                    print('No Entry was found...')
            else :
                print('Enter data first....')
            
    def delete_entry(self):
        with open(self.file,'r') as file:
            contant = file.read()
            if len(contant) > 0:
                print('Entries deleted...')
            else:
                print('No entries to delete...')
        with open(self.file,'w') as file:
            
            file.truncate(0)
        
    
    

            
     

b1 = FileOperator()
print('Welcome to journal book')

while True:
    print()
    print('Choose an option:')
    print('1. Add Entry')
    print('2. Show all Entry')
    print('3. Find Sepcific Entry')
    print('4. Delete all Entries')
    print('5. Exit')

    print()
    try:
        choice = int(input('Enter your Choice: '))
    except:
        print('Enter integer number only')
        continue
    match choice:
        case 1:
            b1.new_entry()
        case 2:
            b1.read_entry()
        case 3:
            b1.find_entry()
        case 4:
            print()
            choice = input('Are you sure? (yes/no): ')
                        
            if choice.lower() == 'yes':
                b1.delete_entry()
            elif choice.lower() == 'no':
                print('Returning...')
                continue
            else:
                print('Invalid choice...')
        case 5:
            print('Exiting Program...')
            break
        case _:
            print('Invalid choice...')