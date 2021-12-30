from Card import Card
from Deck import Deck
import HandStrength
import random

if __name__ == '__main__':
    deck = Deck()
    # while True:
    #     num_players = input("How many players? Enter 2-8: ")
    #     if num_players not in "2345678" or len(num_players) != 1:
    #         print("Invalid entry")
    #         continue
    #     num_players = int(num_players)
    # card1 = Card(3, 3)
    # card2 = Card(6, 2)
    # card3 = Card(7, 1)
    # card4 = Card(11, 1)
    # card5 = Card(4, 3)
    # card6 = Card(0, 0)
    # card7 = Card(9, 2)

    # player_hand = [card1, card2]
    # comm_cards = [card3, card4, card5, card6, card7]
    # full_hand = HandStrength.get_strength(player_hand, comm_cards)

    player_hand = []
    comm_cards = []

    for i in range(2):
        card_index = random.randrange(0, len(deck.cards) - 1)
        new_card = deck.cards[card_index]
        player_hand.append(new_card)
        deck.cards.remove(new_card)

    for i in range(5):
        card_index = random.randrange(0, len(deck.cards) - 1)
        new_card = deck.cards[card_index]
        comm_cards.append(new_card)
        deck.cards.remove(new_card)

    print(HandStrength.get_strength(player_hand, comm_cards))
