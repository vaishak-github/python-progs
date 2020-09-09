def check_val_is_string(val):
    while val.isdigit() or len(val)==0:
        print("Please enter alphabetic team name")
        val = input(str("enter team name"))
        val = val.lstrip()
    return val


def dict_insert(li):
    li = {li: li}

    return li


def lst_insert(a, value):
    value.append(a)

    return value


def check_in_list(val, lst):
    count = 0
    if val in lst:
        count = 1
    if count == 1:
        print("Team already exists.Please enter new team name")
        val = input(str("enter team name"))
        val = val.lstrip()
        val=check_val_is_string(val)
        check_in_list(val, lst)
        return val
    else:
        return val


def take_values(lst):
    for i in range(1, 7):
        val = input(str("enter team name_" + str(i)))
        val = val.lstrip()
        val = check_val_is_string(val)
        val = check_in_list(val, lst)
        lst.append(val)
    return lst


def take_scores_of_team(lst, value):
    for i in range(len(lst)):
        a = dict_insert(lst[i])
        b = lst_insert(a, value)
    print(b)
    for i in range(0, len(lst)):
        j = i + 1
        pts_first_team = 0
        pts_second_team = 0
        gs_count_first_team = 0
        gc_count_first_team = 0

        gs_count_second_team = 0
        gc_count_second_team = 0

        for j in range(j, len(lst)):
            val = str(input("Enter score of" + lst[i] + "-" + lst[j]))
            val = val.split("-")
            first_team_gs = int(val[0])
            gs_count_first_team = first_team_gs + gs_count_first_team
            b[i]['gs'] = gs_count_first_team
            #  print(first_team_gs)

            first_team_gc = int(val[1])
            gc_count_first_team = first_team_gc + gc_count_first_team
            b[i]['gc'] = gc_count_first_team
            #  print(first_team_gc)

            second_team_gs = int(val[1])
            gs_count_second_team = second_team_gs + gs_count_second_team
            b[j]['gs'] = gs_count_second_team
            # print(second_team_gs)

            second_team_gc = int(val[0])
            gc_count_second_team = second_team_gc + gc_count_second_team
            b[j]['gc'] = gc_count_second_team
            #  print(second_team_gc)

            if first_team_gs > first_team_gc:
                pts_won_by_first_team = 3
                pts_first_team = pts_won_by_first_team + pts_first_team
                b[i]['pts'] = pts_first_team
            else:
                pts_won_by_first_team = 0
                pts_first_team = pts_won_by_first_team + pts_first_team
                b[i]['pts'] = pts_first_team
            if second_team_gs > second_team_gc:
                pts_won_by_second_team = 3
                pts_second_team = pts_won_by_second_team + pts_second_team
                b[j]['pts'] = pts_second_team
            else:
                pts_won_by_second_team = 0
                pts_second_team = pts_won_by_second_team + pts_second_team
                b[j]['pts'] = pts_second_team
            if first_team_gs == second_team_gs:
                pts_won_by_first_team = pts_won_by_second_team = 1
                pts_first_team = pts_won_by_first_team + pts_first_team
                b[i]['pts'] = pts_first_team
                pts_second_team = pts_won_by_second_team + pts_second_team
                b[j]['pts'] = pts_second_team
            gs_count_second_team = 0
            gc_count_second_team = 0

            c = lst_insert(b, value)
    return(c)


def home():
    lst = []
    value = []

    take_values(lst)
    print(lst)
    b = take_scores_of_team(lst, value)
    print(b)


home()
