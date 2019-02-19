
import unittest
import black_jack
from black_jack import Game,Player,Dealer,Controller,View,Card,Deck,Chip,Hand


class TestGame(unittest.TestCase):


#HAND TESTS
    # def test_create_hand(self):
    #     hand = Hand()
    #     result = black_jack.Hand()
    #     self.assertEqual(type(result),type(hand))
    #     del hand

    # def test_has_ace(self):
    #     hand = Hand()
    #     card = Card(suit='Clubs',value=(1,11),face='Ace')
    #     hand.cards.append(card)
    #     # self.assertEqual(hand.has_ace(),True)
    #     del hand
    #     del card

    #hand returns total
    # def test_hand_total(self):
    #     hand = Hand()
    #     card = Card(suit='Hearts',value=10,face='Jack')
    #     hand.cards.append(card)
    #     hand.cards.append(card)
    #     hand.cards.append(card)
    #     self.assertEqual(hand.total(),30)
    #     del hand
    #     del card


    #hand busted
    def test_hand_busted(self):
        hand = Hand()
        card = Card(suit='Hearts',value=10,face='Jack')
        hand.cards.append(card)
        hand.cards.append(card)
        hand.cards.append(card)
        self.assertEqual(hand.busted(),True)
        del hand
        del card

    #hand is black jack
    def test_hand_black_jack(self):
        hand = Hand()
        jack = Card(suit='Hearts',value=10,face='Jack')
        nine = Card(suit='Hearts',value=9,face='9')
        two = Card(suit='Hearts',value=2,face='2')
        ace = Card(suit='Hearts',value=(1,11),face='Ace')
        hand.cards.append(jack)
        hand.cards.append(ace)
        # hand.cards.append(two)
        self.assertEqual(hand.black_jack(),True)
        del hand




if __name__ == '__main__':
    unittest.main()
