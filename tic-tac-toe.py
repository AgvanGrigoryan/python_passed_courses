from collections import deque
import math
class TicTacToe:
    __rules = 'Крестики Нолики\nСделай 3 в ряд и победи. Игрок который первым соберет последовательность победит.Как Играть: Во время своего хода вводите от 1 до 9 и нажимаете Enter, Если данное поле сободно ваш ход зачисливается иначе повторите ввод'
    
    def __init__(self, player1:str, player2:str):
        self.playerOne = player1
        self.playerTwo = player2
        print(self.rules)

    @property
    def playerOne(self):
        return self.__playerOne

    @playerOne.setter
    def playerOne(self, name):
        self.__playerOne = {'name': name, 'sign': 'X'}

    @property
    def playerTwo(self):
        return self.__playerTwo


    @playerTwo.setter
    def playerTwo(self, name):
        self.__playerTwo = {'name': name, 'sign': 'O'}

    def __game_init(self):
        self.__game_over = False
        self.__turnDeque = deque([self.__playerTwo,self.__playerOne]*5,9)
        self.__board = [' ', ' ', ' ',' ', ' ', ' ',' ', ' ', ' ']
        self.drawBoard()
        

    @property
    def rules(self):
        return TicTacToe.__rules

    def start(self):
        self.__game_init()
        while not self.__game_over and self.__turnDeque:
            person = self.__turnDeque.popleft()
            self.__EnterStep(person)
            self.drawBoard()
            if self.__isWinCombination(person):
                break
                        
    def __isWinCombination(self, person):
        sign = person['sign']
        board = list(map(lambda f: True if f == sign else False,self.__board))
        if all(board[0:3]) or all(board[3:6]) or all(board[6:9]) \
            or all([board[0],board[3],board[6]]) or all([board[1],board[4],board[7]]) or all([board[2],board[5],board[8]]) \
            or all([board[0],board[4],board[8]]) or all([board[2],board[4],board[6]]):
            print(f"{person['name']} is Win")
            self.gameOver()
                                  


    def __EnterStep(self,person):
        while True:
            step = input(f"{person['name']}\'s({person['sign']}) turn(0-quit): ")
            if not step.isdigit():
                print(f'Expected number not {step}')
                continue
            step = int(step)
            if step == 0:
                self.gameOver()
                break
            if not (0<step<=9):
                print('Input numbers between 1 and 9!')
                continue
            if not self._isFieldFree(step):
                print('This field is not empty. Choose another field')
                continue
            else:
                self.__board[step-1] = person['sign']
                break
                         
    def _isFieldFree(self,step):
        return self.__board[step-1]==' '


    def drawBoard(self):
        for i in range(0,9,3):
            print(self.__board[i],self.__board[i+1],self.__board[i+2], sep=' | ', end='\n---------\n')
            
    def gameOver(self):
        self.__game_over = True
        print("Game is ended.")
##        
##    def __setPlayer(self,sign):
##        playerName = input(f'Enter a {sign} Player name: ')
##        player = {'name': playerName, 'sign': sign}
##        return player

    

player1 = input('Player One name: ')
player2 = input('Player Two name: ')
game = TicTacToe(player1, player2)
game.start()
input()
