def sort_key(card):
    return card.strength


def get_strength(player_hand, comm_cards):
    hand = []
    for card in player_hand:
        hand.append(card)
    for card in comm_cards:
        hand.append(card)
    hand.sort(key=sort_key)

    # check for flush and straight flush
    flush = check_flush(hand)
    if flush != -1:
        for card in hand:
            if card.suit != flush:
                hand.remove(card)
        straight_flush = check_straight(hand)
        if straight_flush != -1:
            return get_straight_flush_strength(straight_flush)
        else:
            return get_flush_strength(hand, flush)

    # check for straight
    straight = check_straight(hand)
    if straight != -1:
        return get_straight_strength(straight)

    # check for quads
    quads = check_quads(hand)
    if quads != -1:
        return get_quads_strength(hand, quads)

    # find trips and pairs
    trips = check_trips(hand)
    pairs = check_pairs(hand)

    # check for full house
    if len(trips) > 0 and len(pairs) > 0 or len(trips) >= 2:
        if len(trips) == 1:
            return "6" + convert_to_hex(trips[0]) + convert_to_hex(pairs[0])
        else:
            return "6" + convert_to_hex(trips[0]) + convert_to_hex(trips[1])

    # check for trips
    if len(trips) == 1:
        return get_trips_strength(hand, trips)

    # check for two pair
    if len(pairs) >= 2:
        return get_two_pair_strength(hand, pairs)

    # check for one pair
    if len(pairs) == 1:
        return get_pair_strength(hand, pairs)

    # return high card
    return get_high_card_strength(hand)


def get_diffs(hand):
    diffs = [-1, -1, -1, -1, -1, -1, -1]
    for index in range(len(hand)):
        if index > 0:
            diffs[index] = hand[index].strength - hand[index - 1].strength
    return diffs


# Consumes a sorted list of 7 cards. If any suit occurs 5 or more times in the hand, returns
# that suit value, otherwise returns -1.
def check_flush(hand):
    """
    Consumes a sorted 7 card hand and checks for a flush
    :param hand: Sorted list of 7 cards
    :return: The suit number of the flush if present,
    returns -1 if no flush
    """
    suit_counts = [0, 0, 0, 0]
    for card in hand:
        suit_counts[card.suit] += 1

    for suit_num in range(len(suit_counts)):
        if suit_counts[suit_num] >= 5:
            return suit_num
    return -1


# Consumes a sorted list of 7 cards. If the hand contains a sequence of least 5 cards wherein
# the strength of each card in the sequence is one greater than the previous, returns the value
# of the largest strength in the sequence. Returns 3 if the hand contains the cards 2, 3, 4, 5, A.
# Returns -1 if no straight is found.
def check_straight(hand):
    """
    Consumes a sorted 7 card hand and checks if it contains a straight
    :param hand: Sorted list of 7 cards.
    :return: Strength of the strongest card in the straight if found,
    otherwise -1.
    """
    diffs = get_diffs(hand)
    card_strengths = []
    for card in hand:
        card_strengths.append(card.strength)
    counter = 0
    longest = 0
    strength = 0
    for index in range(len(hand)):
        if diffs[index] == 1:
            counter += 1
            if counter > longest:
                longest = counter
                strength = card_strengths[index]
        elif diffs[index] != 0:
            counter = 0
    if longest >= 4:
        return strength
    if card_strengths.count(12) >= 1 and card_strengths.count(0) >= 1 and card_strengths.count(1) >= 1 and \
            card_strengths.count(2) >= 1 and card_strengths.count(3) >= 1:
        return 3
    return -1


def check_quads(hand):
    """
    Consumes a sorted 7 card hand and checks if it contains four of a kind
    :param hand: Sorted list of 7 cards.
    :return: Strength of four of a kind card if present, otherwise -1.
    """
    diffs = get_diffs(hand)
    counter = 0
    for index in range(1, len(hand)):
        if diffs[index] == 0:
            counter += 1
        else:
            counter = 0
        if counter == 3:
            return hand[index].strength
    return -1


def check_trips(hand):
    """
    Consumes a sorted 7 card hand and returns every instance of trips
    :param hand: Sorted list of 7 cards.
    :return: Strength of trips card(s) in descending list, empty
    list if none found
    """
    diffs = get_diffs(hand)
    counter = 0
    trips = []
    for index in range(1, len(hand)):
        if diffs[index] == 0:
            counter += 1
        else:
            counter = 0
        if counter == 2:
            trips.append(hand[index].strength)
            counter = 0
    trips.sort(reverse=True)
    return trips


def check_pairs(hand):
    """
    Consumes a sorted 7 card hand and returns each pair strength
    :param hand: Sorted list of 7 cards
    :return: A list with the strength of each pair found, empty
    if no pairs
    """
    diffs = get_diffs(hand)
    pairs = []
    for index in range(1, len(hand)):
        if diffs[index] == 0 and index < len(diffs) - 1 \
                and diffs[index + 1] != 0 and diffs[index - 1] != 0:
            pairs.append(hand[index].strength)
        elif index == 6 and diffs[index] == 0 and diffs[index - 1] != 0:
            pairs.append(hand[index].strength)
    pairs.sort(reverse=True)
    return pairs


def convert_to_hex(number):
    if number == 10:
        return "A"
    if number == 11:
        return "B"
    if number == 12:
        return "C"
    return str(number)


def get_straight_flush_strength(strength):
    return "8" + convert_to_hex(strength)


def get_flush_strength(hand, suit):
    result = "5"
    for index in range(len(hand) - 1, -1, -1):
        if hand[index].suit == suit:
            result += convert_to_hex(hand[index].strength)
        if len(result) == 6:
            break
    return result


def get_straight_strength(strength):
    return "4" + convert_to_hex(strength)


def get_quads_strength(hand, quad_card):
    result = "7" + convert_to_hex(quad_card)
    for index in range(len(hand) - 1, -1, -1):
        if hand[index].strength != quad_card:
            result += convert_to_hex(hand[index].strength)
        if len(result) == 3:
            break
    return result


def get_trips_strength(hand, trips):
    result = "3" + convert_to_hex(trips[0])
    for index in range(len(hand) - 1, -1, -1):
        if hand[index].strength != trips[0]:
            result += convert_to_hex(hand[index].strength)
        if len(result) == 4:
            break
    return result


def get_two_pair_strength(hand, pairs):
    result = "2" + convert_to_hex(pairs[0]) + convert_to_hex(pairs[1])
    for index in range(len(hand) - 1, -1, -1):
        if hand[index].strength != pairs[0] and hand[index].strength != pairs[1]:
            result += convert_to_hex(hand[index].strength)
        if len(result) == 4:
            break
    return result


def get_pair_strength(hand, pairs):
    result = "1" + convert_to_hex(pairs[0])
    for index in range(len(hand) - 1, -1, -1):
        if hand[index].strength != pairs[0]:
            result += convert_to_hex(hand[index].strength)
        if len(result) == 5:
            break
    return result


def get_high_card_strength(hand):
    result = "0"
    for index in range(len(hand) - 1, -1, -1):
        result += convert_to_hex(hand[index].strength)
        if len(result) == 6:
            break
    return result
