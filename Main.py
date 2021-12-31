from Card import Card
from Deck import Deck
import HandStrength
import random
import Increment


def convert_strength(value):
    if value == "A":
        return 12
    elif value == "K":
        return 11
    elif value == "Q":
        return 10
    elif value == "J":
        return 9
    elif value == "T":
        return 8
    else:
        return int(value) - 2


def convert_suit(value):
    if value == "D":
        return 0
    elif value == "H":
        return 1
    elif value == "S":
        return 2
    elif value == "C":
        return 3


def get_card_index(cards, strength, suit):
    for i in range(len(cards)):
        if cards[i].strength == strength and cards[i].suit == suit:
            return i
    return -1


if __name__ == '__main__':
    deck = Deck()

    while True:
        num_players = input("How many players? Enter 2-8: ")
        if num_players not in "2345678" or len(num_players) != 1:
            print("Invalid entry")
            continue
        num_players = int(num_players)

        player_hands = []
        for player_num in range(num_players):
            valid_entry = False
            current_player_hand = []
            while not valid_entry:
                card1 = input("Enter Player " + str(player_num + 1) + " first card: ")
                if len(card1) != 2 or card1[0] not in "23456789TJQKA" \
                        or card1[1] not in "DHSC":
                    print("Invalid card entry")
                    continue
                new_card1 = Card(convert_strength(card1[0]), convert_suit(card1[1]))
                card_index = get_card_index(deck.cards, new_card1.strength, new_card1.suit)
                if card_index == -1:
                    print("Card already dealt")
                    continue
                deck.cards.pop(card_index)

                while True:
                    card2 = input("Enter Player " + str(player_num + 1) + " second card: ")
                    if len(card2) != 2 or card2[0] not in "23456789TJQKA" or \
                            card2[1] not in "DHSC":
                        print("Invalid card entry")
                        continue
                    else:
                        new_card2 = Card(convert_strength(card2[0]), convert_suit(card2[1]))
                        card_index = get_card_index(deck.cards, new_card2.strength, new_card2.suit)
                        if card_index == -1:
                            print("Card already dealt")
                            continue
                        deck.cards.pop(card_index)
                        break
                valid_entry = True
                player_hands.append([new_card1, new_card2])
        for hand in player_hands:
            print(str(hand[0]) + " " + str(hand[1]))

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

    # player_hand = []
    # comm_cards = []
    #
    # for i in range(2):
    #     card_index = random.randrange(0, len(deck.cards) - 1)
    #     new_card = deck.cards[card_index]
    #     player_hand.append(new_card)
    #     deck.cards.remove(new_card)
    #
    # for i in range(5):
    #     card_index = random.randrange(0, len(deck.cards) - 1)
    #     new_card = deck.cards[card_index]
    #     comm_cards.append(new_card)
    #     deck.cards.remove(new_card)
    #
    # print(HandStrength.get_strength(player_hand, comm_cards))

    # index_list = [0, 1, 2, 3, 4]
    # print(index_list)
    # while index_list:
    #     index_list = Increment.increment_indices(index_list, len(deck.cards))
    #     print(index_list)

