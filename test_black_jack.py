import unittest
import black_jack
from black_jack import Game,Player,Dealer,Controller,View,Card,Deck,Chip,Hand

#CARD TESTS
class TestGame(unittest.TestCase):


    def test_hand_black_jack(self):
        game = Game()
        game.turn = 'Player'
        player = Player()
        dealer = Dealer()
        view = View()
        card1 = Card(suit='Clubs',value=(1,11),face='Ace')
        card2 = Card(suit='Clubs',value=(10),face='10')
        card3 = Card(suit='Clubs',value=(5),face='5')
        player.hand.cards.append(card1)
        player.hand.cards.append(card2)
        dealer.hand.cards.append(card1)
        dealer.hand.cards.append(card3)
        self.assertEqual(game.game_over(view,player,dealer),True)



if __name__ == '__main__':
    unittest.main()
