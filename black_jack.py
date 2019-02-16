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

    def add_cards(self,new_cards):
        self.cards += new_cards

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

    def cards_out(self,num):
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
        self.hand = Hand()
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
        self.hand = Hand()
        self.name = 'Dealer'

    def deal_cards(self,num,deck):
        return deck.cards_out(num)

    def __del__(self):
        self.hand = Hand()


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
        self.bet = 0
        self.deck.add_cards()

    def won_test():
        pass

    def __del__(self):
        self.deck = Deck()

class Controller:
    def __init__(self):
        self.game = Game()
        self.player = Player()
        self.dealer = Dealer()
        self.view = View()



    def init_game(self):
        #add money to the players bank
        self.player.create_bank(100,25)



        # ASK THE PLAYER TO BET AND VALIDATE THE BET AMOUNT
        value = self.view.place_bet()
        while self.player.bet(value) == False:
            value = self.view.place_bet()
        else:
            self.game.bet = value

        #DEAL CARDS
        player_cards = self.dealer.deal_cards(2,self.game.deck)
        self.player.hand.add_cards(player_cards)

        dealer_cards = self.dealer.deal_cards(2,self.game.deck)
        self.dealer.hand.add_cards(dealer_cards)

        #show cards (player all, dealer one)
        print(self.view.display_bank(self.player))
        print(self.view.display_hand(self.player))
        print(self.view.display_hand(self.dealer))

        self.player_play()
        self.dealer_play()
        self.check_won()



    def player_play(self):
        response = True
        while response == True:
            response = self.view.hit()
            if response == True:
                player_cards = self.dealer.deal_cards(1,self.game.deck)
                self.player.hand.add_cards(player_cards)
            if self.player.hand.busted() == True:
                self.view.display_busted()
                break
            if self.player.hand.black_jack() == True:
                self.view.display_game_over(self.player,self.dealer)
                break

    def dealer_play(self):
        while self.dealer.hand.total() < 21:
            dealer_card = self.dealer.deal_cards(1,self.game.deck)
            self.dealer.hand.add_cards(dealer_card)
            if self.dealer.hand.busted() == True:
                self.view.display_busted(self.dealer)
                break
            if self.dealer.hand.black_jack() == True:
                self.view.display_game_over(self.player,self.dealer)
                break

    def check_won(self):
        winner = {}
        if self.player.hand.total() > self.dealer.hand.total():
            winner = self.player
            num = self.bet/25
            self.player.bank.add_chips(num,25)
        else:
            winner = self.dealer
        self.view.display_game_over(winner,self.player,self.dealer)



    def __del__(self):
        self.game = Game()
        self.player = Player()
        self.dealer = Dealer()



class View:
    def __init__(self):
        self.name = 'View'

    def display_bank(self,player):
        return f'Your Bank is: {player.bank.show_bank()}'

    def place_bet(self):
        #ADD ERROR CHECKING FOR IF THEY ENTER SOMETHING OTHER THAN A NUMBER
        return int(input("Place your bet"))

    def display_hand(self,player):
        if player.name == 'Player':
            response = f'Your hand is: \n'
            for card in player.hand.cards:
                response += f" {card.face} of {card.suit}\n"
        else:
            response = f"The Dealer's: \n"
            for card in player.hand.cards:
                response += f" {card.face} of {card.suit}\n"

        return response

    def display_busted(self,game_player):
        if game_player.name == "Player":
            return 'You Busted!'
        else:
            return 'Dealer Busted'

    def hit(self):
        response = ''
        while response not in ['H','h','S','s']:
          response = input('Would you like to hit or stay?(H/S)\n')
        if response == 'H' or response =='h':
          return True
        else:
          return False

    def display_game_over(self,winner,player,dealer):
        return f'{winner.name} is the Winner!\n Your bank is now {self.display_bank(player)}'



    def __del__(self):
        pass




controller = Controller()
