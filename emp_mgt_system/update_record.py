def update(choice, c, lst, n):
    if choice == "name":
        for i in range(len(lst)):
            #   for d in lst[i]:
            if lst[i]["emp_id"] == c:
                lst[i]["emp_name"] = n
        return lst
    elif choice == "email":
        for i in range(len(lst)):
            # for d in lst[i]:
            if lst[i]["emp_id"] == c:
                lst[i]["emp_email"] = n
        return lst

    else:
        for i in range(len(lst)):
            # for d in lst[i]:
            if lst[i]["emp_id"] == c:
                lst[i]["emp_dob"] = n
        return lst


    #for i in dicts.items():
     #   if dicts["empid"] == emp_id:
      #      dicts.update(['name'])==name



