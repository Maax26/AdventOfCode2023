from collections import Counter, defaultdict

_RANKS = {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "J": 10,
    "Q": 11,
    "K": 12,
    "A": 13,
}

_FIVE_OF_A_KIND = "five_of_a_kind"
_FOUR_OF_A_KIND = "four_of_a_kind"
_FULL_HOUSE = "full_house"
_THREE_OF_A_KIND = "three_of_a_kind"
_TWO_PAIR = "two_pair"
_ONE_PAIR = "one_pair"
_HIGH_CARD = "high_card"


def _five_of_a_kind(hand):
    card_counter = Counter([card for card in hand])
    for card in hand:
        if card_counter[card] == 5:
            return True
    return False


def _four_of_a_kind(hand):
    card_counter = Counter([card for card in hand])
    for card in hand:
        if card_counter[card] == 4:
            return True
    return False


def _full_house(hand):
    card_counter = Counter([card for card in hand])
    if sorted(card_counter.values()) == [2, 3]:
        return True
    return False


def _three_of_a_kind(hand):
    card_counter = Counter([card for card in hand])
    for card in hand:
        if card_counter[card] == 3:
            return True
    return False


def _pair(hand):
    one_pair = False
    two_pair = False
    card_counter = Counter([card for card in hand])
    for counter in card_counter.values():
        if counter == 2:
            if not one_pair:
                one_pair = True
            else:
                two_pair = True
    return one_pair, two_pair


def _two_pair(hand):
    return _pair(hand)[1]


def _one_pair(hand):
    return _pair(hand)[0]


def _identify_hand(hand):
    if _five_of_a_kind(hand):
        return _FIVE_OF_A_KIND

    if _four_of_a_kind(hand):
        return _FOUR_OF_A_KIND

    if _full_house(hand):
        return _FULL_HOUSE

    if _three_of_a_kind(hand):
        return _THREE_OF_A_KIND

    if _two_pair(hand):
        return _TWO_PAIR

    if _one_pair(hand):
        return _ONE_PAIR

    return _HIGH_CARD


def _insert_hand_is_greater(current_hand, insert_hand):
    for i in range(len(current_hand)):
        if _RANKS[insert_hand[i]] == _RANKS[current_hand[i]]:
            continue
        return _RANKS[insert_hand[i]] > _RANKS[current_hand[i]]


def _sorted_insert(category, hand, bid):
    n = len(category)

    if n == 0:
        category.append((hand, bid))
        return category
    if n == 1:
        if _insert_hand_is_greater(category[0][0], hand):
            category.append((hand, bid))
        else:
            temp_val = category.pop()
            category.append((hand, bid))
            category.append(temp_val)
        return category

    i = 0
    while i < n and _insert_hand_is_greater(
        category[i][0], hand
    ):  # value >= sorted_list[i]:
        i += 1

    if i >= n:
        category.append((hand, bid))
        return category
    else:
        new_list = category[:i]
        list_end = category[i:]
        new_list.append((hand, bid))
        for value in list_end:
            new_list.append(value)
        return new_list


def main():
    # inputs = open("test_input.txt")
    inputs = open("input.txt")

    ordered_hands = {
        _HIGH_CARD: [],
        _ONE_PAIR: [],
        _TWO_PAIR: [],
        _THREE_OF_A_KIND: [],
        _FULL_HOUSE: [],
        _FOUR_OF_A_KIND: [],
        _FIVE_OF_A_KIND: [],
    }

    for line in inputs:
        hand, bid = line.strip().split()
        hand_category = _identify_hand(hand)
        ordered_hands[hand_category] = _sorted_insert(
            ordered_hands[hand_category], hand, bid
        )

    current_rank = 1
    total_winnings = 0
    for category, hands in ordered_hands.items():
        for _, bid in hands:
            winnings = int(bid) * current_rank
            total_winnings += winnings
            current_rank += 1

    print(total_winnings)


if __name__ == "__main__":
    main()
