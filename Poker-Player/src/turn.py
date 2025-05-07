from .action_line import *
from .hand_evaluation import *
import random
from datetime import datetime

def count_odd(pot, amount):
    return amount / (pot + amount)

def bet(pot, left, right):
    random.seed(datetime.now())
    size = random.randint(left, right)
    return round(pot * size / 100)

def defense(seat, card_rank, equity, pot, odd, valid_actions, vi_action, action_line, behind):
    if seat == 1:
        if vi_action["action"] == "RAISE":
            action_line.vi_status = 'a'
            if card_rank >= 2 and equity >= 0.5:
                action = "call"
                amount = valid_actions[1]["amount"]
            elif card_rank > 0 and equity >= 0.5 and odd <= 0.28:
                action = "call"
                amount = valid_actions[1]["amount"]
            else:
                amount = 0
                if valid_actions[1]["amount"] != 0:
                    action = "fold"
                else:
                    action = "call"
        else:
            action_line.vi_status = 'p'
            if card_rank >= 1 and equity >= 0.6:
                action_line.status = 'a'
                action = "raise"
                amount = max(bet(pot, 100, 100), valid_actions[2]["amount"]["min"])
            else:
                amount = 0
                if valid_actions[1]["amount"] != 0:
                    action = "fold"
                else:
                    action = "call"
    elif seat == 0:
        if not vi_action:
            action = "call"
            amount = 0
        else:
            if card_rank >= 2 and equity >= 0.85:
                action_line.status = 'a'
                action = "raise"
                amount = bet(pot, 150, 150)
            elif card_rank >= 2 and equity >= 0.6 and odd <= 0.34:
                action = "call"
                amount = valid_actions[1]["amount"]
            elif card_rank > 0 and equity >= 0.6 and odd <= 0.28:
                action = "call"
                amount = valid_actions[1]["amount"]
            else:
                amount = 0 
                if valid_actions[1]["amount"] != 0:
                    action = "fold"
                else:
                    action = "call"
    if behind and action == "raise":
        amount = amount * 2
    amount = min(amount, valid_actions[2]["amount"]["max"])
    return (action, amount)

def attack(seat, card_rank, equity, pot, odd, valid_actions, vi_action, action_line, behind):
    if seat == 1:
        if vi_action["action"] == "RAISE":
            action_line.vi_status = 'a'
            if card_rank >= 2 and equity >= 0.65:
                action = "call"
                amount = valid_actions[1]["amount"]
            elif card_rank > 0 and equity >= 0.65 and odd <= 0.28:
                action = "call"
                amount = valid_actions[1]["amount"]
            else:
                amount = 0
                if valid_actions[1]["amount"] != 0:
                    action = "fold"
                else:
                    action = "call"
        else:
            action_line.vi_status = 'p'
            if card_rank > 0 and equity >= 0.6:
                action = "raise"
                amount = max(bet(pot, 100, 100), valid_actions[2]["amount"]["min"])
            else:
                action = "call"
                amount = 0
    elif seat == 0:
        if not vi_action:
            if card_rank >= 1 and equity >= 0.65:
                action = "raise"
                amount = max(bet(pot, 100, 100), valid_actions[2]["amount"]["min"])
            else:
                action = "call"
                amount = 0
        else:
            if card_rank >= 2 and equity >= 0.65:
                action = "call"
                amount = valid_actions[1]["amount"]
            else:
                action = "fold"
                amount = 0
    if behind and action == "raise":
        amount = amount * 2
    amount = min(amount, valid_actions[2]["amount"]["max"])
    return (action, amount)

def turn_strategy(seat, hole_card, card_info, card_rank, valid_actions, round_state, action_line, equity, behind):
    pot = round_state["pot"]["main"]["amount"]
    odd = count_odd(pot, valid_actions[1]["amount"])
    history = round_state["action_histories"]["turn"]
    if len(history) == 0:
        vi_action = []
    else:
        vi_action = history[-1]
    if action_line.my_his["flop"][-1][0] == "CALL":
        action_line.status = 'p'
    else:
        action_line.statis = 'a'
        action_line.vi_status = 'p'
            
    if action_line.status == 'p':
        action, amount = defense(seat, card_rank, equity, pot, odd, valid_actions, vi_action, action_line, behind)
    else:
        action, amount = attack(seat, card_rank, equity, pot, odd, valid_actions, vi_action, action_line, behind)

    action_line.update(seat, round_state, action, amount)
    return (action, amount)
