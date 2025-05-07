from .chart import * # BB_limp, BB_raise, SB_15, SB_10
from .action_line import *

def fold2win(round_count, seat, stack):
    round_left = 20 - round_count
    if seat == 1:
        big_num = round_left // 2
        small_num = round_left - big_num
    else:
        small_num = round_left // 2
        big_num = round_left - small_num
    
    blinds = 10 * big_num + 5 * small_num
    if stack - blinds >= 1000:
        return True
    else:
        return False

def perflop_strategy(seat, hole_card, valid_actions, round_state, action_line, equity):
    players = round_state["seats"]
    if players[0]["name"] == "b09902060":
        stack = players[0]["stack"]
    else:
        stack = players[1]["stack"]
        
    if fold2win(round_state["round_count"], seat, stack):
        return ("fold", 0)
    
    history_len = len(round_state["action_histories"]["preflop"])
    last_action = round_state["action_histories"]["preflop"][-1]
    allin_amount = valid_actions[2]["amount"]["max"]
    call_amount = valid_actions[1]["amount"]
    if seat == 1:
        if last_action["action"] == "RAISE" and history_len == 3:
            # at BB facing raise
            label = BB_raise.check(hole_card)
            # 0: all in
            # 1: call vs 2x raise
            # 2: call vs < 2.5x raise
            # 3: fold
            # 4: raise 15bb
            # 5: raise 15bb vs < 5bb raise, call
            if label == 0:
                if equity >= 0.8:
                    return ("raise", amount)
                else:
                    action_line.update(seat, round_state, "call", call_amount)
                    return ("call", call_amount)
            elif label == 1:
                if equity >= 0.5 and last_action["amount"] <= 50:
                    action_line.update(seat, round_state, "call", call_amount)
                    return ("call", call_amount)
                elif equity >= 0.4 and last_action["amount"] <= 20:
                    action_line.update(seat, round_state, "call", call_amount)
                    return ("call", call_amount)
                else:
                    return ("fold", call_amount)
            elif label == 2:
                if hole_card[0][1] == 'A' and hole_card[1][1] == 'A':
                    action_line.update(seat, round_state, "call", call_amount)
                    return ("call", call_amount)
                elif equity < 0.6 and last_action["amount"] > 80:
                    return ("fold", 0)
                else:
                    action_line.update(seat, round_state, "call", call_amount)
                    return ("call", call_amount)
            elif label == 3:
                return ("fold", 0)
            elif label == 4:
                action_line.update(seat, round_state, "raise", 150)
                return ("raise", 150)
            else:
                if call_amount > 50:
                    action_line.update(seat, round_state, "call", call_amount)
                    return ("call", call_amount)
                else:
                    return ("raise", 150)
        elif last_action["action"] == "CALL" and history_len == 3:
            # at BB facing limp
            label = BB_limp.check(hole_card)
            # 0: all in (raise 15bb)
            # 1: call
            # 2: raise 2.5x / go broke
            # 3: raise 2.5x / fold
            if label == 0:
                action_line.update(seat, round_state, "raise", 150)
                return ("raise", 150)
            elif label == 1:
                action_line.update(seat, round_state, "call", call_amount)
                return ("call", call_amount)
            elif label == 2 or label == 3:
                action_line.update(seat, round_state, "raise", 30)
                return ("raise", 30)
        else:
            target_action = round_state["action_histories"]["preflop"][-3]["action"]
            # at BB facing reraise
            if target_action == "CALL":
                label == BB_limp.check(hole_card)
                if label == 2:
                    action_line.update(seat, round_state, "raise", allin_amount)
                    return ("raise", allin_amount)
                else:
                    return ("fold", 0)
            elif target_action == "RAISE":
                return ("fold", 0)

    if seat == 0:
        if history_len == 2:
            label = SB_15.check(hole_card)
            # 0: limp / call all in
            # 1: limp / call vs < 3.5x
            # 2: raise 2x / call vs < 3x
            # 3: all in (raise 15bb)
            # 4: raise 2x / go broke
            # 5: raise 2x / fold
            # 6: limp / fold
            # 7: fold
            if label == 0 or label == 1 or label == 6:
                action_line.update(seat, round_state, "call", call_amount)
                return ("call", call_amount)
            elif label == 2 or label == 4 or label == 5:
                action_line.update(seat, round_state, "raise", 20)
                return ("raise", 20)
            elif label == 3:
                action_line.update(seat, round_state, "raise", 150)
                return ("raise", 150)
            else:
                return ("fold", 0)
        elif history_len == 4:
            # at SB facing reraise
            label = SB_15.check(hole_card)
            if label == 0:
                action_line.update(seat, round_state, "call", call_amount)
                return ("call", call_amount)
            elif label == 1:
                if equity < 0.6 and last_action["amount"] > 50:
                    return ("fold", 0)
                else:
                    action_line.update(seat, round_state, "call", call_amount)
                    return ("call", call_amount)
            elif label == 2:
                if equity < 0.6 and last_action["amount"] > 80:
                    return ("fold", 0)
                else:
                    action_line.update(seat, round_state, "call", call_amount)
                    return ("call", call_amount)
            elif label == 3:
                return ("fold", 0)
            elif label == 4:
                action_line.update(seat, round_state, "raise", allin_amount)
                return ("raise", allin_amount)
            elif label == 5 or label == 6:
                return ("fold", 0)

