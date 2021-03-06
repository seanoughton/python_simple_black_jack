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
        self.total = 0

    def add_cards(self,new_cards):
        self.cards += new_cards

    def get_total(self):
        total_options = self.iterate_through_cards()
        if self.hand_has_ace() == False:
            self.total = total_options[1]
        else:
            self.total = self.ace_score_options(total_options)

    #IF THE 11 OPTION IS BUSTED RETURN THE 1 OPTION
    #IF THE 11 OPTION IS NOT BUSTED RETURN THE 11 OPTION
    def ace_score_options(self,total_options):
        if total_options[1] > 21:
            return total_options[0]
        else:
            return total_options[1]

    def hand_has_ace(self):
        for card in self.cards:
          if self.is_ace(card) == True:
              return True
        return False

    def is_ace(self,card):
        return card.face == 'Ace'

    def iterate_through_cards(self):
        total_options = [0,0]
        for card in self.cards:
          total_options = self.add_hand_total(card,total_options)
        return total_options

    def add_hand_total(self,card,total_options):
        if self.is_ace(card) == True:
            self.card_is_ace(card,total_options)
        else:
            self.card_not_ace(card,total_options)
        return total_options

    def card_is_ace(self,card,total_options):
        x,y = card.value
        total_options[0] += x
        total_options[1] += y
        return total_options

    def card_not_ace(self,card,total_options):
        total_options[0] += card.value
        total_options[1] += card.value
        return total_options

    def busted(self):
        self.get_total()
        return self.total > 21

    def black_jack(self):
        self.get_total()
        return self.total == 21

    def clear(self):
        self.cards = []

    def __del__(self):
        self.cards = []



class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ['Spades','Hearts','Diamonds','Clubs']
        self.faces = ['Jack','Queen','King','Ace']

    def add_cards(self):
        self.iterate_through_suits()
        self.shuffle_deck()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def iterate_through_suits(self):
        for suit in self.suits:
            self.add_non_face_cards(suit)
            self.add_face_cards(suit)

    def add_non_face_cards(self,suit):
      for i in range(2,11):
        card = Card(suit=suit,value=i,face=i)
        self.cards.append(card)

    def add_face_cards(self,suit):
        for face in self.faces:
          self.cards.append(self.test_face(face,suit))

    def test_face(self,face,suit):
        if face == 'Ace':
          return Card(suit=suit,value=(1,11),face=face)
        else:
          return Card(suit=suit,value=10,face=face)

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
        self.amount = 0

    def add(self,num):
        self.amount += num

    def remove(self,num):
        self.amount -= num

    # def add_chips(self,bet,value=25):
    #     num = int(bet/25)
    #     for i in range(0,num):
    #         chip = Chip(value)
    #         self.chips.append(chip)
    #
    # def subtract_chips(self,bet,value=25):
    #     num = int(bet/25)
    #     for i in range(0,num):
    #         self.chips.pop()


    # def show_bank(self):
    #     amount = 0
    #     for chip in self.chips:
    #         amount += chip.value
    #     return amount


    def __del__(self):
        self.chips = []


class Player:
    def __init__(self):
        self.chips = []
        self.hand = Hand()
        self.name = 'Player'
        self.bank = Bank()
        self.black_jack = False

    def create_bank(self,num):
        # self.bank.add_chips(num,value)
        self.bank.add(num)

    def enough_for_bet(self,value):
        if self.bank.amount < value or value < 1:
            return False
        else:
            return True

    def bet(self,view):
        value = 0
        while self.enough_for_bet(value) == False:
            value = view.place_bet()
        return value


    def __del__(self):
        self.hand = Hand()
        self.bank = Bank()

class Dealer:
    def __init__(self):
        self.hand = Hand()
        self.name = 'Dealer'
        self.black_jack = False

    def deal_cards(self,num,deck):
        return deck.cards_out(num)

    def __del__(self):
        self.hand = Hand()


