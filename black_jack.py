class Game:
    def __init__(self):
        self.deck = []
        self.player = {}
        self.dealer = {}

class Player:
  def __init__(self):
    self.chips = []
    self.hand = {}
    self.name = 'Player'

class Dealer:
    def __init__(self):
        self.hand = {}
        self.name = 'Dealer'

class Controller:
    def __init__(self):
        self.game = Game()
        self.player = Player()
        self.dealer = Dealer()

controller = Controller()
