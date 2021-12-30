class Card:
    """
    A card has a suit and a strength.
    """
    card_names = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                  "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
    suit_names = ["Diamonds", "Hearts", "Spades", "Clubs"]

    def __init__(self, strength, suit):
        self.strength = strength
        self.suit = suit

    def __str__(self):
        return self.card_names[self.strength] + " of " + self.suit_names[self.suit]

