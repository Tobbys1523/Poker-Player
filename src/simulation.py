from multiprocessing import Process, Pool
import random as rand
from datetime import datetime
from game.engine.card import Card
from game.engine.hand_evaluator import HandEvaluator

def montecarlo(hole_card, community_card):
    community_card = fill_community(community_card, community_card + hole_card)
    vi_hole = pick_unused(2, community_card + hole_card)
    my_score = HandEvaluator.eval_hand(hole_card, community_card)
    vi_score = HandEvaluator.eval_hand(vi_hole, community_card)
    return 1 if my_score >= vi_score else 0

def equity(hole_card, community_card, epoch):
    win = [0] * epoch
    with Pool(processes=8) as pool:
        for i in range(epoch):
            win[i] = montecarlo(hole_card, community_card)
    return sum(win) / epoch

def fill_community(community_card, used_card):
    card_num = 5 - len(community_card)
    return community_card + pick_unused(card_num, used_card)

def pick_unused(num, used_card):
    used = []
    unused = []
    picked = []
    for c in used_card:
        used.append(Card.to_id(c))
    for id in range(1, 53):
        if id not in used:
            unused.append(id)
    choice = rand.sample(unused, num)
    return [Card.from_id(c) for c in choice]
