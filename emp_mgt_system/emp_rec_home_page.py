import datetime
from list_record import *
from delete_record import *
from insert_record import *
from search_record import *
from update_record import *

print("           Welcome to EMS             ")
def switch_demo(argument):

    switcher = {
        1: Insert,
        2: update,
        3: delete,
        4: search,
        5: list
    }
    switcher.get(argument)()


def take_values():
    name = str(input("Enter name of emp:"))
    emp_id = int(input("Enter id of emp"))
    email = str(input("Enter the email id"))
    date_entry = input('Enter a date in YYYY-MM-DD format')
    year, month, day = map(int, date_entry.split('/'))
    date1 = datetime.date(year, month, day)
    print(date1)
    lst = []
    emp = {'name': name,
           'emp id': emp_id,
           'email': email,
           'date_entry': date_entry}
    print(emp)
    lst.append(emp)
    print("Enter 1 :to insert a record "
          "Enter 2 :to update a record "
          "Enter 3 to delete a record"
          "Entert 4 to search a record"
          "Enetr 5 to list records")
    choice = int(input())
    switch_demo(choice)


take_values()
