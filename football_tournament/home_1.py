from tabulate import tabulate


def check_team_name_is_string(team_name):
    while team_name.isdigit() or len(team_name) == 0:
        print("Please enter alphabetic team name")
        team_name = input(str("enter team name"))
        team_name = team_name.lstrip()
    return team_name


def check_in_list(team_name, team_lst):
    count = 0
    if team_name in team_lst:
        count = 1
    if count == 1:
        print("Team already exists.Please enter new team name")
        team_name = input(str("enter team name"))
        team_name = team_name.lstrip()
        team_name = check_team_name_is_string(team_name)
        check_in_list(team_name, team_lst)
        return team_name
    else:
        return team_name


def dict_insert(team_name):
    d = {'team': team_name, 'pts': 0, 'gs': 0, 'gc': 0, 'w': 0, 'l': 0, 'd': 0,'gd':0, 'pos': 0}

    return d


def take_values(lst):
    team_lst = []
    print("                ||Enter scores of each team||                          ")
    for i in range(1, 7):
        team_name = str(input("Enter team" + str(i)))
        team_name = team_name.lstrip()
        team_name = check_team_name_is_string(team_name)
        team_name = check_in_list(team_name, team_lst)
        team_lst.append(team_name)
        d = dict_insert(team_name)
        lst.append(d)

    a = take_scores(lst, team_lst)
    return a


def take_scores(lst, team_lst):
    for i in range(0, len(lst)):
        j = i + 1
        lst[i]['pos'] = j

        for j in range(j, len(lst)):
            val = str(input("Enter score of" + team_lst[i] + "-" + team_lst[j]))
            val = val.split("-")
            first_team_gs = int(val[0])
            # gs_count_first_team = first_team_gs + gs_count_first_team
            lst[i]['gs'] = lst[i]['gs'] + first_team_gs  # goals scored of first team

            first_team_gc = int(val[1])
            # gc_count_first_team = first_team_gc + gc_count_first_team
            lst[i]['gc'] = lst[i]['gc'] + first_team_gc  # goals conceded by first team

            lst[i]['gd'] = lst[i]['gs'] - lst[i]['gc']

            second_team_gs = int(val[1])
            # gs_count_second_team = second_team_gs + gs_count_second_team
            lst[j]['gs'] = lst[j]['gs'] + second_team_gs  # goals scored by second team

            second_team_gc = int(val[0])
            # gc_count_second_team = second_team_gc + gc_count_second_team
            lst[j]['gc'] = lst[j]['gc'] + second_team_gc  # goals conceded by second team
            lst[j]['gd'] = lst[j]['gs'] - lst[j]['gc']
            if first_team_gs > first_team_gc:
                pts_won_by_first_team = 3
                pts_first_team = pts_won_by_first_team + lst[i]['pts']
                lst[i]['pts'] = pts_first_team
                lst[i]['w'] = lst[i]['w'] + 1
                pts_won_by_second_team = 0
                pts_second_team = pts_won_by_second_team + lst[j]['pts']
                lst[j]['pts'] = pts_second_team
                lst[j]['l'] = lst[j]['l'] + 1
            elif first_team_gc > first_team_gs:
                pts_won_by_second_team = 3
                pts_second_team = pts_won_by_second_team + lst[j]['pts']
                lst[j]['pts'] = pts_second_team
                lst[j]['w'] = lst[j]['w'] + 1
                pts_won_by_first_team = 0
                pts_first_team = pts_won_by_first_team + lst[i]['pts']
                lst[i]['pts'] = pts_first_team
                lst[i]['l'] = lst[i]['l'] + 1
            else:
                pts_won_by_first_team = pts_won_by_second_team = 1

                lst[i]['pts'] = pts_won_by_first_team + lst[i]['pts']
                lst[i]['d'] = lst[i]['d'] + 1

                lst[j]['pts'] = pts_won_by_second_team + lst[j]['pts']
                lst[j]['d'] = lst[j]['d'] + 1

    return lst


