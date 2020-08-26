import insert_record as ir
import update_record as ur
import delete_record as dr
import search_record as sr
import datetime
import re
import validations as v

def lst_insert(d, lst):
    lst.append(d)
    return lst


def core():
    print("       emp   management system            ")
    lst = []
    i = 0
    while i >= 0:
        print("enter choice:(1:insert)/(2:update)/(3:delete)/(4:search)/(5:list)")
        print(lst)
        choice = int(input())
        if choice == 1:

            name = input("Enter name of emp:")
            while not name.isalpha():
                print("Invalid name")
                name = input("Enter name of emp:")
            emp_id = input("Enter id of emp")
            while not emp_id.isdigit():
                print("Invalid id")
                emp_id = input("Enter id of emp:")
            #e_id = v.check_id(emp_id)
            email = str(input("Enter the email id"))
            e = v.check_email(email)
            date_entry = input('Enter a date in YYYY/MM/DD format')
            d = v.check_dob(date_entry)

            di = ir.Insert(name, int(emp_id), e, d)
            a = lst_insert(di, lst)
            print(a)
        if choice == 2:
            emp_id = input("Enter id of emp u want to update details")
            while not emp_id.isdigit():
                print("Invalid id")
                emp_id = input("Enter id of emp u want to update details:")
            print("Enter the attribute which you want to update(name,email,dob)")
            choice = str(input())
            if choice == "name":
                new_name = str(input("Enter new_name"))
                while not name.isalpha():
                    print("Invalid name")
                    name = input("Enter new_name")
                a = ur.update(choice, int(emp_id), lst, new_name)
                print(a)
            elif choice == "email":
                new_email = str(input("Enter new_email"))
                e = v.check_email(new_email)
                a = ur.update(choice, int(emp_id), lst, e)
                print(a)
            else:
                new_dob = str(input("Enter new_dob"))
                a = ur.update(choice, int(emp_id), lst, new_dob)
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
        if choice==5:
               print(lst)

        print("Do you wish to continue (Y/N)")
        wish = input()
        if wish == 'N' or wish == 'n':
            break
        i = i + 1
        print(i)


core()
