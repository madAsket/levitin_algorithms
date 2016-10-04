# -*- coding: utf-8 -*-

# Вычисление наибольшего общего делителя с помощью Алгоритма Эвклида

def euclid_nod(num1, num2):
    minNum = min(num1, num2)
    NOD = max(num1, num2)
    while minNum != 0:
        r = NOD % minNum
        NOD = minNum
        minNum = r
    return NOD