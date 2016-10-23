# -*- coding: utf-8 -*-

# Бинарный поиск по отсортированному списку
import random
from time import sleep


def binary_digit_search(key):
    print "key", key
    array = [i for i in range(1, 100)]
    binaryPlacement = len(array)/2
    while True:
        print "arr", array
        print "bp", binaryPlacement
        if key == array[binaryPlacement]:
            return key
        if key > array[binaryPlacement]:
            array = array[binaryPlacement:]
        elif key < array[binaryPlacement]:
            array = array[:binaryPlacement]
        binaryPlacement = len(array) / 2


def test_binary_digit_search():
    key = random.randint(1, 99)
    print binary_digit_search(key)

test_binary_digit_search()