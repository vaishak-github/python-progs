def Insert(i, n, e, d):

    dic = {'emp_id': i, 'emp_name': n, 'emp_email': e, 'emp_dob': d}
    print("The details for employee with id:", dic['emp_id'], "are:\n Name:", dic['emp_name'],
          "\n Email:", dic['emp_email'], "\n Date of birth:", dic["emp_dob"])
    return dic
