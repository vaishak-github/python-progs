def check_winner(lst):
    #for x
    if(lst[0]=='X' and lst[1]=='X' and lst[2]=='X'): #horizontal check
        print("X won")
        return 1
    if (lst[3] == 'X' and lst[4] == 'X' and lst[5] == 'X'):
        print("X won")
        return 1
    if (lst[6] == 'X' and lst[7] == 'X' and lst[8] == 'X'):
        print("X won")
        return 1
    if (lst[0] == 'X' and lst[3] == 'X' and lst[6] == 'X'): #vertical check
            print("X won")
            return 1
    if (lst[1] == 'X' and lst[4] == 'X' and lst[7] == 'X'):
            print("X won")
            return 1
    if (lst[2] == 'X' and lst[5] == 'X' and lst[8] == 'X'):
            print("X won")
            return 1

    if (lst[0] == 'X' and lst[4] == 'X' and lst[8] == 'X'):#diagonal check
        print("X won")
        return 1
    if (lst[2] == 'X' and lst[4] == 'X' and lst[6] == 'X'):
        print("X won")
        return 1
    if (lst[6] == 'X' and lst[7] == 'X' and lst[8] == 'X'):
        print("X won")
        return 1

 # for 0

    if (lst[0] == '0' and lst[1] == '0' and lst[2] == '0'):  # horizontal check
        print("0 won")
        return 1
    if (lst[3] == '0' and lst[4] == '0' and lst[5] == '0'):
        print("0  won")
        return 1
    if (lst[6] == '0' and lst[7] == '0' and lst[8] == '0'):
        print("0 won")
        return 1

    if (lst[0] == '0' and lst[3] == '0' and lst[6] == '0'):  # vertical check
        print("0 won")
        return 1
    if (lst[1] == '0' and lst[4] == '0' and lst[7] == '0'):
        print("0 won")
        return 1
    if (lst[2] == '0' and lst[5] == '0' and lst[8] == '0'):
        print("0 won")
        return 1

    if (lst[0] == '0' and lst[4] == '0' and lst[8] == '0'):  # diagonal check
        print("0 won")
        return 1
    if (lst[2] == '0' and lst[4] == '0' and lst[6] == '0'):
        print("0 won")
        return 1
    if (lst[6] == '0' and lst[7] == '0' and lst[8] == '0'):
        print("0 won")
        return 1
    return 0



def take_values():
    lst=[]
    for i in range(9):
        print("Enter the ",i,"th move")
        ele = str(input())
        lst.append(ele.upper())  # adding the element
    print(lst)
    print(lst[0],'|',lst[1],'|',lst[2])
    print('--  --  --')
    print(lst[3],'|',lst[4],'|',lst[5])
    print('--  --  --')
    print(lst[6],'|',lst[7],'|',lst[8])
    print('--  --  --')
    print()
    check=check_winner(lst)
    if check==0:
        print("Draww")
take_values()