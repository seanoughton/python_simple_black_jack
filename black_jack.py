import random
import os
clear = lambda: os.system('clear')

class Card:
    def __init__(self,suit="Hearts",value=2,face='2'):
        self.suit = suit
        self.value = value
        self.face = face

class Hand:
    def __init__(self,cards=[]):
        self.cards = cards

    def busted():
        pass

class Deck:
    def __init__(self,):
        self.cards = []

    def add_cards(self):
        suits = ['Spades','Hearts','Diamonds','Clubs']
        face_cards = ['Jack','Queen','King','Ace']
        for suit in suits:
          for i in range(2,11):
            card = Card(suit=suit,value=i,face=i)
            self.cards.append(card)
          for card in face_cards:
            if card == 'Ace':
              card = Card(suit=suit,value=(1,11),face=card)
            else:
              card = Card(suit=suit,value=10,face=card)
            self.cards.append(card)
        random.shuffle(self.cards)



    def deal_cards(self):
        pass

    def clear_deck(self):
        self.cards = []

    def __del__(self):
        self.cards = []


class Chip:
    def __init__(self,value):
        self.value = value

class Player:
    def __init__(self):
        self.chips = []
        self.hand = {}
        self.name = 'Player'

    def bet():
        pass

    def hit():
        pass

    def return_bank():
        return self.chips * 25

    def add_chips(num):
        pass

    def remove_chips(num):
        pass

    def __del__(self):
        self.chips = []
        self.hand = {}

class Dealer:
    def __init__(self):
        self.hand = {}
        self.name = 'Dealer'

    def hit():
        pass

    def __del__(self):
        self.hand = {}


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = {}
        self.dealer = {}

        self.deck.add_cards()

    def won_test():
        pass

    def __del__(self):
        self.deck = {}

class Controller:
    def __init__(self):
        self.game = Game()
        self.player = Player()
        self.dealer = Dealer()



    def init_game():
        pass
    def player_play():
        pass
    def dealer_play():
        pass
    def check_bust():
        pass
    def check_won():
        pass

    def __del__(self):
        self.game = {}
        self.player = {}
        self.dealer = {}



class View:
    def __init__(self):
        self.name = 'View'

    def display_hand():
        pass

    def display_game_won():
        pass

    def __del__(self):
        pass




controller = Controller()
