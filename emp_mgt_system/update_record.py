def Update(name, emp_id, dicts):
    for i in range(0, len(dicts)):
        for d in dicts[i]:
            if dicts[i]["empid"] == emp_id:
                dicts[i]["name"] = name
    return dicts

    #for i in dicts.items():
     #   if dicts["empid"] == emp_id:
      #      dicts.update(['name'])==name



