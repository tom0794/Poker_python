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
        suit_char = ""
        if self.suit == 0:
            suit_char = "♦"
        elif self.suit == 1:
            suit_char = "♥"
        elif self.suit == 2:
            suit_char = "♠"
        elif self.suit == 3:
            suit_char = "♣"

        str_char = ""
        if self.strength < 8:
            str_char = " " + str(self.strength + 2)
        elif self.strength == 8:
            str_char = "10"
        elif self.strength == 9:
            str_char = " J"
        elif self.strength == 10:
            str_char = " Q"
        elif self.strength == 11:
            str_char = " K"
        elif self.strength == 12:
            str_char = " A"
        return str_char + suit_char
        # return self.card_names[self.strength] + " of " + self.suit_names[self.suit]

