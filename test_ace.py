import unittest
# import black_jack
from black_jack import Hand,Card,Player

#CARD TESTS
class TestGame(unittest.TestCase):
    def test_has_ace(self):
        player = Player()
        player.bank.amount = 2500
        hand = Hand()
        card = Card(suit='Clubs',value=(1,11),face='Ace')
        hand.cards.append(card)
        self.assertEqual(hand.has_ace(),True)
        del hand
        del card

    def test_ace_hand_under_21_total(self):
        hand = Hand()
        card1 = Card(suit='Clubs',value=(1,11),face='Ace')
        card2 = Card(suit='Clubs',value=(2),face='2')
        card3 = Card(suit='Clubs',value=(5),face='5')
        hand.cards.append(card1)
        hand.cards.append(card2)
        hand.cards.append(card3)
        self.assertEqual(hand.total(),18)
        del hand

    def test_ace_hand_over_21_total(self):
        hand = Hand()
        card1 = Card(suit='Clubs',value=(1,11),face='Ace')
        card2 = Card(suit='Clubs',value=(5),face='5')
        card3 = Card(suit='Clubs',value=(5),face='5')
        hand.cards.append(card1)
        hand.cards.append(card2)
        hand.cards.append(card3)
        self.assertEqual(hand.total(),21)
        del hand


if __name__ == '__main__':
    unittest.main()
