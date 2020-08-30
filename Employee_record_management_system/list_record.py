def listing_records(lst):
    if len(lst)==0:
        print("Sorry,no records in the system")
    else:
        print("    Employee record info till date:      ")
        for i in lst:
         print("Id:", i['emp_id'], "||  Name:", i['emp_name'],
               "||  Email:", i['emp_email'], "||  DOB:", i['emp_dob'])
