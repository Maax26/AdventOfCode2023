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


def _insertion_sort(category, hand, bid):
    items = list(category)
    for key, value in category.items():
        for i in range(5):
            if _RANKS[hand[i]] > _RANKS[key[i]]:
                temp = (key, value)
                items.insert(key.index(), (hand, bid))
                items.insert(key.index()+1, temp)
    if not category.items():
        items.insert(0, (hand, bid))

    category = dict(items)




def main():
    inputs = open("test_input.txt")

    ordered_hands = {
        _FIVE_OF_A_KIND: {},
        _FOUR_OF_A_KIND: {},
        _FULL_HOUSE: {},
        _THREE_OF_A_KIND: {},
        _TWO_PAIR: {},
        _ONE_PAIR: {},
        _HIGH_CARD: {},
    }

    for line in inputs:
        hand, bid = line.strip().split()
        ordered_hands[_identify_hand(hand)][hand] = bid
        # _insertion_sort(ordered_hands[_identify_hand(hand)], hand, bid)

    import json
    print(json.dumps(ordered_hands, indent=4))


if __name__ == "__main__":
    main()
