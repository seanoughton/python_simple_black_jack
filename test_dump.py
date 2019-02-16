







        #only displays one of the dealers cards at the beginning of the game
        def test_display_hand_dealer_beginning(self):
            view = View()
            dealer = Dealer()
            deck = Deck()
            deck.add_cards()
            cards = dealer.deal_cards(2,deck)
            dealer.hand.add_cards(cards)
            response = f"The Dealer's: \n"
            for card in dealer.hand.cards:
                response += f" {card.face} of {card.suit}\n"
            self.assertEqual(view.display_hand(dealer),response)
            del view,dealer,deck,cards,response




    # view can display won the game information: display_game_won(game,player,dealer)
