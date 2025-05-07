from game.players import BasePokerPlayer
from game.engine.card import Card
from game.engine.hand_evaluator import HandEvaluator
from .hand_evaluation import *
from .simulation import *
from .preflop import *
from .flop import *
from .turn import *
from .river import *
from .action_line import *
import random as rand
import json

class Player(BasePokerPlayer):
    def __init__(self):
        self.seat = None # 1: Big blind, 0: Small blind
        self.card = []
        self.card_info = None
        self.board_info = None
        self.action_line = None
        self.odds = None
        self.equity = None
        self.stack = 1000
        self.is_behind = False

    def declare_action(self, valid_actions, hole_card, round_state):
        community_card = []
        if len(round_state["community_card"]) != 0:
            for card in round_state["community_card"]:
                community_card.append(Card.from_str(card))
        self.card_info = HandEvaluator.gen_hand_rank_info(self.card, community_card)
        self.equity = equity(self.card, community_card, 5000)
        result = hand_eval(round_state["community_card"], hole_card, self.card_info)
        rank = combo_rank(result)

        if round_state["street"] == "preflop":
            action, amount = perflop_strategy(self.seat, hole_card, valid_actions, round_state, self.action_line, self.equity)
        elif round_state["street"] == "flop":
            action, amount = flop_strategy(self.seat, hole_card, result, rank, valid_actions, round_state, self.action_line, self.equity, self.is_behind)
        elif round_state["street"] == "turn":
            action, amount = turn_strategy(self.seat, hole_card, result, rank, valid_actions, round_state, self.action_line, self.equity, self.is_behind)
        elif round_state["street"] == "river":
            action, amount = river_strategy(self.seat, hole_card, result, rank, valid_actions, round_state, self.action_line, self.equity, self.is_behind)
        return action, amount

    def receive_game_start_message(self, game_info):
        pass

    def receive_round_start_message(self, round_count, hole_card, seats):
        self.card = []
        self.card.append(Card.from_str(hole_card[0]))
        self.card.append(Card.from_str(hole_card[1]))
        self.action_line = ActionLine()

        if round_count == 1:
            if seats[0]["name"] == "b09902060":
                self.seat = 1
            else:
                self.seat = 0
        else:
            self.seat ^= 1

        if seats[0]["name"] == "b09902060":
            self.stack = seats[0]["stack"]
        else:
            self.stack = seats[1]["stack"]
        
        if round_count > 10 and self.stack < 1000:
            self.is_behind = True
        else:
            self.is_behind = False

    def receive_street_start_message(self, street, round_state):
        pass

    def receive_game_update_message(self, new_action, round_state):
        pass

    def receive_round_result_message(self, winners, hand_info, round_state):
        pass


def setup_ai():
    return Player()
