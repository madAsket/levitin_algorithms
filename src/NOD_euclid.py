# -*- coding: utf-8 -*-

# Вычисление наибольшего общего делителя с помощью Алгоритма Эвклида

def euclid_nod_original(maxNum, minNum):
    r = minNum
    while maxNum - minNum != 0:
        r = maxNum - minNum
        print r
        if(r >= minNum):
            minNum = minNum
            maxNum = min(r, maxNum)
        else:
            maxNum = min(maxNum, minNum)
            minNum = r
    return r

def euclid_nod(NOD, minNum):
    while minNum != 0:
        r = NOD % minNum
        NOD = minNum
        minNum = r
    return NOD


def euclid_extended_nod(NOD, minNum, diofantC=None):
    x2 = 1
    x1 = 0
    y2 = 0
    y1 = 1
    while minNum != 0:
        q = NOD / minNum
        r = NOD - q * minNum
        NOD = minNum
        minNum = r
        x = x2 - q * x1
        y = y2 - q * y1
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    x = x2
    y = y2
    if diofantC and diofantC % NOD == 0:
        Xd = x * (diofantC / NOD)
        Yd = y * (diofantC / NOD)
        return [NOD, x, y, Xd, Yd]
    return [NOD, x, y]




print(euclid_extended_nod(60, 24, 71))