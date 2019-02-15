
import unittest
import black_jack
from black_jack import Game,Player,Dealer,Controller,View,Card,Deck,Chip,Hand

#CARD TESTS
class TestGame(unittest.TestCase):
    def test_create_card(self):
        result = black_jack.Card()
        self.assertEqual(type(result),type(Card()))

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

    def test_deck_shuffled(self):
        deck = Deck()
        deck.add_cards()
        first_suit = deck.cards[0]
        second_suit = deck.cards[14]
        #NEED A BETTER SOLUTION FOR THIS BECAUSE RANDOMLY THESE VALUES WILL BE THE SAME
        self.assertNotEqual(first_suit.value,second_suit.value)
        del deck


#CHIP TESTS
    def test_create_chip(self):
        chip = Chip(25)
        result = black_jack.Chip(25)
        self.assertEqual(type(result),type(chip))
        chip = {}

#HAND TESTS
    def test_create_hand(self):
        hand = Hand()
        result = black_jack.Hand()
        self.assertEqual(type(result),type(hand))
        del hand

    def test_has_ace(self):
        hand = Hand()
        card = Card(suit='Clubs',value=(1,11),face='Ace')
        hand.cards.append(card)
        self.assertEqual(hand.has_ace(),True)
        del hand
        del card

    #hand returns total
    def test_hand_total(self):
        hand = Hand()
        card = Card(suit='Hearts',value=10,face='Jack')
        hand.cards.append(card)
        hand.cards.append(card)
        hand.cards.append(card)
        self.assertEqual(hand.total(),30)
        del hand
        del card


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

#GAME TESTS
    def test_create_game(self):
        game = Game()
        self.assertEqual(type(game.deck.cards),type([]))
        del game

#PLAYER TESTS
    def test_create_player(self):
        player = Player()
        player_test = black_jack.Player()
        self.assertEqual(type(player_test),type(player))
        del player, player_test

#DEALER TESTS
    def test_create_dealer(self):
        dealer = Dealer()
        dealer_test = black_jack.Dealer()
        self.assertEqual(type(dealer_test),type(dealer))
        del dealer,dealer_test

    #dealer can deal cards to a player

#VIEW TESTS
    def test_create_view(self):
        view = View()
        view_test = black_jack.View()
        self.assertEqual(type(view_test),type(view))
        del view,view_test

    # view can display the players hand: display_hand(hand,player)
    # view can display the dealers hand: display_hand(hand,dealer)
    # view can display won the game information: display_game_won(game,player,dealer)

#CONTROLLER TESTS
    def test_create_controller(self):
        controller = Controller()
        controller_test = black_jack.Controller()
        self.assertEqual(type(controller_test),type(controller))
        del controller,controller_test

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
