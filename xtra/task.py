#!/usr/bin/python3
# Author:   @AgbaD || @agba_dr3


# ===================== 1 ======================== #
import random


def pour(array):
    i = 0
    while i < len(array):
        a = array[i]
        b = random.choice(array)
        for j in array:
            if a + b + j == 0:
                print(a, b, j)
                return
        i += 1
    print('Not found')

# ===================== 2 ======================== #


def bin_to_dec(n):
    """
    :param n: binary number
    :return: binary converted to decimal
    """
    try:
        decimal = int(n, 2)
        return decimal
    except ValueError:
        return "Invalid binary number"


def dec_to_bin(n):
    """
    :param n: decimal number
    :return: decimal converted to binary
    """
    return bin(int(n)).replace("0b", "")


def add_bin(x: str, y: str):
    """
    :param x: first binary number
    :param y: first binary number
    :return: sum of binary numbers
    """
    a = bin_to_dec(x)
    b = bin_to_dec(y)
    c = a + b
    return dec_to_bin(c)


# ===================== 3 ======================== #

answers = 1, 2, 3, 4, 5, 6


# ===================== 4 ======================== #

ans = [2, 33, 222, 14]


# ===================== 5 ======================== #
answer = (0, 1)


if __name__ == "__main__":
    h = []
    for i in range(50):
        if i % 3 == 0:
            h.append(-i)
        else:
            h.append(i)
    pour(h)
