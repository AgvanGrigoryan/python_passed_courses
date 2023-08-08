import random
from colorama import init,Fore,Style,Back
init()

suits = ("Червы", "Бубны", "Пики", "Трефы")
ranks = (
    "Двойка", "Тройка", "Четверка", "Пятерка",
    "Шестерка", "Семерка", "Восьмерка", "Девятка",
    "Десятка", "Валет", "Дама", "Король", "Туз"
    )

values = {
    "Двойка": 2, "Тройка": 3, "Четверка": 4,
    "Пятерка": 5,"Шестерка": 6,"Семерка": 7,
    "Восьмерка": 8,"Девятка": 9, "Десятка": 10,
    "Валет": 10,"Дама": 10,"Король": 10, "Туз": 11
    }


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank, values[rank]))

    def shuffle(self):
        for _ in range(5):
            random.shuffle(self.deck)

    def __str__(self):
        cards = ',\n'.join(map(str, self.deck))
        return "Колода: {len(self.deck)} карт.\n" + cards

    def deal(self):
        return self.deck.pop()


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} {self.suit}"


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        # card is Card object given from Deck class(Deck.deal())
        self.cards.append(card)
        self.value += card.value
        if card.rank.lower() == 'туз':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Player:
    def __init__(self, chips=100, is_dealer=False):
        self.hand = Hand()
        if not is_dealer:
            self.chips = chips
            self.bet = 0

    def take_bet(self):
        while True:
            bet = input(f"Сделайте ставку, у вас {self.chips} фишек: ")
            if not bet.isdigit():
                print("Введите число!")
                continue
            elif int(bet) > self.chips:
                print("Недостаточно фишек для ставки")
                continue
            else:
                self.bet = int(bet)
                break

    def lose_bet(self):
        self.chips -= self.bet

    def win_bet(self):
        self.chips += self.bet

    def hit(self, deck):
        self.hand.add_card(deck.deal())
        self.hand.adjust_for_ace()


class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.playing = True
        # player
        self.player = Player()
        self.dealer = Player(is_dealer=True)
        self.greating()

    def restart(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player.hand = Hand()
        self.dealer.hand = Hand()

    def start(self):
        while True:
            self.player.take_bet()
            self.deal_cards()
            self.show_some()
            while self.playing:
                self.hit_or_stand(self.player)
                self.show_some()
                if self.player.hand.value > 21:
                    self.player_busts()
                    break

            if self.player.hand.value <= 21:
                while self.dealer.hand.value < 17:
                    self.dealer.hit(self.deck)

                self.show_all()
                if self.dealer.hand.value > 21:
                    self.dealer_busts()
                elif self.dealer.hand.value > self.player.hand.value:
                    self.dealer_wins()
                elif self.dealer.hand.value < self.player.hand.value:
                    self.player_wins()
                else:
                    self.push()

            print('\nКолличество фишек игрока {}'.format(self.player.chips))
            play_again = input('Хотите сыграть снова?(y или n): ').lower()
            if play_again == 'n':
                print('')
                break
            elif play_again == 'y':
                self.playing = True
                self.restart()
            else:
                break

    @staticmethod
    def greating():
        print('Добро пожаловать в игру Блекджек!')

    def deal_cards(self):
        self.player.hand.add_card(self.deck.deal())
        self.player.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())

    def show_some(self):
        print(f'\n{Fore.LIGHTCYAN_EX}Карты Дилера: {Fore.RESET}',
              self.dealer.hand.cards[0],
              f'{Fore.LIGHTBLACK_EX}<карта скрыта>{Fore.RESET}',
              sep='\n\t')
        print(f'{Fore.LIGHTGREEN_EX}Карты Игрока: {Fore.RESET}',
              *self.player.hand.cards, sep='\n\t')

    def show_all(self):
        print(f'\n{Fore.LIGHTCYAN_EX}Карты Дилера: {Fore.RESET}',
              *self.dealer.hand.cards, sep='\n\t')
        print(f'Сумма карт Дилера {self.dealer.hand.value}')
        print(f'{Fore.LIGHTGREEN_EX}Карты Игрока: {Fore.RESET}',
              *self.player.hand.cards, sep='\n\t')
        print(f'Сумма карт Игрока {self.player.hand.value}')

    def hit_or_stand(self, who):
        while True:
            choice = input('Взять доп.карту(hit) или остаться при текующих картах(stand).\nВведите h или s: ')

            match choice.lower():
                case 'h':
                    who.hit(self.deck)
                    self.show_some()
                case 's':
                    print('Игрок остается при текующих картах. Ход диллера')
                    self.playing = False

                    break
                case _:
                    print('Извините, ответ непонятен. Пожалуйста введите h или s')

    def player_busts(self):
        print('Превышение суммы 21 для Игрока!')
        self.player.lose_bet()

    def player_wins(self):
        print('\nИгрок выиграл!')
        self.player.win_bet()

    def dealer_busts(self):
        print('\nИгрок выиграл! Дилер превысил 21')
        self.player.win_bet()

    def dealer_wins(self):
        print('\nДилер выиграл')
        self.player.lose_bet()

    def push(self):
        print('\nНичья')


game = Blackjack()
game.start()
