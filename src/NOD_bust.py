# -*- coding: utf-8 -*-

# Алгоритм вычисления GCD перебором

def bust_nod(num1, num2):
    minNumber = min(num1, num2)
    while True:
        if (num1 % minNumber) == 0 and (num2 % minNumber) == 0:
            return minNumber
        else:
            minNumber = minNumber - 1