# -*- coding: utf-8 -*-

# сортировка массива методом подсчета сравнений
import random

# [65, 59, 46, 62, 14, 25, 78, 22, 47, 79]
# [7,  5,  3,  6,  0,  2,  8,  1,  4,  9]

def ccs(array):
    # Создаем массив с нулевыми весами, размером с оригинальный массив
    cnt = [0 for i in range(len(array))]
    print cnt
    # Первый цикл идет по значениям массива от 0 до len-1 (9 итераций)
    for i in range(len(array)-1):
        print "i",i
        # Второй цикл идет от значения i первого цикла 1,2... до len (Сравниваем значения всех старших индексов)
        for j in range(i + 1, len(array)):
            print "j", j
            print "arr i",array[i]
            print "arr j",array[j]
            # Если старший индекс больше младшего увеличиваем вес его индекса
            if array[i] < array[j]:
                cnt[j] += 1
            else:
                # Иначе увеличиваем вес младшего индекса
                cnt[i] += 1
    print cnt
    s = [0 for i in range(len(array))]
    # Проставляем значения из старого массива в новый массив, где место в массиве будет его весом.
    for i in range(len(array)):
        s[cnt[i]] = array[i]
    print s
    return s


def test_ccs():
    # generated_array = [random.randint(1, 100) for i in range(10)]
    generated_array = [60, 35, 81, 98, 14, 47]
    print generated_array
    ccs(generated_array)

test_ccs()