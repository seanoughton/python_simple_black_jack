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
    def __init__(self,cards=[]):
        self.cards = cards

    def create_deck():
        pass

    def deal_cards():
        pass

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

class Dealer:
    def __init__(self):
        self.hand = {}
        self.name = 'Dealer'

    def hit():
        pass


class Game:
    def __init__(self):
        self.deck = []
        self.player = {}
        self.dealer = {}

    def won_test():
        pass


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



class View:
    def __init__(self):
        self.name = 'View'

    def display_hand():
        pass

    def display_game_won():
        pass




controller = Controller()