class Game:
    def __init__(self):
        self.deck = Deck()
        self.bet = 0
        self.deck.add_cards()
        self.turn = 'Player'
        self.over = False
        self.winner = {}


    def has_black_jack(self):
        pass

    def player_play(self,view,player,dealer):
        response = view.hit()
        self.hit_until_stay(view,player,dealer)
        # while response == True:
        #     player_cards = dealer.deal_cards(1,self.deck)
        #     player.hand.add_cards(player_cards)
        #
        #     if self.game_over(view,player,dealer) == True:
        #         break
        #     else:
        #         view.display_hand(player)
        #
        #     response = view.hit()

        self.turn = "Dealer"

    def hit_until_stay(self,view,player,dealer):
        while response == True:
            player_cards = dealer.deal_cards(1,self.deck)
            player.hand.add_cards(player_cards)

            if self.game_over(view,player,dealer) == True:
                break
            else:
                view.display_hand(player)
            response = view.hit()


    def dealer_play(self,view,player,dealer):
        while dealer.hand.total() < 21:
            dealer_card = dealer.deal_cards(1,self.deck)
            dealer.hand.add_cards(dealer_card)

            if self.game_over(view,player,dealer) == True:
                break


    def game_over(self,view,player,dealer):
        response = False
        if self.turn == 'Player':
            if player.hand.busted() == True:
                self.winner = dealer
                response = True
            if player.hand.black_jack() == True:
                self.winner = player
                player.black_jack = True
                response =  True

        if self.turn == "Dealer":
            if dealer.hand.busted() == True:
                self.winner = player
                response = True
            elif dealer.hand.black_jack() == True:
                self.winner = dealer
                dealer.black_jack = True
                response = True
            elif player.hand.total() < dealer.hand.total():
                self.winner = dealer
                response =  True


        if response == True:
            self.over = True
            if self.winner == player:
                player.bank.add(self.bet)
            if self.winner == dealer:
                player.bank.remove(self.bet)
            view.display_game_over(winner=self.winner,player=player,dealer=dealer)


        return response



    def __del__(self):
        self.deck = Deck()

class Controller:
    def __init__(self):
        self.game = Game()
        self.player = Player()
        self.dealer = Dealer()
        self.view = View()

        self.player.create_bank(2500)


    def init_game(self):
        clear()
        #PLAYER SETUP
        self.game = Game()
        self.player.hand.clear()
        self.dealer.hand.clear()
        self.view.display_bank(self.player)
        self.game.bet = self.player.bet(view=self.view)

        clear()
        #DEAL CARDS
        player_cards = self.dealer.deal_cards(2,self.game.deck)
        self.player.hand.add_cards(player_cards)

        dealer_cards = self.dealer.deal_cards(2,self.game.deck)
        self.dealer.hand.add_cards(dealer_cards)

        #SHOW CARDS (player all, dealer one)
        self.view.display_hand(self.player)
        self.view.display_hand(self.dealer)

        self.game.player_play(view=self.view,player=self.player,dealer=self.dealer)

        if self.game.over == False:
            self.game.dealer_play(view=self.view,player=self.player,dealer=self.dealer)


        self.play_again()


    def play_again(self):
        response = self.get_input()
        if response == 'Y' or response =='y':
            self.init_game()
        if response == 'N' or response =='n':
            print('GoodBye!')
            return

    def get_input(self):
        response = ''
        while response not in ['Y','y','N','n']:
          response = input('Would you like to play again?(Y/N)\n')
        return response





    def __del__(self):
        self.game = Game()
        self.player = Player()
        self.dealer = Dealer()



class View:
    def __init__(self):
        self.name = 'View'

    def display_bank(self,player):
        print (f'Your Bank is: {player.bank.amount}')

    def place_bet(self):
        #ADD ERROR CHECKING FOR IF THEY ENTER SOMETHING OTHER THAN A NUMBER
        return int(input("Place your bet: \n"))

    def display_hand(self,player):
        if player.name == 'Player':
            response = f'Your Hand is: \n'
            for card in player.hand.cards:
                response += f" {card.face} of {card.suit}\n"
        else:
            response = f"The Dealer's Hand is: \n"
            for card in player.hand.cards:
                response += f" {card.face} of {card.suit}\n"

        print(response)

    def display_busted(self,game_player):
        if game_player.name == "Player":
            print('You Busted!')
        else:
            print ('Dealer Busted')

    def hit(self):
        response = ''
        while response not in ['H','h','S','s']:
          response = input('Would you like to hit or stay?(H/S)\n')
        if response == 'H' or response =='h':
          return True
        else:
          return False

    def display_game_over(self,winner,player,dealer):
        clear()
        if player.hand.busted() == True:
            self.display_busted(player)
        if dealer.hand.busted() == True:
            self.display_busted(dealer)

        print(f'{winner.name} is the Winner!\n')
        if player.black_jack == True or dealer.black_jack == True:
            print('BLACK JACK!!!')
        self.display_hand(dealer)
        self.display_hand(player)
        print(f'Your bank is now {self.display_bank(player)}')



    def __del__(self):
        pass


#
# controller = Controller()
# controller.init_game()
