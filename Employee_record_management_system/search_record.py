
def search(lst, eid, choice):
    if choice == 1:
        for i in lst:
            if i['emp_id'] == eid:
                return i

    if choice == 2:
        for i in lst:
            if eid in i['emp_name']:
                return i
