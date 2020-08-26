def delete(eid, lst):
    for i in lst:
        if i['emp_id'] == eid:
            # print(lst[i])
            lst.remove(i)

    return lst
