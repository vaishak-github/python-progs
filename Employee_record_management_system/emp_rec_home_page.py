import insert_record as ir
import update_record as ur
import delete_record as dr
import search_record as sr
import datetime
import re
import validations as v
import list_record as lr


def choice1_insert(lst):
    emp_id = input("Enter id of emp")
    while not emp_id.isdigit():
        print("Invalid id")
        emp_id = input("Enter id of emp:")
    emp_id = check_unique(emp_id, lst)
    name = input("Enter name of emp:")
    while not name.isalpha():
        print("Invalid name")
        name = input("Enter name of emp:")

    email = str(input("Enter the email id"))
    e = v.check_email(email)

    date_entry = input('Enter a date in YYYY/MM/DD format')
    d = v.check_dob(date_entry)

    di = ir.Insert(int(emp_id), name, e, d)
    a = lst_insert(di, lst)


def choice2_update(lst):
    emp_id = input("Enter id of emp u want to update details")
    while not emp_id.isdigit():
        print("Invalid id")
        emp_id = input("Enter id of emp you want to update details:")
    print(
        " Enter 1 for updating  name \n"
        " Enter 2 for updating  email \n"
        " Enter 3 for updating  dob  \n"
    )
    choice = int(input())
    if choice == 1:
        new_name = str(input("Enter new_name"))
        while not new_name.isalpha():
            print("Invalid name")
            new_name = input("Enter new_name")
        a = ur.update(choice, int(emp_id), lst, new_name)
        print("Name:", a, "has been updated for id", emp_id)

    elif choice == 2:
        new_email = str(input("Enter new_email"))
        e = v.check_email(new_email)
        a = ur.update(choice, int(emp_id), lst, e)
        print("Email:", a, "has been updated for id ", emp_id)
    else:
        new_dob = str(input("Enter new_dob"))
        a = ur.update(choice, int(emp_id), lst, new_dob)
        print("DOB", a, "has been updated for id ", emp_id)


def choice3_delete(lst):
    eid = int(input("Enter id of emp u want to delete"))
    a = dr.delete(eid, lst)
    print("The records for id:", eid, "is deleted")


def choice4_search(lst):
    print("search using :(1:id)/(2:name)")
    choice = int(input())
    if choice == 1:
        eid = int(input("Enter id"))
        a = sr.search(lst, eid, choice)

    else:
        name = str(input("Enter name"))
        b = sr.search(lst, name, choice)


def choice5_list(lst):
    lr.listing_records(lst)


def check_unique(eid, lst):
    eid = int(eid)
    count = 0
    for i in lst:
        if i['emp_id'] == eid:
            count = 1

    if count == 1:
        print("Id already exists")
        eid = input("Enter id of emp:")
        check_unique(eid, lst)
    else:
        return eid


def lst_insert(d, lst):
    lst.append(d)
    return lst


def core():
    print("                               Vk's                                ")
    print("                   Employee  Records  Management System            ")
    lst = []
    i = 0
    while i >= 0:
        print("Enter choice:(1:insert)/(2:update)/(3:delete)/(4:search)/(5:list)")
        try:
            choice = int(input())
        except ValueError:
            print("Enter proper choice")
            continue
        else:
            if choice == 1:
                choice1_insert(lst)

            if choice == 2:
                choice2_update(lst)

            if choice == 3:
                choice3_delete(lst)

            if choice == 4:
                choice4_search(lst)

            if choice == 5:
                choice5_list(lst)

        print("Do you wish to continue (Y/N)")
        wish = input()
        if wish == 'N' or wish == 'n':
            break
        i = i + 1


core()
