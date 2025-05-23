class Range:
    def __init__(self):
        self.chart = [[None]*13 for i in range(13)]
        self.label = {}

    def check(self, hole_card):
        def get_index(card):
            mapping = {"A": 0, "K": 1, "Q": 2, "J": 3, "T": 4, "9": 5, "8": 6, "7": 7, "6": 8, "5": 9, "4": 10, "3": 11, "2": 12,}
            return mapping[card[1]]
        
        index_l = max(get_index(hole_card[0]), get_index(hole_card[1]))
        index_s = min(get_index(hole_card[0]), get_index(hole_card[1]))
        if hole_card[0][0] == hole_card[1][0]:
            label = self.chart[index_s][index_l]
        else:
            label = self.chart[index_l][index_s]

        return label
        
# at BB facing limp
BB_limp = Range()
BB_limp.label = {0: "a(r15)", 1: "c", 2: "r2.5/b", 3: "r2.5/f"}
"""
# Original
BB_limp.chart = [
        [2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0],
        [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 0, 1, 2, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 3, 1, 1, 1, 2, 0, 0, 0, 1, 1, 1, 1],
        [0, 3, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
        [0, 3, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
        [0, 3, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],]
"""
BB_limp.chart = [
        [2, 2, 2, 2, 2, 2, 2, 2, 0, 1, 1, 1, 1],
        [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 0, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 2, 0, 1, 2, 0, 0, 1, 1, 1, 1, 1, 1],
        [0, 3, 1, 1, 1, 2, 0, 0, 1, 1, 1, 1, 1],
        [0, 3, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
        [0, 3, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
        [0, 3, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],]
        
# in BB facing raise
BB_raise = Range()
BB_raise.label = {0: "a", 1: "c2", 2: "c", 3: "f", 4: "r15", 5:"r15<50"}
"""
# Original
BB_raise.chart = [
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0],
        [0, 0, 2, 0, 2, 2, 2, 2, 2, 2, 0, 2, 2],
        [0, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2],
        [0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2],
        [0, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2, 2],
        [0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 2, 2, 2],
        [0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 2, 2, 2],
        [0, 2, 2, 2, 3, 1, 2, 2, 2, 0, 2, 2, 2],
        [0, 2, 2, 2, 3, 3, 3, 3, 2, 2, 0, 1, 1],
        [0, 2, 2, 1, 3, 3, 3, 3, 3, 1, 2, 0, 1],
        [0, 2, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 0],]
"""
BB_raise.chart = [
        [2, 0, 0, 0, 4, 4, 4, 5, 5, 5, 2, 2, 2],
        [0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [4, 5, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        [5, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2],
        [5, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2],
        [5, 2, 2, 2, 2, 2, 4, 5, 2, 2, 2, 2, 2],
        [5, 2, 2, 2, 2, 2, 2, 4, 5, 2, 2, 2, 2],
        [2, 2, 2, 2, 2, 2, 2, 2, 4, 5, 2, 2, 2],
        [2, 2, 2, 2, 3, 1, 2, 2, 2, 5, 2, 2, 2],
        [2, 2, 2, 2, 3, 3, 3, 3, 2, 2, 5, 1, 1],
        [2, 2, 2, 1, 3, 3, 3, 3, 3, 1, 2, 5, 1],
        [2, 2, 2, 1, 3, 3, 3, 3, 3, 3, 3, 3, 5],]

# in SB with 10~15 bb
SB_15 = Range()
SB_15.label = {0: "l/c", 1: "l/c3.5", 2: "r2/c3", 3: "a(r15)", 4: "r2/c", 5: "r2/f", 6: "l/f", 7: "f"}
"""
# Original
SB_15.chart = [
        [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3],
        [4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3],
        [4, 4, 4, 4, 4, 0, 0, 0, 3, 3, 3, 3, 3],
        [4, 4, 0, 0, 4, 4, 0, 3, 3, 3, 3, 3, 3],
        [4, 4, 3, 3, 3, 4, 3, 3, 3, 3, 1, 1, 1],
        [4, 3, 1, 1, 1, 1, 4, 3, 3, 3, 1, 1, 1],
        [2, 3, 1, 1, 1, 1, 1, 4, 3, 3, 3, 1, 1],
        [3, 3, 6, 6, 6, 6, 6, 1, 3, 3, 3, 1, 1],
        [3, 1, 6, 6, 6, 6, 6, 6, 1, 3, 3, 1, 1],
        [3, 1, 6, 6, 5, 6, 5, 5, 6, 1, 3, 1, 1],
        [3, 1, 6, 5, 6, 7, 7, 6, 5, 5, 6, 3, 1],
        [3, 1, 6, 5, 6, 7, 7, 7, 7, 7, 7, 7, 1],]
"""
SB_15.chart = [
        [4, 4, 4, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2],
        [4, 4, 0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1],
        [4, 4, 4, 0, 0, 0, 2, 2, 2, 2, 1, 1, 1],
        [4, 4, 4, 4, 4, 2, 2, 2, 1, 1, 1, 1, 1],
        [4, 4, 2, 2, 4, 4, 2, 1, 1, 1, 1, 1, 1],
        [4, 4, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
        [4, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1],
        [2, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1],
        [2, 1, 6, 6, 6, 6, 6, 1, 2, 1, 1, 1, 1],
        [1, 1, 6, 6, 6, 6, 6, 6, 1, 2, 1, 1, 1],
        [1, 1, 6, 6, 5, 6, 5, 5, 6, 1, 2, 1, 1],
        [1, 1, 6, 5, 6, 7, 7, 6, 5, 5, 6, 2, 1],
        [1, 1, 6, 5, 6, 7, 7, 7, 7, 7, 7, 7, 1],]

# in SB with <10 bb
SB_10 = Range()
SB_10.label = {0: "l/c", 1: "a", 2: "l/f"}
SB_10.chart = [
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2],
        [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 2, 2, 2],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
        [1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 2, 2],
        [1, 1, 2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2],
        [1, 1, 2, 2, 2, 2, 2, 2, 1, 1, 1, 2, 2],
        [1, 1, 2, 3, 3, 3, 2, 2, 2, 1, 1, 1, 2],
        [1, 1, 2, 3, 3, 3, 3, 3, 2, 2, 1, 1, 3],
        [1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3],
        [1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1],]
