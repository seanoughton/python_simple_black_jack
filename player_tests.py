
import unittest
import black_jack
from black_jack import Game,Player,Dealer,Controller,View,Card,Deck,Chip,Hand

#CARD TESTS
class TestGame(unittest.TestCase):
    # def test_create_card(self):
    #     result = black_jack.Card()
    #     self.assertEqual(type(result),type(Card()))

#DECK TESTS





#HAND TESTS



    #hand busted
    # def test_hand_busted(self):
    #     hand = Hand()
    #     card = Card(suit='Hearts',value=10,face='Jack')
    #     hand.cards.append(card)
    #     hand.cards.append(card)
    #     hand.cards.append(card)
    #     self.assertEqual(hand.busted(),True)
    #     del hand
    #     del card

    #hand is black jack
    # def test_hand_black_jack(self):
    #     hand = Hand()
    #     jack = Card(suit='Hearts',value=10,face='Jack')
    #     nine = Card(suit='Hearts',value=9,face='9')
    #     two = Card(suit='Hearts',value=2,face='2')
    #     ace = Card(suit='Hearts',value=(1,11),face='Ace')
    #     hand.cards.append(jack)
    #     hand.cards.append(ace)
    #     # hand.cards.append(two)
    #     self.assertEqual(hand.black_jack(),True)
    #     del hand







#PLAYER TESTS
    def test_create_player(self):
        player = Player()
        player_test = black_jack.Player()
        self.assertEqual(type(player_test),type(player))
        del player, player_test

    def test_bet_approved(self):
        player = Player()
        view = View()
        player.create_bank(2500)
        bet = player.bet(100)
        self.assertEqual(bet,100)
        del player
    #
    def test_bet_refused(self):
        player = Player()
        view = View()
        player.create_bank(50)
        self.assertEqual(player.bet(1000),False)
        del player


#DEALER TESTS
    # def test_create_dealer(self):
    #     dealer = Dealer()
    #     dealer_test = black_jack.Dealer()
    #     self.assertEqual(type(dealer_test),type(dealer))
    #     del dealer,dealer_test
    #
    # def test_deal_cards(self):
    #     dealer = Dealer()
    #     deck = Deck()
    #     deck.add_cards()
    #     cards = dealer.deal_cards(2,deck)
    #     self.assertIsInstance(cards[0],Card)
    #     del dealer
    #
    # def test_player_recieves_dealt_cards(self):
    #     dealer = Dealer()
    #     deck = Deck()
    #     deck.add_cards()
    #     cards = dealer.deal_cards(2,deck)
    #     player = Player()
    #     player.hand.cards += cards
    #     self.assertEqual(len(player.hand.cards),2)
    #     del dealer

#CONTROLLER TESTS
    # def test_create_controller(self):
    #     controller = Controller()
    #     controller_test = black_jack.Controller()
    #     self.assertEqual(type(controller_test),type(controller))
    #     del controller,controller_test
    #
    # # controller has game,player,dealer
    # def test_has_game_player_dealer_view(self):
    #     controller = Controller()
    #     self.assertIsInstance(controller.game,Game)
    #     self.assertEqual(controller.player.name,'Player')
    #     self.assertIsInstance(controller.dealer,Dealer)
    #     self.assertIsInstance(controller.view,View)
    #     del controller
    #
    #
    # def test_has_game_player_dealer_deck(self):
    #     controller = Controller()
    #     self.assertIsInstance(controller.game,Game)
    #     del controller

        # controller can initialize a game :init_game()

    # def test_game_init_has_bank_(self):
    #     controller = Controller()
    #     controller.init_game()
    #     self.assertEqual(controller.player.bank.show_bank(),2500)
    #     del controller
    #
    # def test_game_init_player_bet(self):
    #     controller = Controller()
    #     controller.init_game()
    #     self.assertEqual(controller.game.bet,100)
    #     del controller
    #
    # def test_game_init_deal_cards(self):
    #     controller = Controller()
    #     controller.init_game()
    #     self.assertEqual(len(controller.player.hand.cards),2)
    #     self.assertEqual(len(controller.dealer.hand.cards),2)
    #     del controller
    #


# controller initializes the player's play :player_play()
    # def test_game_player_play(self):
    #     controller = Controller()
    #     controller.init_game()
    #     #HIT 1 TIMES
    #     self.assertEqual(len(controller.player.hand.cards),2)
    #     del controller


    # controller initializes the dealers's play :dealer_play()
    # def test_game_dealer_play(self):
    #     controller = Controller()
    #     controller.init_game()
    #     self.assertGreater(controller.dealer.hand.total(),20)
    #     del controller
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

#VIEW TESTS
    # def test_create_view(self):
    #     view = View()
    #     view_test = black_jack.View()
    #     self.assertEqual(type(view_test),type(view))
    #     del view,view_test

    # def test_display_hand_player(self):
    #     view = View()
    #     dealer = Dealer()
    #     deck = Deck()
    #     deck.add_cards()
    #     cards = dealer.deal_cards(2,deck)
    #     player = Player()
    #     player.hand.add_cards(cards)
    #     response = f'Your hand is: \n'
    #     for card in player.hand.cards:
    #         response += f" {card.face} of {card.suit}\n"
    #     self.assertEqual(view.display_hand(player),response)
    #     del view,dealer,deck,cards,player,response

    # def test_display_hand_dealer(self):
    #     view = View()
    #     dealer = Dealer()
    #     deck = Deck()
    #     deck.add_cards()
    #     cards = dealer.deal_cards(2,deck)
    #     dealer.hand.add_cards(cards)
    #     response = f"The Dealer's: \n"
    #     for card in dealer.hand.cards:
    #         response += f" {card.face} of {card.suit}\n"
    #     self.assertEqual(view.display_hand(dealer),response)
    #     del view,dealer,deck,cards,response

    # def test_display_player_hit(self):
    #     view = View()
    #     player = Player()
    #     dealer = Dealer()
    #     deck = Deck()
    #     deck.add_cards()
    #     cards = dealer.deal_cards(2,deck)
    #     player.hand.add_cards(cards)
    #     self.assertEqual(view.hit(),True)
    #     del view,player,dealer,deck,cards

    # def test_display_busted(self):
    #     view = View()
    #     self.assertEqual(view.display_busted(),'You Busted!')
    #     del view

    # def test_display_bank(self):
    #     view = View()
    #     player = Player()
    #     player.create_bank(100,25)
    #     self.assertEqual(view.display_bank(player),f'Your Bank is: {player.bank.show_bank()}')
    #     del view,player





if __name__ == '__main__':
    unittest.main()
