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
    d = {'team': team_name, 'gs': 0, 'gc': 0, 'pts': 0, 'w': 0, 'l': 0, 'd': 0}
    return d


def take_values():
    team_lst = []
    lst = []
    for i in range(1, 4):
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

        for j in range(j, len(lst)):
            val = str(input("Enter score of" + team_lst[i] + "-" + team_lst[j]))
            val = val.split("-")
            first_team_gs = int(val[0])
            # gs_count_first_team = first_team_gs + gs_count_first_team
            lst[i]['gs'] = lst[i]['gs'] + first_team_gs  # goals scored of first team

            first_team_gc = int(val[1])
            # gc_count_first_team = first_team_gc + gc_count_first_team
            lst[i]['gc'] = lst[i]['gc'] + first_team_gc  # goals conceded by first team

            second_team_gs = int(val[1])
            # gs_count_second_team = second_team_gs + gs_count_second_team
            lst[j]['gs'] = lst[j]['gs'] + second_team_gs  # goals scored by second team

            second_team_gc = int(val[0])
            # gc_count_second_team = second_team_gc + gc_count_second_team
            lst[j]['gc'] = lst[j]['gc'] + second_team_gc  # goals conceded by second team

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


def cal_top_teams(li):

    lii = li.copy()  # lii is second list ,li is original list
    for i in range(1, len(lii) - 1):
        for j in range(0, len(lii) - 1 - i + 1):
            if lii[j]['pts'] > lii[j + 1]['pts']:
                temp = lii[j]['pts']
                lii[j]['pts'] = lii[j + 1]['pts']
                lii[j + 1]['pts'] = temp
    for i in range(len(lii)):
        print("team :", li[i]['team'], "points are:", li[i]['pts'])

    print(".......", li)
    return lii


def home():
    li = take_values()
    print("the list of dict", li)
    a = cal_top_teams(li)
    print("abhka list", a)
    print("pehleka list", li)


home()
