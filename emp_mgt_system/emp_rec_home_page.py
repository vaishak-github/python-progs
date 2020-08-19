from insert_record import *
from update_record import Update


def core():
    i = 0
    dicts = {}
    while i < 100000:

        print("Enter 1 :to insert a record \n"
              "Enter 2 :to update a record \n"
              "Enter 3 :to delete a record \n"
              "Enter 4:to search a record \n"
              "Enter 5 :to list records \n"
              "Enter 6 : to exit ")
        choice = int(input())
        if choice == 1:
            name = str(input("Enter name of emp:"))
            emp_id = int(input("Enter id of emp"))
            email = str(input("Enter the email id"))
            date_entry = input('Enter a date in YYYY/MM/DD format')
            print(dicts)
            a = Insert(name,emp_id,email,date_entry)
            dicts[i]=a
            print(dicts)
        if choice ==2:
            name = str(input("Enter name of emp:"))
            emp_id = int(input("Enter id of emp"))
            u=Update(name,emp_id,dicts)



        print("Do you wish to continue (Y/N")
        wish = input()
        if wish == 'N' or wish == 'n':
            break
        i = i + 1
        print(i)


core()
