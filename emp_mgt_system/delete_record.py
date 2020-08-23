def delete(eid, lst):
    for i in range(len(lst)):
        if lst[i]["emp_id"] == eid:
           # print(lst[i])
            del lst[i]

    return lst
