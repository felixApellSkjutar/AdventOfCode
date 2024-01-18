

with open('inp', 'r') as file:
    ls = file.read().strip()

    hands = [(x, int(y)) for x,y in [line.split() for line in ls.split('\n')]]
    


task2 = True


def classify(cards: str) -> int:
    counts = [cards.count(card) for card in cards]
    
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        if 2 in counts:
            return 4
        return 3
    if counts.count(2) == 4:
        return 2
    if 2 in counts:
        return 1
    return 0


letter_map = {"T": "A", "J": "B" if not task2 else ".", "Q": "C", "K": "D", "A": "E"}

def replacements(hand):
    if hand == "":
        return [""]

    return [
        x + y
        for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
        for y in replacements(hand[1:])
    ]


def classify2(hand):
    return max(map(classify, replacements(hand)))


def strength(hand):
    if task2:
        return (classify2(hand), [letter_map.get(card, card) for card in hand])    
    return (classify(hand), [letter_map.get(card, card) for card in hand])


hands.sort(key=lambda play: strength(play[0]))

total = 0
for rank, (hand, bid) in enumerate(hands, 1):
    total += rank*bid

print(total)