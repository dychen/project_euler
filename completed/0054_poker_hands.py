def convert_values(values):
    new = []
    for value in values:
        if value == 'T':
            new.append(10)
        elif value == 'J':
            new.append(11)
        elif value == 'Q':
            new.append(12)
        elif value == 'K':
            new.append(13)
        elif value == 'A':
            new.append(14)
        else:
            new.append(int(value))
    return new

def hash_values(values):
    h = {}
    for value in values:
        if value in h:
            h[value] += 1
        else:
            h[value] = 1
    return h

def most_common_values(values):
    h_values = hash_values(values)
    maximum = max(h_values.values())
    arr = []
    for value in h_values.keys():
        if h_values[value] == maximum:
            arr.append(value)
    arr.sort()
    arr.reverse()
    return arr

def is_pair(hand):
    values = map(lambda x: x[0], hand)
    return len(set(values)) == 4

def is_two_pair(hand):
    values = map(lambda x: x[0], hand)
    return len(set(values)) == 3 and 2 in hash_values(values).values()

def is_three_of_a_kind(hand):
    values = map(lambda x: x[0], hand)
    return len(set(values)) == 3 and 3 in hash_values(values).values()

def is_straight(hand):
    values = map(lambda x: x[0], hand)
    new = convert_values(values)
    new.sort()
    for i in range(len(new)-1):
        if new[i+1] - new[i] != 1:
            return False
    return True

def is_flush(hand):
    suits = map(lambda x: x[1], hand)
    return len(set(suits)) == 1

def is_full_house(hand):
    values = map(lambda x: x[0], hand)
    return len(set(values)) == 2 and 2 in hash_values(values).values()

def is_four_of_a_kind(hand):
    values = map(lambda x: x[0], hand)
    return len(set(values)) == 2 and 3 in hash_values(values).values()

def is_straight_flush(hand):
    values = map(lambda x: x[0], hand)
    suits = map(lambda x: x[1], hand)
    return is_straight(hand) and is_flush(hand)

def is_royal_flush(hand):
    values = map(lambda x: x[0], hand)
    suits = map(lambda x: x[1], hand)
    return is_straight_flush(hand) and 'T' in values and 'J' in values and 'Q' in values and 'K' in values and 'A' in values

def tiebreak(h1, h2):
    new_h1 = map(lambda x: x[0], h1)
    new_h2 = map(lambda x: x[0], h2)
    return tiebreak_iter(new_h1, new_h2)

def tiebreak_iter(h1, h2):
    new_h1 = convert_values(h1)
    new_h2 = convert_values(h2)
    common_1 = most_common_values(new_h1)
    common_2 = most_common_values(new_h2)
    if common_1 > common_2:
        return True
    elif common_2 > common_1:
        return False
    else:
        for e in common_1:
            while e in new_h1:
                new_h1.remove(e)
        for e in common_2:
            while e in new_h2:
                new_h2.remove(e)
        return tiebreak_iter(new_h1, new_h2)

def winner(h1, h2):
    w1 = is_royal_flush(h1)
    w2 = is_royal_flush(h2)
    if w1 and w2:
        print 'Royal Flush Tiebreak'
        return tiebreak(h1, h2)
    elif w1:
        print 'Royal Flush p1'
        return True
    elif w2:
        print 'Royal Flush p2'
        return False
    else:
        w1 = is_straight_flush(h1)
        w2 = is_straight_flush(h2)
        if w1 and w2:
            print 'Straight Flush Tiebreak'
            return tiebreak(h1, h2)
        elif w1:
            print 'Straight Flush p1'
            return True
        elif w2:
            print 'Straight Flush p2'
            return False
        else:
            w1 = is_four_of_a_kind(h1)
            w2 = is_four_of_a_kind(h2)
            if w1 and w2:
                print 'Four of a Kind Tiebreak'
                return tiebreak(h1, h2)
            elif w1:
                print 'Four of a Kind p1'
                return True
            elif w2:
                print 'Four of a Kind p2'
                return False
            else:
                w1 = is_full_house(h1)
                w2 = is_full_house(h2)
                if w1 and w2:
                    print 'Full House Tiebreak'
                    return tiebreak(h1, h2)
                elif w1:
                    print 'Full House p1'
                    return True
                elif w2:
                    print 'Full House p2'
                    return False
                else:
                    w1 = is_flush(h1)
                    w2 = is_flush(h2)
                    if w1 and w2:
                        print 'Flush Tiebreak'
                        return tiebreak(h1, h2)
                    elif w1:
                        print 'Flush p1'
                        return True
                    elif w2:
                        print 'Flush p2'
                        return False
                    else:
                        w1 = is_straight(h1)
                        w2 = is_straight(h2)
                        if w1 and w2:
                            print 'Straight Tiebreak'
                            return tiebreak(h1, h2)
                        elif w1:
                            print 'Straight p1'
                            return True
                        elif w2:
                            print 'Straight p2'
                            return False
                        else:
                            w1 = is_three_of_a_kind(h1)
                            w2 = is_three_of_a_kind(h2)
                            if w1 and w2:
                                print 'Three of a Kind Tiebreak'
                                return tiebreak(h1, h2)
                            elif w1:
                                print 'Three of a Kind p1'
                                return True
                            elif w2:
                                print 'Three of a Kind p2'
                                return False
                            else:
                                w1 = is_two_pair(h1)
                                w2 = is_two_pair(h2)
                                if w1 and w2:
                                    print 'Two Pair Tiebreak'
                                    return tiebreak(h1, h2)
                                elif w1:
                                    print 'Two Pair p1'
                                    return True
                                elif w2:
                                    print 'Two Pair p2'
                                    return False
                                else:
                                    w1 = is_pair(h1)
                                    w2 = is_pair(h2)
                                    if w1 and w2:
                                        print 'Pair Tiebreak'
                                        return tiebreak(h1, h2)
                                    elif w1:
                                        print 'Pair p1'
                                        return True
                                    elif w2:
                                        print 'Pair p2'
                                        return False
                                    else:
                                        print 'High Card Tiebreak'
                                        return tiebreak(h1, h2)


file = open('tmp.txt', 'r')
count = 0
for line in file:
    p1 = line.strip().split()[:5]
    p2 = line.strip().split()[5:]
    print str(p1) + ' ::: ' + str(p2)
    win = winner(p1, p2)
    print win
    if win:
        count += 1
print count
file.close()