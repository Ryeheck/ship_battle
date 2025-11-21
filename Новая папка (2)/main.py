from copy import deepcopy
from time import sleep
import boards


def proverka_1(ships_team, chisl_ychen):
    for char in range(1, chisl_ychen+1): 

        boards.print_board_team(ships_team) 

        while True:
            try:
                size_A, size_1 = input(f'Enter, where will stand ship in {i} team, {char} player [example: A5 B5]: ').split()

                size_abs_A, *size_abs_num = size_A
                size_abs_A_1, *size_abs_num_1 = size_1

                j=''
                k=''
                for l in size_abs_num:
                    j += l
                for p in size_abs_num_1:
                    k += p

                size_abs_num, size_abs_num_1 = j, k
                size_abs_A, size_abs_A_1 = dict1[size_abs_A], dict1[size_abs_A_1]
                size_abs_num, size_abs_num_1 = int(size_abs_num), int(size_abs_num_1)
                
                

                if size_abs_A > size_abs_A_1:
                    size_abs_A, size_abs_A_1 = size_abs_A_1, size_abs_A

                if size_abs_num > size_abs_num_1:
                    size_abs_num, size_abs_num_1 = size_abs_num_1, size_abs_num

                if size_abs_A == size_abs_A_1: #горизонталь
                    for size in range(size_abs_num, size_abs_num_1+1):
                       ships_team[size][size_abs_A] = 'L'
                    break
                elif size_abs_num == size_abs_num_1: #вертикаль
                    for size in range(size_abs_A, size_abs_A_1+1):
                        ships_team[size_abs_num][size] = 'L'
                    break
                else:
                    print('no correct data')
            except ValueError:
                print('valueerror')
            except IndexError:
                print('indexerror')
            except KeyError:
                print("keyerror")
            except UnboundLocalError:
                print("MORE")

    boards.print_board_team(ships_team) 

def proverka_2(ships_team, comanda):
    while True:
        while True:
            try:
                shot = input(f'Shoot on {comanda} team!: ')
                shot_A, *shot_1 = shot
                break
            except ValueError:
                print('ValueError')

        j = ''
        for l in shot_1:
            j +=l
        shot_1 = l

        try:
            shot_1 = int(shot_1)
            shot_A = dict1[shot_A]

            if shot_1 > 10 or shot_1 < -1:
                print('out of range')

            ships_team[shot_1][shot_A] == 'L'
            break
        except ValueError:
            print('valueerror')
        except IndexError:
            print('out of range')
        except KeyError:
            print('keyerror')
    return shot_A, shot_1

def tick_tack(tick):
    tick += 1
    
    while tick > 0:
        tick -= 1

        sleep(1)
        print(f'Через {tick} все сотрется', end='\r')
    print('\033[H\033[J', end = '')


dict1 = {f'{boards.ascii_uppercase[i]}': i+1 for i in range(len(boards.ascii_uppercase))}
board_team_1 = []
board_team_2 = []

while True:
    try:
        position = int(input('■■■■■■ or standart or doesnt_standart_board [1,2,3]: '))
        position = int(position)

        if 1 < position < 4: #replace 1-0
            break
        print('NONE')
    except ValueError:
        print('NONe')

if position == 2:
    board_team_1 = boards.board_standart(board_team_1)
    board_team_2 = boards.board_standart(board_team_2)
elif position == 3:
    board_team_1 = boards.doesnt_standart_board(board_team_1, comanda=1)
    board_team_2 = boards.doesnt_standart_board(board_team_2, comanda=2)

for i in range(1, 3):
    while True:
        chisl_ychen = input(f'How many people in {i} team?: ')
        try:
            chisl_ychen = int(chisl_ychen)
            break
        except ValueError:
            print('Некоректно')
    if i==1:   
        ships_team_1 = deepcopy(board_team_1)

        proverka_1(ships_team_1, chisl_ychen)
        tick_tack(3)
    else:
        ships_team_2 = deepcopy(board_team_2)

        proverka_1(ships_team_2, chisl_ychen)
        tick_tack(3)

comanda = 1
board_team_1[5].append(' ENEMY ꉂ(˵˃ ᗜ ˂˵)')
board_team_2[5].append(" ENEMY (˶ˆᗜˆ˵)")

while True:
    if 'L' not in [item for sublist in ships_team_2 for item in sublist]:
        sleep(0.5)
        [[sleep(0.1), print(char, end='', flush=True)] for char in 'Team 1 win']

        break
    elif  'L' not in [item for sublist in ships_team_1 for item in sublist]:
        sleep(0.5)
        [[sleep(0.1), print(char, end='', flush=True)] for char in 'Team 2 win']

        break
    elif comanda == 2:
        comanda = 1
        boards.print_board_team(board_team_1)
        shot_A, shot_1 = proverka_2(ships_team_1, comanda)

        if ships_team_1[shot_1][shot_A] == 'L':
            board_team_1[shot_1][shot_A] = '\033[0;31mX\033[0m'
            ships_team_1[shot_1][shot_A] = ' '
            comanda = 2

            if ships_team_1[shot_1][shot_A] != 'L' and ships_team_1[shot_1+1][shot_A] != 'L' and ships_team_1[shot_1-1][shot_A] != 'L' and ships_team_1[shot_1][shot_A+1] != 'L' and ships_team_1[shot_1][shot_A-1] != 'L':
                [[sleep(0.1), print(char, end='', flush=True)] for char in 'KILL']
            else:
                [[sleep(0.1), print(char, end='', flush=True)] for char in 'HIT']

        else:
            [[sleep(0.1), print(char, end='', flush=True)] for char in 'MISS']

            board_team_1[shot_1][shot_A] = '\033[0;32m-\033[0m'
            boards.print_board_team(board_team_1)
            tick_tack(3)
    else:
        comanda = 2
        boards.print_board_team(board_team_2)
        shot_A, shot_1 = proverka_2(ships_team_2, comanda)

        if ships_team_2[shot_1][shot_A] == 'L':

            board_team_2[shot_1][shot_A] = '\033[0;31mX\033[0m'
            ships_team_2[shot_1][shot_A] = ' '
            comanda = 1

            if ships_team_2[shot_1][shot_A] != 'L' and ships_team_2[shot_1+1][shot_A] != 'L' and ships_team_2[shot_1-1][shot_A] != 'L' and ships_team_2[shot_1][shot_A+1] != 'L' and ships_team_2[shot_1][shot_A-1] != 'L':
                [[sleep(0.1), print(char, end='', flush=True)] for char in 'KILL']
            else:
                [[sleep(0.1), print(char, end='', flush=True)] for char in 'HIT']

        else:
            [[sleep(0.1), print(char, end='', flush=True)] for char in 'MISS']

            board_team_2[shot_1][shot_A] = '\033[0;32m-\033[0m'
            boards.print_board_team(board_team_2)
            tick_tack(3)

print()
print('(⸝⸝ ♡﹏♡⸝⸝)')