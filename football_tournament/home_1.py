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
    d = {'team': team_name, 'gs': 0, 'gc': 0, 'pts': 0, 'w': 0, 'l': 0, 'd': 0, 'pos': 0}

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
        for j in range(i + 1, len(lii)):
            if lii[i]['pts'] < lii[j]['pts']:
                if lii[i]['pos'] < lii[j]['pos']:
                    temp = lii[i]['pos']
                    lii[i]['pos'] = lii[j]['pos']
                    lii[j]['pos'] = temp

                else:
                    continue


    print("")
    print(lii)
    print("")
    for i in range(0, len(lii)):
        for j in range(i + 1, len(lii)):
            if lii[i]['pts'] == lii[j]['pts']:
                if lii[i]['gd'] < lii[j]['gd']:
                    if lii[i]['pos'] < lii[j]['pos']:
                        temp = lii[i]['pos']
                        lii[i]['pos'] = lii[j]['pos']
                        lii[j]['pos'] = temp

                    else:
                        continue

    print("                  ||Points after quarterfinals are ||                ")
    for i in range(0, len(lii)):
        print("team||", lii[i]['team'], " goals scored||", lii[i]['gs'], " goals conceded||", lii[i]['gc'],
              " points||", lii[i]['pts'], " win||", lii[i]['w'], " loss||", lii[i]['l'], " draw||", lii[i]['d'],
              " gd||", lii[i]['gd'], " position||", lii[i]['pos'])

    # arranging all teams in order of points
    for i in range(0, len(lii)):
        for j in range(i + 1, len(lii)):
            if lii[i]['pos'] > lii[j]['pos']:
                temp = lii[j]
                lii[j] = lii[i]
                lii[i] = temp

    lst2 = lii[0:4]
    print("")
    print("                  ||Semifinalists||                  ")
    for i in range(0, len(lst2)):
        print("team||", lst2[i]['team'], " goals scored||", lst2[i]['gs'], " goals conceded||", lst2[i]['gc'],
              " points||", lst2[i]['pts'], " win||", lst2[i]['w'], " loss||", lst2[i]['l'], " draw||", lst2[i]['d'],
              " gd||", lst2[i]['gd'], " position||", lst2[i]['pos'])

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

    print("                 ||table after semis matches||       ")
    for i in range(0, len(hello)):
        print("team||", hello[i]['team'], " goals scored||", hello[i]['gs'], " goals conceded||", hello[i]['gc'],
              " points||", hello[i]['pts'], " win||", hello[i]['w'], " loss||", hello[i]['l'], " draw||", hello[i]['d'],
              " gd||", hello[i]['gd'], " position||", hello[i]['pos'])

    for i in range(0, len(hello)):
        for j in range(i + 1, len(hello)):
            if hello[i]['pts'] < hello[j]['pts']:
                temp = hello[j]['pos']
                hello[j]['pos'] = hello[i]['pos']
                hello[i]['pos'] = temp

    for i in range(0, len(hello)):
        for j in range(i + 1, len(hello)):
            if hello[i]['pts'] == hello[j]['pts']:
                if hello[i]['gd'] < hello[j]['gd']:
                    temp = hello[j]['pos']
                    hello[j]['pos'] = hello[i]['pos']
                    hello[i]['pos'] = temp

    print("                   ||final pts after semis||")
    for i in range(0, len(hello)):
        print("team||", hello[i]['team'], " goals scored||", hello[i]['gs'], " goals conceded||", hello[i]['gc'],
              " points||", hello[i]['pts'], " win||", hello[i]['w'], " loss||", hello[i]['l'], " draw||", hello[i]['d'],
              " gd||", hello[i]['gd'], " position||", hello[i]['pos'])

    lst3 = hello[0:2]
    print("                   ||Finalists||")
    for i in range(0, len(lst3)):
        print("team||", lst3[i]['team'], " goals scored||", lst3[i]['gs'], " goals conceded||", lst3[i]['gc'],
              " points||", lst3[i]['pts'], " win||", lst3[i]['w'], " loss||", lst3[i]['l'], " draw||", lst3[i]['d'],
              " gd||", lst3[i]['gd'], " position||", lst3[i]['pos'])


def home():
    lst = []
    fi = []
    li = take_values(lst)
    print("                ||the list of dict||              ")
    print(li)
    a = semifinalists(li)
    finalists(a)


home()
