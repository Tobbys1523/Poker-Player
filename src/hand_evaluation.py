def card2int(card):
    mapping = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2,}
    return mapping[card[1]]

def is_Hits(com_num, hand_num):
    #print("In Hits")
    num_dict = {14: 0, 13: 0, 12: 0, 11: 0, 10: 0, 9: 0, 8: 0, 7: 0, 6: 0, 5: 0, 4: 0, 3: 0, 2: 0}
    card_list = com_num + hand_num
    pair = 0
    trip = 0
    quad = 0
    for num in card_list:
        num_dict[num] += 1
    for i in range(2, 15):
        if num_dict[i] == 2:
            pair += 1
        elif num_dict[i] == 3:
            trip += 1
        elif num_dict[i] == 4:
            quad += 1
    if quad > 0:
        return "quad"
    elif trip > 0 and pair > 0:
        return "full"
    elif trip > 0:
        return "trip"
    elif pair > 1:
        return "2pair"
    elif pair > 0:
        if hand_num[-1] >= com_num[-1] and num_dict[hand_num[-1]] > 1:
            return "good"
        elif hand_num[0] == com_num[-1]:
            return "good"
        elif hand_num[0] >= com_num[-2] and num_dict[hand_num[0]] > 1:
            return "mid"
        else:
            return "bad"
    else:
        return "high"

def is_Flush(com_color, hand_color):
    #print("In Flush")
    if com_color['S'] + hand_color['S'] >= 5:
        return True
    if com_color['H'] + hand_color['H'] >= 5:
        return True
    if com_color['D'] + hand_color['D'] >= 5:
        return True
    if com_color['C'] + hand_color['C'] >= 5:
        return True
    return False

def is_Straight(com_num, hand_num):
    #print("In Straight")
    card_set = set(com_num) | set(hand_num)
    if 14 in card_set:
        card_set.add(1)
    card_list = list(card_set)
    card_list.sort()
    i = 0
    straight = False
    while(i + 4 < len(card_list)):
        if card_list[i+4] - card_list[i] == 4:
            straight = True
            break
        i += 1
    if straight:
        return True
    return False

def has_Draw(com_color, com_num, hand_color, hand_num, result):
    #print("In Draw")
    if com_color['S'] + hand_color['S'] == 4 and hand_color['S'] != 0:
        result["flushdraw"] = True
    elif com_color['H'] + hand_color['H'] == 4 and hand_color['H'] != 0:
        result["flushdraw"] = True
    elif com_color['D'] + hand_color['D'] == 4 and hand_color['D'] != 0:
        result["flushdraw"] = True
    elif com_color['C'] + hand_color['C'] == 4 and hand_color['C'] != 0:
        result["flushdraw"] = True
    out = 0
    for i in range(1, 15):
        new = com_num + [i]
        if is_Straight(new, hand_num):
            out += 1
    if out == 2:
        result["2enddraw"] = True
    return result


def hand_eval(community_card, hole_card, card_info):
    strength = card_info["hand"]["strength"]
    combo_high = card_info["hand"]["high"]
    combo_low = card_info["hand"]["low"]
    hole_high = card_info["hole"]["high"]
    hole_low = card_info["hole"]["low"]

    com_color = {'S': 0, 'H': 0, 'D': 0, 'C': 0}
    com_num = []
    hand_color = {'S': 0, 'H': 0, 'D': 0, 'C': 0}
    hand_num = []
    for card in community_card:
        com_num.append(card2int(card))
        com_color[card[0]] += 1
    hand_color[hole_card[0][0]] += 1
    hand_num.append(card2int(hole_card[0]))
    hand_color[hole_card[1][0]] += 1
    hand_num.append(card2int(hole_card[1]))
    com_num.sort()
    hand_num.sort()
    if len(community_card) >= 3:
        if strength == "TWOPAIR":
            if combo_high == hole_high and combo_low == hole_low:
                strength = "GOODTWO"
            elif hole_low == combo_high:
                strength = "GOODTWO"
            else:
                strength = "BADTWO"
        elif strength == "ONEPAIR":
            if hole_high == combo_high and combo_high >= com_num[-1]:
                strength = "GOODPAIR"
            elif hole_low == combo_high and combo_high >= com_num[-1]:
                strength = "GOODPAIR"
            else:
                strength = "BADPAIR"
    result = {
            "strength": strength,
            "flushdraw": False,
            "2enddraw": False
    }
    result = has_Draw(com_color, com_num, hand_color, hand_num, result)
    return result

def combo_rank(card_info):
    strength = card_info["strength"]
    if strength == "STRAIGHTFLASH":
        return 3
    elif strength == "FOURCARD":
        return 3
    elif strength == "FULLHOUSE":
        return 3
    elif strength == "FLASH":
        return 3
    elif strength == "STRAIGHT":
        return 3
    elif strength == "THREECARD":
        return 3
    elif strength == "GOODTWO":
        return 3
    elif strength == "BADTWO":
        return 1
    elif strength == "GOODPAIR":
        return 2
    elif strength == "BADPAIR":
        return 1
    elif strength == "HIGHCARD":
        if card_info["flushdraw"] or card_info["2enddraw"]:
            return 1
        else:
            return 0
