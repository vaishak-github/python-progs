def check_val_is_string(val):
    while val.isdigit():
        print("Please enter alphabetic team name")
        val = input(str("enter team name"))
    return val


def dict_insert(l, pts, gs, gc):
    dicti = {'name': l, "points": pts, "goals_scored": gs, "goals_conceded": gc}

    return dicti


def lst_insert(score_lst, a):
    # a[1]['goal_Scored'=
    score_lst.append(a)
    return score_lst


def check_in_list(val, lst):
    count = 0
    if val in lst:
        count = 1
    if count == 1:
        print("Team already exists.Please enter new team name")
        val = input(str("enter team name"))
        val = val.lstrip()
        check_val_is_string(val)
        check_in_list(val, lst)
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


def take_scores_of_team(lst, score_lst):
    for i in range(len(lst)):
        j = i + 1
        f = lst[i]
        pts = 0
        gs = 0
        gc = 0

        for j in range(j, len(lst)):
            val = str(input("Score of " + lst[i] + "-" + lst[j]))

            val = val.split("-")
            gs_count = int(val[0])
            gs = gs + gs_count
            gc_count = int(val[1])
            gc = gc + gc_count
            if gs_count > gc_count:
                pts_win = 3
                pts = pts + pts_win
            if gc_count > gs_count:
                pts_loss = 0
                pts = pts + pts_loss
            if gc_count == gs_count:
                pts_draw = 1
                pts = pts_draw + pts
            a = dict_insert(f, pts, gs, gc)

        b = lst_insert(score_lst, a)
    return b


def home():
    lst = []
    score_lst = []
    take_values(lst)
    print(lst)
    b = take_scores_of_team(lst, score_lst)
    print(b)


home()
