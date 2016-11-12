# -*- coding: utf-8 -*-
from time import sleep

# Алгоритм построения корневого дерева из свободного дерева


def root_tree_builder(matrix, rootVertex, marks):
    markedVertex = []

    def build_childs(vertex, nestedTree):
        markedVertex.append(vertex)
        # Идем по значениям связей заданной вершины и отмечаем дочерние
        index = 0
        childTree = {}
        for p in matrix[vertex]:
            # Если дочерняя еще не добавлена в отмеченные и есть связь, строим для нее внутренние связи
            if index not in markedVertex and p == 1:
                build_childs(index, childTree)
            index += 1
        # Добавляем получившееся поддерево для родительской вершины
        nestedTree[marks[vertex]] = childTree
        return nestedTree

    # Запуск - строим дерево, начиная с заданного коря rootVertex
    return build_childs(rootVertex, {})


def test():
    matrix = [
    #    A     B     C     D     E     F
        [0,    1,    1,    0,    0,    0], #A
        [1,    0,    0,    0,    0,    0], #B
        [1,    0,    0,    1,    1,    0], #C
        [0,    0,    1,    0,    0,    0], #D
        [0,    0,    1,    0,    0,    1], #E
        [0,    0,    0,    0,    1,    0]  #F
    ]
    rootVertex = 2 # C
    # Наименования вершин
    marks = ["A", "B", "C", "D", "E", "F"]
    result = root_tree_builder(matrix, rootVertex, marks)
    print result

test()