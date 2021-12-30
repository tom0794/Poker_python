from Card import Card


class Deck:

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for strength in range(13):
                new_card = Card(strength, suit)
                self.cards.append(new_card)



