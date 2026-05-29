from functools import wraps
from collections import Counter

def call_counter(fun):
    count = 0

    @wraps(fun)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"[DEBUG] Function '{fun.__name__}' has been called {count} time(s).")
        return fun(*args, **kwargs)
    wrapper.get_call_count = lambda: count
    return wrapper

def rank_hand(hand):
    counts = Counter(hand)
    values = sorted(counts.values(), reverse=True)
    if values == [5]: return 6
    if values == [4, 1]: return 5
    if values == [3, 2]: return 4
    if values == [3, 1, 1]: return 3
    if values == [2, 2, 1]: return 2
    if values == [2, 1, 1, 1]: return 1
    return 0

# @call_counter
def rank_hand_part_2(hand):
    if 'J' not in hand:
        return rank_hand(hand)
    # J is in the hand
    not_J_cards = tuple(str(i) for i in range(2, 10)) + ('T', 'Q', 'K', 'A')
    potential_hands = [''.join(card if card != 'J' else not_J_cards[i] for card in hand)
                       for i in range(len(not_J_cards))]
    # print(f"{potential_hands = }")
    best_hands = [h for h in potential_hands 
                  if rank_hand(h) == max(rank_hand(potential_hand)
                                         for potential_hand in potential_hands)]
    if len(best_hands) == 1:
        # print(f"{best_hands = }")
        return rank_hand(best_hands[0])
    
    best_hands.sort(key=lambda h: (rank_hand(h), [card_ranks(c) for c in h]))
    return rank_hand(best_hands[-1])

def card_ranks(card):
    order = dict(zip([str(i) for i in range(2, 10)] + ['T', 'J', 'Q', 'K', 'A'], [i for i in range(2, 15)]))
    return order[card]

def card_ranks_part_2(card):
    lst = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']
    order = dict(zip(lst, [i for i in range(2, 15)]))
    return order[card]

file = r"C:\Users\lyndo\Documents\Coding and Programming Folder\2023 Day 7 Advent of Code Input.txt"

hands = []
with open(file) as f:
    for line in f:
        hand, bid = line.strip().split()
        hands.append((hand, int(bid)))

hands.sort(key=lambda h: (rank_hand(h[0]), [card_ranks(c) for c in h[0]]))

winnings = sum(i * h[1] for i, h in enumerate(hands, 1))
print(f"{winnings = :,}")

# Part 2
# try:
hands.sort(key=lambda h: (rank_hand_part_2(h[0]), [card_ranks_part_2(c) for c in h[0]]))
# except TypeError:
#     # print(f"{hands = }")
#     pass
winnings = sum(i * h[1] for i, h in enumerate(hands, 1))
print(f"{winnings = :,}")