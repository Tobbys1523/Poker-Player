class ActionLine:
    def __init__(self):
        self.status = None
        self.vi_status = None
        self.pot_type = None
        self.my_his = {"preflop": [], "flop": [], "turn": [], "river": []}
        self.vi_his = {"preflop": [], "flop": [], "turn": [], "river": []}
        self.odds = None
        self.equity = None
        self.street_connect = 0
        self.street_heavy = 0

    def his2info(self, history, pot, index):
        if index == 0:
            if history[index]["action"] == "RAISE":
                return ["raise", history[index]["amount"] / 10]
            else:
                return ["call", 0]
        else:
            if history[index]["action"] == "RAISE":
                if history[index-1]["amount"] != 0:
                    return ["raise", history[index]["amount"] / history[index-1]["amount"]]
                else:
                    return ["raise", history[index]["amount"] / pot]
            else:
                return ["call", history[index]["amount"]]

    def update(self, seat, round_state, action, amount):
        if action == "call":
            self.status = 'p'
        elif action == "raise":
            self.status = 'a'
        else:
            return

        if round_state["street"] == "preflop":
            history = round_state["action_histories"]["preflop"]
            history.append({"action": action.upper(), "amount": amount})
            pot = round_state["pot"]["main"]["amount"]
            if history[-1]["action"] == "CALL" and history[-2]["action"] == "CALL":
                self.pot_type = "limp"
            elif len(history) == 4:
                self.pot_type = "raise"
            elif len(history) > 4:
                self.pot_type = "3bet"
            if len(self.my_his["preflop"]) == 0:
                if seat == 1:
                    self.vi_his["preflop"].append(self.his2info(history, pot, 2))
                    self.my_his["preflop"].append(self.his2info(history, pot, 3))
                else:
                    self.my_his["preflop"].append(self.his2info(history, pot, 2))
            else:
                self.vi_his["preflop"].append(self.his2info(history, pot, -2))
                self.my_his["preflop"].append(self.his2info(history, pot, -1))
        elif round_state["street"] == "flop":
            history = round_state["action_histories"]["flop"]
            history.append({"action": action.upper(), "amount": amount})
            pot = round_state["pot"]["main"]["amount"]
            if len(self.my_his["flop"]) == 0:
                if seat == 1:
                    self.vi_his["flop"].append(self.his2info(history, pot, 0))
                    self.my_his["flop"].append(self.his2info(history, pot, 1))
                else:
                    self.my_his["flop"].append(self.his2info(history, pot, 0))
            else:
                self.vi_his["flop"].append(self.his2info(history, pot, -2))
                self.my_his["flop"].append(self.his2info(history, pot, -1))
        elif round_state["street"] == "turn":
            history = round_state["action_histories"]["turn"]
            history.append({"action": action.upper(), "amount": amount})
            pot = round_state["pot"]["main"]["amount"]
            if len(self.my_his["turn"]) == 0:
                if seat == 1:
                    self.vi_his["turn"].append(self.his2info(history, pot, 0))
                    self.my_his["turn"].append(self.his2info(history, pot, 1))
                else:
                    self.my_his["turn"].append(self.his2info(history, pot, 0))
            else:
                self.vi_his["turn"].append(self.his2info(history, pot, -2))
                self.my_his["turn"].append(self.his2info(history, pot, -1))
        elif round_state["street"] == "river":
            history = round_state["action_histories"]["river"]
            history.append({"action": action.upper(), "amount": amount})
            pot = round_state["pot"]["main"]["amount"]
            if len(self.my_his["river"]) == 0:
                if seat == 1:
                    self.vi_his["river"].append(self.his2info(history, pot, 0))
                    self.my_his["river"].append(self.his2info(history, pot, 1))
                else:
                    self.my_his["river"].append(self.his2info(history, pot, 0))
            else:
                self.vi_his["river"].append(self.his2info(history, pot, -2))
                self.my_his["river"].append(self.his2info(history, pot, -1))


