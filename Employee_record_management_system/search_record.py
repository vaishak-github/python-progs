def search(lst, eid, choice):
    if choice == 1:
        for i in lst:
            if i['emp_id'] == eid:
                print("The details for employee with id:", i['emp_id'], "are:\n Name:", i['emp_name'],
                      "\n Email:", i['emp_email'], "\n Date of birth:", i["emp_dob"])
                return i

    if choice == 2:
        a = 1
       # print("The records matching ", eid, "are:\n ", a, ")")

        result = [print("\n id:",
                        i['emp_id'], "\n name", i['emp_name'], "\n email", i['emp_email'], "\n dob", i['emp_dob'],
                        "\n ************************************************************************************")
                  for i in lst if i['emp_name'].startswith(eid)]

        return result
