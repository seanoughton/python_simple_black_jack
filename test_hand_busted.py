import unittest
import black_jack
from black_jack import Game,Player,Dealer,Controller,View,Card,Deck,Chip,Hand

#CARD TESTS
class TestGame(unittest.TestCase):


    def test_hand_busted(self):
        game = Game()
        game.turn = 'Player'
        player = Player()
        dealer = Dealer()
        view = View()
        card1 = Card(suit='Clubs',value=(10),face='10')
        card2 = Card(suit='Clubs',value=(8),face='8')
        card3 = Card(suit='Clubs',value=(2),face='2')
        player.hand.cards.append(card1)
        player.hand.cards.append(card2)
        player.hand.cards.append(card3)
        # dealer.hand.cards.append(card1)
        # dealer.hand.cards.append(card3)
        self.assertEqual(player.hand.busted(),True)



if __name__ == '__main__':
    unittest.main()
