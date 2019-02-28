
import unittest
import black_jack
from black_jack import Game,Player,Dealer,Controller,View,Card,Deck,Chip,Hand

#CARD TESTS
class TestGame(unittest.TestCase):


#DECK TESTS
    def test_create_deck(self):
        deck = Deck()
        deck.add_cards()
        self.assertEqual(type(deck.cards),type([]))
        del deck


    def test_deck_size(self):
        deck = Deck()
        deck.add_cards()
        result = deck.cards
        self.assertEqual(len(result),52)
        del deck

    # def test_deck_shuffled(self):
    #     deck = Deck()
    #     deck.add_cards()
    #     first_suit = deck.cards[0]
    #     second_suit = deck.cards[14]
    #     #NEED A BETTER SOLUTION FOR THIS BECAUSE RANDOMLY THESE VALUES WILL BE THE SAME
    #     self.assertNotEqual(first_suit.value,second_suit.value)
    #     del deck

    def test_cards_out(self):
        deck = Deck()
        deck.add_cards()
        self.assertIsInstance((deck.cards_out(2)[0]),Card)
        del deck




if __name__ == '__main__':
    unittest.main()
