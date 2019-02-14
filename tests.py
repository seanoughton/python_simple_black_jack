
import unittest
import black_jack
from black_jack import Game,Player,Dealer,Controller

game = Game()
player = Player()
dealer = Dealer()
controller = Controller()

class TestGame(unittest.TestCase):
    #CAN CREATE CONTROLLER
    def test_create_controller(self):
        result = controller
        self.assertEqual(type(result),type(controller))
    #CAN CREATE VIEW

    #CAN CREATE A GAME
    def test_create_game(self):
        result = controller.game
        self.assertEqual(type(result),type(game))

    #PLAYER AND DEALER ARE CREATED
    def test_create_player(self):
        result = controller.player
        self.assertEqual(type(result),type(player))

    def test_create_dealer(self):
        result = controller.dealer
        self.assertEqual(type(result),type(dealer))

    #CREATE CARDS
    #CREATE DECK
    #CREATE CHIPS
    #CREATE HAND


    #GIVE PLAYER CHIPS
    #PLAYER MAKES BET
    #DEAL CARDS (TO PLAYER AND DEALER)



if __name__ == '__main__':
    unittest.main()













# class TestCap(unittest.TestCase):
#
#     def test_one_word(self):
#         text = 'python'
#         result = black_jack.cap_text(text)
#         self.assertEqual(result, 'Python')
#
#     def test_multiple_words(self):
#         text = 'monty python'
#         result = black_jack.cap_text(text)
#         self.assertEqual(result, 'Monty Python')
