import random
import os
clear = lambda: os.system('clear')

class Card:
    def __init__(self,suit="Hearts",value=2,face='2'):
        self.suit = suit
        self.value = value
        self.face = face

class Hand:
    def __init__(self):
        self.cards = []

    def has_ace(self):
        for card in self.cards:
          if card.face == 'Ace':
              return True
        return False

    def iterate_through_cards(self):
        total = [0,0]
        for card in self.cards:
          if card.face == 'Ace':
            x,y = card.value
            total[0] += (x + total[1])
            total[1] += y
          else:
            total[1] += card.value
        return total

    def total(self):
        total = self.iterate_through_cards()
        if self.has_ace() == False:
            return total[1]
        else:
            #IF THE 11 OPTION IS BUSTED RETURN THE 1 OPTION
            if total[1] > 21:
              return total[0]
            #IF THE 11 OPTION IS NOT BUSTED RETURN THE 11 OPTION
            if total[1] <= 21:
                return total[1]


    def busted(self):
        if self.total() > 21:
            return True
        else:
            return False

    def black_jack(self):
        if self.total() == 21:
            return True
        else:
            return False

    def __del__(self):
        self.cards = []





class Deck:
    def __init__(self):
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

    def get_cards(self,num):
        cards = []
        for i in range(0,num):
            cards.append(self.cards.pop())
        return cards

    def clear_deck(self):
        self.cards = []

    def __del__(self):
        self.cards = []


class Chip:
    def __init__(self,value):
        self.value = value

class Bank:
    def __init__(self):
        self.chips = []

    def add_chips(self,num,value):
        for i in range(0,num):
            chip = Chip(value)
            self.chips.append(chip)

    def subtract_chips(self,num,value):
        for i in range(0,num):
            self.chips.pop()


    def show_bank(self):
        amount = 0
        for chip in self.chips:
            amount += chip.value
        return amount


    def __del__(self):
        self.chips = []


class Player:
    def __init__(self):
        self.chips = []
        self.hand = {}
        self.name = 'Player'
        self.bank = Bank()

    def create_bank(self,num,value):
        self.bank.add_chips(num,value)

    def bet(self,value):
        #check to make sure that the player has enough in the bank to make the bet
        #if so, return the value
        #else, return an error message
        if value <= self.bank.show_bank():
            return value
        else:
            return False



    def __del__(self):
        self.hand = {}
        self.bank = {}

class Dealer:
    def __init__(self):
        self.hand = {}
        self.name = 'Dealer'

    def deal_cards(self,num,deck):
        return deck.get_cards(2)

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
