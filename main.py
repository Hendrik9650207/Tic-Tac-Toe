theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(' ' + board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
    print('---+---+---')
    print(' ' + board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
    print('---+---+---')
    print(' ' + board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'])


def positionBoard(board):
    list1 = list(board.keys())
    print('The Board Coordinate:')
    print()
    print(list1[0] + '|' + list1[1] + '|' + list1[2])
    print('-----+-----+-----')
    print(list1[3] + '|' + list1[4] + '|' + list1[5])
    print('-----+-----+-----')
    print(list1[6] + '|' + list1[7] + '|' + list1[8])
    print('-----+-----+-----')
    print()


turn = 'O'
positionBoard(theBoard)
printBoard(theBoard)
for i in range(9):
    move = str(input('Turn:' + turn + ' Enter your move:'))
    while True:
        if move in theBoard.keys():
            theBoard[move] = turn
            break
        else:
            print('Enter the right coordinate.')
            move = str(input('Turn:' + turn + ' Enter your move:'))

    if turn == 'O':
        turn = 'X'
    else:
        turn = 'O'
    printBoard(theBoard)

