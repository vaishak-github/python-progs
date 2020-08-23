import insert_record as ir
import update_record as ur
import delete_record as dr


def lst_insert(d, lst):
    lst.append(d)
    return lst


def core():
    print("       emp   management system            ")
    lst = []

    i = 0
    while i >= 0:
        print("enter choice:(insert)/(update)/(delete)/(list)/(search)")
        choice = str(input())
        if choice == "insert":
            name = str(input("Enter name of emp:"))
            emp_id = int(input("Enter id of emp"))
            email = str(input("Enter the email id"))
            date_entry = input('Enter a date in YYYY/MM/DD format')
            di = ir.Insert(name, emp_id, email, date_entry)
            a = lst_insert(di, lst)
            print(a)
        if choice == "update":
            id = int(input("Enter id of emp u want to update details"))
            print("Enter the attribute which you want to update(name,email,dob)")
            choice = str(input())
            if choice == "name":
                new_name = str(input("Enter new_name"))
                a = ur.update(choice, id, lst, new_name)
                print(a)
            elif choice == "email":
                new_email = str(input("Enter new_email"))
                a = ur.update(choice, id, lst, new_email)
                print(a)
            else:
                new_dob = str(input("Enter new_dob"))
                a = ur.update(choice, id, lst, new_dob)
                print(a)

        if choice == "delete":
            id = int(input("Enter id of emp u want to delete"))
            a= dr.delete(id,lst)
            print(a)

        print("Do you wish to continue (Y/N)")
        wish = input()
        if wish == 'N' or wish == 'n':
            break
        i = i + 1
        print(i)


core()
