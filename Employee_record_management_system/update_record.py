def update(choice, c, lst, n):
    if choice == 1:
        for i in lst:
            if i['emp_id'] == c:
                i['emp_name'] = n
        return i['emp_name']

    elif choice == 2:
        for i in range(len(lst)):
            # for d in lst[i]:
            if lst[i]["emp_id"] == c:
                lst[i]["emp_email"] = n
        return lst[i]["emp_email"]

    else:
        for i in range(len(lst)):
            # for d in lst[i]:
            if lst[i]["emp_id"] == c:
                lst[i]["emp_dob"] = n
        return lst[i]["emp_email"]


    # for i in dicts.items():
    #   if dicts["empid"] == emp_id:
    #      dicts.update(['name'])==name