def semifinalists(li):
    lii = li.copy()  # lii is second list ,li is original list

    for i in range(0, len(lii)):
        for j in range(0, len(lii)):
            if lii[i]['pts'] < lii[j]['pts']:
                if lii[i]['pos'] < lii[j]['pos']:
                    temp = lii[i]['pos']
                    lii[i]['pos'] = lii[j]['pos']
                    lii[j]['pos'] = temp

                else:
                    continue

    print("\n")

    for i in range(0, len(lii)):
        for j in range(0, len(lii)):
            if lii[i]['pts'] == lii[j]['pts']:
                if lii[i]['gd'] < lii[j]['gd']:
                    if lii[i]['pos'] < lii[j]['pos']:
                        temp = lii[i]['pos']
                        lii[i]['pos'] = lii[j]['pos']
                        lii[j]['pos'] = temp

                    else:
                        continue

    header = lii[0].keys()
    rows = [x.values() for x in lii]
    print("                  ||Points after quarterfinals are ||                ")
    print(tabulate(rows, header))
    print("\n")




    # arranging all teams in order of points
    for i in range(0, len(lii)):
        for j in range(0, len(lii)):
            if lii[i]['pos'] < lii[j]['pos']:
                temp = lii[i]
                lii[i] = lii[j]
                lii[j] = temp

    lst2 = lii[0:4]
    header = lst2[0].keys()
    rows = [x.values() for x in lst2]
    print("                  ||Semifinalists||                  ")
    print(tabulate(rows, header))
    print("\n")
    return lst2


def finalists(li):
    fin_lst = []
    team_lst = []
    for i in range(0, len(li)):
        a = li[i]['team']
        team_lst.append(a)
        d = dict_insert(a)
        fin_lst.append(d)
    hello = take_scores(fin_lst, team_lst)
    header = hello[0].keys()
    rows = [x.values() for x in hello]
    print("                 ||table after semis matches||       ")
    print(tabulate(rows, header))
    print("\n")
    for i in range(0, len(hello)):
        for j in range(0, len(hello)):
            if hello[i]['pts'] < hello[j]['pts']:
                temp = hello[j]['pos']
                hello[j]['pos'] = hello[i]['pos']
                hello[i]['pos'] = temp

    for i in range(0, len(hello)):
        for j in range(0, len(hello)):
            if hello[i]['pts'] == hello[j]['pts']:
                if hello[i]['gd'] < hello[j]['gd']:
                    temp = hello[j]['pos']
                    hello[j]['pos'] = hello[i]['pos']
                    hello[i]['pos'] = temp
    header = hello[0].keys()
    rows = [x.values() for x in hello]

    print("                   ||final pts after semis||")
    print(tabulate(rows, header))
    print("\n")

    lst3 = hello[0:2]
    header = lst3[0].keys()
    rows = [x.values() for x in lst3]
    print("                   ||Finalists||")
    print(tabulate(rows, header))
    print("\n")
    return lst3


def winners(li):
    w_lst = []
    team_lst = []
    for i in range(0, len(li)):
        a = li[i]['team']
        team_lst.append(a)
        d = dict_insert(a)
        w_lst.append(d)
    winner = take_scores(w_lst, team_lst)

    if winner[0]['gs'] < winner[1]['gs']:
        header = winner[0].keys()
        rows = [x.values() for x in winner]
        print("                Team",winner[1]['team'], " are the champions of CL-20")
        print(tabulate(rows,header))
    else:
        header = winner[0].keys()
        rows = [x.values() for x in winner]
        print("                Team", winner[0]['team'], " are the champions of CL-20")
        print(tabulate(rows, header))


def home():
    print("                  Welcome to Champions league 2020                         ")
    lst = []
    fi = []
    li = take_values(lst)
    a = semifinalists(li)
    b = finalists(a)
    winners(b)


home()
