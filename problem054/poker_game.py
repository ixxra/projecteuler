
def is_royal_flush(hand):
    if len(set([s for v,s in hand])) > 1:
        return False
    return set([v for v, s in hand]) == set(['T', 'J', 'Q', 'K', 'A'])


def is_straight_flush(hand):
    if len(set([s for v,s in hand])) > 1:
        return False
    Suit = ['2', '3', '4', '5', '6', '7', '8', '9', 
            'T', 'J', 'Q', 'K', 'A'
        ]
    values = sorted([v for v, s in hand])
    print values[0]
    i = Suit.index(values[0])
    
    return i < 9 and Suit[i + 1] == values[1] and \
            Suit[i + 2] == values[2] and \
            Suit[i + 3] == values[3] and \
            Suit[i + 4] == values[4]


def is_four_of_a_kind(hand):
    values = [v for v, s in hand]

    for v in values:
        if values.count(v) == 4:
            return True

    return False


def is_full_house(hand):
    def test_pair((x, y)):
        return x == y

    values = [v for v, s in hand]

    for v in values:
        if values.count(v) == 3:
            if test_pair([w for w in values if w != v]):
                return True

    return False


def is_flush(hand):
    return len(set([s for v, s in hand])) == 1


def is_straight(hand):
    Suit = ['2', '3', '4', '5', '6', '7', '8', '9', 
            'T', 'J', 'Q', 'K', 'A'
        ]
    values = sorted([v for v, s in hand])
    i = Suit.index(values[0])
    
    return i < 9 and Suit[i + 1] == values[1] and \
            Suit[i + 2] == values[2] and \
            Suit[i + 3] == values[3] and \
            Suit[i + 4] == values[4]



def is_three_of_a_kind(hand):
    values = [v for v, s in hand]

    for v in values:
        if values.count(v) == 3:
            return True

    return False


def is_two_pairs(hand):
    values = [v for v, s in hand]
    diff_values = set(values)

    if len(diff_values) == 3:
        pairs = 0
        for v in diff_values:
            if values.count(v) == 2:
                pairs += 1
        
        return pairs == 2

    return False


def is_one_pair(hand):
    pass
#    values = [v for v, s in hand]
#    diff_values = set(values)
#
#    if len(diff_values) == 3:
#        pairs = 0
#        for v in diff_values:
#            if values.count(v) == 2:
#                pairs += 1
#        
#        return pairs == 2
#
#    return False
#
#
