import math

def squares(num):
    pos_square = math.sqrt(num)
    neg_square = math.sqrt(num)

    if int(pos_square + 0.5) ** 2 == num:
        return True
    elif int(neg_square + 0.5) ** 2 == num:
        return True
    else:
        return False