def search(lst, eid, choice):
    if choice == 1:
        for i in lst:
            if i['emp_id'] == eid:
                print("The details for employee with id:",eid, "\n Id:", i['emp_id'], "||  Name:", i['emp_name'],
                      "||  Email:", i['emp_email'], "||  DOB:", i['emp_dob'])
                return i

    if choice == 2:
        a = 1
        # print("The records matching ", eid, "are:\n ", a, ")")

        result = [print("The details for employee with Name:",eid,"\n Id:", i['emp_id'], "||  Name:", i['emp_name'],
                        "||  Email:", i['emp_email'], "||  DOB:", i['emp_dob'])
                  for i in lst if i['emp_name'].startswith(eid)]

        return result
