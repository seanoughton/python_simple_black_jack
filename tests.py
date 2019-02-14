
import unittest
import black_jack
from black_jack import Game,Player,Dealer,Controller,View,Card,Deck,Chip,Hand

game = Game()
player = Player()
dealer = Dealer()
controller = Controller()
view = View()
card = Card()
deck = Deck()
chip = Chip(25)
hand = Hand()

class TestGame(unittest.TestCase):
#CAN CREATE CARDS
    def test_create_card(self):
        result = black_jack.Card()
        self.assertEqual(type(result),type(card))

#DECK TESTS
    def test_create_deck(self):
        result = black_jack.Deck()
        self.assertEqual(type(result),type(deck))

    #deck has 52 cards
    #deck is shuffled
    #deck can deal cards to a player




#CHIP TESTS
    def test_create_chip(self):
        result = black_jack.Chip(25)
        self.assertEqual(type(result),type(chip))

#HAND TESTS
    def test_create_hand(self):
        result = black_jack.Hand()
        self.assertEqual(type(result),type(hand))

    #hand busted
    #hand is black jack

#GAME TESTS
    def test_create_game(self):
        result = controller.game
        self.assertEqual(type(result),type(game))

#PLAYER TESTS
    def test_create_player(self):
        result = controller.player
        self.assertEqual(type(result),type(player))

#DEALER TESTS
    def test_create_dealer(self):
        result = controller.dealer
        self.assertEqual(type(result),type(dealer))

#VIEW TESTS
    def test_create_view(self):
        result = black_jack.View()
        self.assertEqual(type(result),type(view))

    # view can display the players hand: display_hand(hand,player)
    # view can display the dealers hand: display_hand(hand,dealer)
    # view can display won the game information: display_game_won(game,player,dealer)


#CONTROLLER TESTS
    def test_create_controller(self):
        result = black_jack.Controller()
        self.assertEqual(type(result),type(controller))

    # controller has game,player,dealer
    # controller can initialize a game :init_game()
    # controller initializes the player's play :player_play()
    # controller initializes the dealers's play :dealer_play()
    # controller initializes hand logic if hand is busted :check_bust()
    # controller initializes game logic if game is won: check_won()

    #controller GIVES PLAYER CHIPS
    #controller initailizes the PLAYER MAKES BET
    #controller DEAL CARDS (TO PLAYER AND DEALER)
    #controller SHOW CARDS ( DIFFERENT FOR DEALER VS PLAYER)
    #controller PLAYER HIT UNTIL STAY
    #controller CHECK FOR BUST OR WIN
    #controller DEALER HIT UNTIL 21 OR BUST
    #controller SHOW CARDS AND FINAL SCORE
    #controller ADJUST PLAYERS BANK (ADD OR REMOVE CHIPS)
    #controller ASK IF THE PLAYER WANTS TO PLAY AGAIN



if __name__ == '__main__':
    unittest.main()
