from collections import Counter


_RANKS = {
    "J": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
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
    card_counter = dict(Counter(list(hand)))
    for card, counter in card_counter.items():
        if card == "J":
            if counter == 5:
                return True
        else:
            if counter + card_counter.get("J", 0) == 5:
                return True
    return False


def _four_of_a_kind(hand):
    card_counter = dict(Counter(list(hand)))
    for card, counter in card_counter.items():
        if card == "J":
            if counter == 4:
                return True
        else:
            if counter + card_counter.get("J", 0) == 4:
                return True
    return False


def _full_house(hand):
    card_counter = dict(Counter(list(hand)))
    if sorted(card_counter.values()) == [2, 3]:
        return True
    if card_counter.get("J", 0):
        del card_counter["J"]
        if list(card_counter.values()) == [2, 2]:
            return True
    return False


def _three_of_a_kind(hand):
    card_counter = dict(Counter(list(hand)))
    for card, counter in card_counter.items():
        if card == "J":
            if counter == 3:
                return True
        else:
            if counter + card_counter.get("J", 0) == 3:
                return True
    return False


def _pair(hand):
    one_pair = False
    two_pair = False
    card_counter = dict(Counter(list(hand)))
    if card_counter.get("J"):
        return True, False
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
    hand_category = _HIGH_CARD
    if _five_of_a_kind(hand):
        hand_category = _FIVE_OF_A_KIND
    elif _four_of_a_kind(hand):
        hand_category = _FOUR_OF_A_KIND
    elif _full_house(hand):
        hand_category = _FULL_HOUSE
    elif _three_of_a_kind(hand):
        hand_category = _THREE_OF_A_KIND
    elif _two_pair(hand):
        hand_category = _TWO_PAIR
    elif _one_pair(hand):
        hand_category = _ONE_PAIR

    return hand_category


def _insert_hand_is_greater(current_hand, insert_hand):
    for i, current_card in enumerate(current_hand):
        if _RANKS[insert_hand[i]] == _RANKS[current_card]:
            continue
        return _RANKS[insert_hand[i]] > _RANKS[current_card]


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
    while i < n and _insert_hand_is_greater(category[i][0], hand):
        i += 1

    if i >= n:
        category.append((hand, bid))
        return category

    new_list = category[:i]
    list_end = category[i:]
    new_list.append((hand, bid))
    for value in list_end:
        new_list.append(value)
    return new_list


def main():
    # inputs = open("test_input.txt", encoding="utf-8")
    inputs = open("input.txt", encoding="utf-8")

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
        if "J" in hand:
            pass
        ordered_hands[hand_category] = _sorted_insert(
            ordered_hands[hand_category], hand, bid
        )

    current_rank = 1
    total_winnings = 0
    for hands in ordered_hands.values():
        for _, bid in hands:
            total_winnings += int(bid) * current_rank
            current_rank += 1

    print(total_winnings)


if __name__ == "__main__":
    main()
