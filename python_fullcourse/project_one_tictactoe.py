##uni hetevyal maser tic tac toe xaxy
##
##game initialization:
##    board sarqel,
##    xaxcoxnun sarqel,
##    um hertne
##
##tiv@ greg@
##
##polen gdnik@

def player_input():
    player = input("Пожалуйста выберите символ 'X' или 'O': ")
    while (new_player:=player.upper()) not in ['X','O']:
         player = input("Пожалуйста выберите символ 'X' или 'O': ")
    return new_player

def confirm(question):
    question = question.replace('?','')
    confirmation = input(f'{question}? Введите Yes или No: ')
    return confirmation.lower() == 'yes'

def draw_board(board):
    print("-----------")
    for i in range(6,-1,-3):
        print('   |   |   ')
        print(f' {board[i]} | {board[i+1]} | {board[i+2]} ')
        print('   |   |   ', end="\n-----------\n")

def mark_board(board, player):
    pos = get_position(board)
    board[pos] = player   
    return board

def get_position(board):
    pos = input('Введите следующую клетку (1-9): ')
    while pos not in ('1','2','3','4','5','6','7','8','9') or not space_check(board,int(pos)-1):
        pos = input('Введите цифру от 1 до 9: ')
    return int(pos)-1

def space_check(board,pos):
    if board[pos] !=' ':
        print('Это поле занято, выберите другое.')
        return False
    return True

def is_win(board, player):
    win_combs = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for comb in win_combs:
        if board[comb[0]] == board[comb[1]] == board[comb[2]] == player:
            return True
    return False

def replay():
    return confirm('Вы хотите сыграть снова?')

def start():
    player = player_input()
    if confirm('Вы готовы ыграть'):
        board = [' '] * 9
        win = False
        while not win and ' ' in board:
            draw_board(board)
            board = mark_board(board, player)
            if win:=is_win(board,player):
                break
            player = 'O' if player=='X' else 'X' 
            
        draw_board(board)
        if win:
            print(f"Поздравляю игрок({player}) выиграл!")
        else:
            print('','---НИЧЬЯ---','', sep='\n===========\n')
            
    

while True:
    start()
    if not replay():
        break

