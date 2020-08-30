import re
from datetime import datetime


def check_id(eid):
    while not eid.isdigit():
        print("Invalid id")
        eid = input("Enter id of emp:")
        return eid


def check_dob(d):
    while True:

        if d.isalnum() or d.isalpha() or d.isspace() or not d:
            print("    Please enter dob in  YYYY/MM/DD FORMAT for eg:2014/03/04     ")
            d = input('Enter  date in YYYY/MM/DD format')
            continue
        else:
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
                continue
            break

    return d


def check_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    while not re.search(regex, email):
        print("Invalid Email")
        email = str(input("Enter the email id"))
    return email
