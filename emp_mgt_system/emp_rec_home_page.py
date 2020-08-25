import insert_record as ir
import update_record as ur
import delete_record as dr
import search_record as sr
import datetime
import re


def check_id(eid):
    regex = '^[0-9]+$'

    while not re.search(regex, eid):
        print("Invalid id")
        eid = input("Enter id of emp")
    return eid


def lst_insert(d, lst):
    lst.append(d)
    return lst


def check_dob(d):
    while True:
        year, month, day = d.split('/')
        day = int(day)
        month = int(month)
        year = int(year)
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            max_days = 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            max_days = 30
        elif year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
            max_days = 29
        else:
            max_days = 28

        if month < 1 or month > 12:
            print("please enter month correctly ")
            d = input("Enter dob again")
            continue
        if day < 1 or day > max_days:
            print("please enter correct date")
            d = input("Enter dob again")
            continue
        if year < 1900 or year > 2015:
            print("please enter correct year")
            d = input("Enter dob again")

        break

    return d


def check_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    while not re.search(regex, email):
        print("Invalid Email")
        email = str(input("Enter the email id"))
    return email


def core():
    print("       emp   management system            ")
    lst = []
    i = 0
    while i >= 0:
        print("enter choice:(1:insert)/(2:update)/(3:delete)/(4:search)/(5:list)")
        
        choice = int(input())
        if choice == 1:

            name = input("Enter name of emp:")
            while not name.isalpha():
                print("Invalid name")
                name = input("Enter name of emp:")
            emp_id = input("Enter id of emp")
            e_id = check_id(emp_id)
            email = str(input("Enter the email id"))
            e = check_email(email)
            date_entry = input('Enter a date in YYYY/MM/DD format')
            d = check_dob(date_entry)

            di = ir.Insert(name, e_id, e, d)
            a = lst_insert(di, lst)
            print(a)
        if choice == 2:
            eid = int(input("Enter id of emp u want to update details"))
            print("Enter the attribute which you want to update(name,email,dob)")
            choice = str(input())
            if choice == "name":
                new_name = str(input("Enter new_name"))
                a = ur.update(choice, eid, lst, new_name)
                print(a)
            elif choice == "email":
                new_email = str(input("Enter new_email"))
                a = ur.update(choice, eid, lst, new_email)
                print(a)
            else:
                new_dob = str(input("Enter new_dob"))
                a = ur.update(choice, eid, lst, new_dob)
                print(a)

        if choice == 3:
            eid = int(input("Enter id of emp u want to delete"))
            a = dr.delete(eid, lst)
            print(a)

        if choice == 4:
            print("search using :(1:id)/(2:name)")
            choice = int(input())
            if choice == 1:
                eid = int(input("Enter id"))
                a = sr.search(lst, eid, choice)
                print(a)
            else:
                name = str(input("Enter name"))
                b = sr.search(lst, name, choice)
                print(b)

        print("Do you wish to continue (Y/N)")
        wish = input()
        if wish == 'N' or wish == 'n':
            break
        i = i + 1
        print(i)


core()
