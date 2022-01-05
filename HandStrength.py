def sort_key(card):
    return card.strength


def get_strength(player_hand, comm_cards):
    """
    Calculates the strength of the best hand that can be formed using
    the player's hand and the community cards.
    :param player_hand: List of 2 cards
    :param comm_cards: List of 5 cards
    :return: String representing the strength of the hand
    """
    hand = []
    for card in player_hand:
        hand.append(card)
    for card in comm_cards:
        hand.append(card)
    hand.sort(key=sort_key)
    diffs = get_diffs(hand)

    # check for flush and straight flush
    flush = check_flush(hand)
    if flush != -1:
        copy = []
        for card in hand:
            copy.append(card)
        for card in copy:
            if card.suit != flush:
                hand.remove(card)
        diffs = get_diffs(hand)
        straight_flush = check_straight(hand, diffs)
        if straight_flush != -1:
            return get_straight_flush_strength(straight_flush)
        else:
            return get_flush_strength(hand, flush)

    # check for straight
    straight = check_straight(hand, diffs)
    if straight != -1:
        return get_straight_strength(straight)

    # check for quads
    quads = check_quads(hand, diffs)
    if quads != -1:
        return get_quads_strength(hand, quads)

    # find trips and pairs
    trips = check_trips(hand, diffs)
    pairs = check_pairs(hand, diffs)

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
    """
    Consumes a sorted hand and returns a list of first differences
    :param hand: List of sorted cards
    :return: List of first difference integers
    """
    diffs = []
    for i in hand:
        diffs.append(-1)
    for index in range(len(hand)):
        if index > 0:
            diffs[index] = hand[index].strength - hand[index - 1].strength
    return diffs


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


def check_straight(hand, diffs):
    """
    Consumes a sorted 7 card hand and checks if it contains a straight.
    Accounts for the case where a 5-high straight is formed using an Ace.
    :param hand: Sorted list of 7 cards
    :param diffs: First differences for the cards in the hand
    :return: Strength of the strongest card in the straight if found,
    otherwise -1.
    """
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


def check_quads(hand, diffs):
    """
    Consumes a sorted 7 card hand and checks if it contains four of a kind
    :param hand: Sorted list of 7 cards
    :param diffs:
    :return: Strength of four of a kind card if present, otherwise -1.
    """
    counter = 0
    for index in range(1, len(hand)):
        if diffs[index] == 0:
            counter += 1
        else:
            counter = 0
        if counter == 3:
            return hand[index].strength
    return -1


def check_trips(hand, diffs):
    """
    Consumes a sorted 7 card hand and returns every instance of trips
    :param hand: Sorted list of 7 cards
    :param diffs:
    :return: Strength of trips card(s) in descending list, empty
    list if none found
    """
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


def check_pairs(hand, diffs):
    """
    Consumes a sorted 7 card hand and returns each pair strength
    :param hand: Sorted list of 7 cards
    :param diffs:
    :return: A list with the strength of each pair found, empty
    if no pairs
    """
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
    """
    Converts the numbers 10, 11, and 12 to their hex equivalent so
    each card strength will be one character
    :param number: Integer between 0 and 12 to be converted to a string
    :return: String representation of the input number
    """
    if number == 10:
        return "A"
    if number == 11:
        return "B"
    if number == 12:
        return "C"
    return str(number)


def get_straight_flush_strength(strength):
    """
    Straight flush is represented with an 8, followed by the highest
    card in the straight flush
    :param strength: Strength of the strongest card in the straight
    flush
    :return: Hand strength string
    """
    return "8" + convert_to_hex(strength)


def get_flush_strength(hand, suit):
    """
    Flush is represented by 5, followed by the highest 5 cards in
    descending order
    :param hand: List of Cards in the flush
    :param suit: The suit of the flush
    :return: Hand strength string
    """
    result = "5"
    for index in range(len(hand) - 1, -1, -1):
        if hand[index].suit == suit:
            result += convert_to_hex(hand[index].strength)
        if len(result) == 6:
            break
    return result


def get_straight_strength(strength):
    """
    Straight is represented by a 4, followed by the highest card
    in the straight.
    :param strength: Strength of the highest straight card
    :return: Hand strength string
    """
    return "4" + convert_to_hex(strength)


def get_quads_strength(hand, quad_card):
    """
    Four of a kind is represented by a 7, followed by the strength
    of the four of a kind card, then the next highest card.
    :param hand: List of cards
    :param quad_card: Strength of the four of a kind card
    :return: Hand strength string
    """
    result = "7" + convert_to_hex(quad_card)
    for index in range(len(hand) - 1, -1, -1):
        if hand[index].strength != quad_card:
            result += convert_to_hex(hand[index].strength)
        if len(result) == 3:
            break
    return result


def get_trips_strength(hand, trips):
    """
    Three of a kind is represented by a 3, followed by the strength
    of the three of a kind card, then the next two highest cards
    :param hand: List of cards
    :param trips: Strength of the three of a kind card
    :return: Hand strength string
    """
    result = "3" + convert_to_hex(trips[0])
    for index in range(len(hand) - 1, -1, -1):
        if hand[index].strength != trips[0]:
            result += convert_to_hex(hand[index].strength)
        if len(result) == 4:
            break
    return result


def get_two_pair_strength(hand, pairs):
    """
    Two pairs is represented by a 2, followed by the strongest pair,
    the weaker pair, and the strongest remaining card
    :param hand: List of cards
    :param pairs: List of pair strengths
    :return: Hand strength string
    """
    result = "2" + convert_to_hex(pairs[0]) + convert_to_hex(pairs[1])
    for index in range(len(hand) - 1, -1, -1):
        if hand[index].strength != pairs[0] and hand[index].strength != pairs[1]:
            result += convert_to_hex(hand[index].strength)
        if len(result) == 4:
            break
    return result


def get_pair_strength(hand, pairs):
    """
    One pair is represented by a 1, followed by the strength of the
    pair card, then the next three highest remaining cards
    :param hand: List of cards
    :param pairs: Pair strength
    :return: Hand strength string
    """
    result = "1" + convert_to_hex(pairs[0])
    for index in range(len(hand) - 1, -1, -1):
        if hand[index].strength != pairs[0]:
            result += convert_to_hex(hand[index].strength)
        if len(result) == 5:
            break
    return result


def get_high_card_strength(hand):
    """
    High card is represented by a 0, followed by the five strongest
    cards in descending order
    :param hand: List of cards
    :return: Hand strength string
    """
    result = "0"
    for index in range(len(hand) - 1, -1, -1):
        result += convert_to_hex(hand[index].strength)
        if len(result) == 6:
            break
    return result
