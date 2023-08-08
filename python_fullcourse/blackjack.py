import random
from typing import Any
class blackjack:
    def __init__(self, chips:int=100):
        self.__deck = ['A','2','3','4','5','6','7','8','9','10','B','Q','K']*4
        self.cards_costs = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'B':10,'Q':10,'K':10}
        self.deck_shuffle()
        self.__player = {'name': 'Игрок','cards':[], 'chips':chips, 'amount': 0}
        self.__diller = {'name': 'Диллер','cards':[], 'amount': 0}

    @property
    def player_chips(self):
        return f"На счёте игрока: {self.__player['chips']} фишек"

    @property
    def player(self):
        return self.__player

    def diller(self):
        return self.__diller
    
    
    def card_cost(self,who,card):
        if cost:=self.cards_costs.get(card, False):
            return card,cost
        elif card == 'A':
            a_cost = input(f"({who['name']})Вы достали ТУЗ, выберите кол-во очков(1 или 11): ")
            while True:
                if a_cost not in ['1','11']:
                    a_cost = input("({who['name']})(ТУЗ) Ввели неправильные данные, наберите (1 или 11): ")
                else:
                    return f"A({a_cost})",int(a_cost)
        else:
            raise ValueError('Такой карты не существует')

    def deck_shuffle(self):
        for _ in range(random.randint(3,7)):
            random.shuffle(self.__deck)

    def answer_bet(self):
        while True:
            bet = input(f"Сделайте ставку, у вас {self.__player['chips']} фишек: ")
            if not bet.isdigit():
                print("Введите число!")
                continue

            elif int(bet)>self.__player['chips']:
                print("Недостаточно фишек для ставки")
                continue
            else:
                self.__player['chips']-=int(bet)
                return int(bet)
     
        
    def card_distribution(self):
        for _ in range(2):
            self.__player['cards'].extend(self.__deck[-1:-3])
            self.__diller['cards'].extend(self.__deck[-3:-5])
            self.__deck = self.__deck[:-3]

    def display_cards(self):
        print(f"Карты игрока: {' | '.join(self.__player['cards'])}")
        print(f"Карты диллера: {' | '.join(self.__diller['cards'][:1])}")


    def hit_or_stay(self,who:{'amount': int, 'cards':[str,...], Any:Any}) -> bool:
        """
        User choice hit or stay and call function
        return: True if hit,False if stay
        """
        choice = input("Хотите взять карту из колоды?(y/hit или n/stay)")
        match choice.lower():
            case 'hit' | 'y':
                self.hit(who,1)
                return True
            case 'stay' | 'n':
                return False

    def hit(self,who,cards_q):
        for _ in range(cards_q):
            card, cost = self.card_cost(who,self.__deck.pop())
            who['amount'] +=cost
            who['cards'].append(card)
            print(f"Вы достали карту {card}")
       
    def start(self):
        bet = self.answer_bet()
        self.card_distribution()
        while True:
            while self.__player['amount']<=21:
                self.display_cards()
                if not self.hit_or_stay(self.__player):
                    break
                if self.__player['amount']==21:
                    self.__player['amount']+=bet*2
                    break
            else:
                print("Игрок Проиграл")
                break
            
            while not self.__diller['amount']>17 or not self.__diller['amount']>self.__player['amount']:
                self.display_cards()
                if not self.hit_or_stay(self.__diller):
                    break
            if (player_amount:=21-self.__player['amount'])>(diller_amount:=21-self.__diller['amount']):
                print("Победил Диллер")
            elif player_amount==diller_amount:
                print("Ничья")
            else:
                print("Победил Игрок")
            break


game = blackjack(300)
game.start()



    
