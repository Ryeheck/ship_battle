from string import ascii_uppercase
from time import sleep


def doesnt_standart_board(board, comanda):
    print(f'Team {comanda}')
    while True:
        try:
            letter = int(input('Сколько буковок??: '))
            nums = int(input('Сколько цифорок?: '))

            if letter < 27:
                if nums < 61:
                    break
                else:
                    print('экран кончился')
            else:
                print('алфавит кончился')

        except ValueError:
            print('normal num!!!')
            
    board = [['□']*(letter+1) for _ in range(nums+1)]

    for char in range(1, nums+1):
        board[char][0] = f'\033[1;37m{char}\033[0m'

    for char in range(1, letter+1):
        board[0][char] = f'\033[1;37m{ascii_uppercase[char-1]}\033[0m'
    board[0][0] = ' '
    return board

def board_standart(board):
    board = [['□']*10 for _ in range(10)]

    for char in range(1, 10):
        board[0][char] = f'\033[1;37m{ascii_uppercase[char-1]}\033[0m'
        board[char][0] = f'\033[1;37m{char}\033[0m'
    board[0][0] = ' '
    return board

def board_custom(board1, board2):
    for char in range(1, 10):
        board1[0][char] = input('top position: ')
        board1[char][0] = input('position in left: ')
        board2[0][char] = board1[0][char]
        board2[char][0] = board1[char][0]

def print_board_team(board):
    print()
    for k in board:
        sleep(0.06)
        print(*k, sep='  ')
