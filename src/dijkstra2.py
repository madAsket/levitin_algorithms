# -*- coding: utf-8 -*-
from time import sleep

# Поиск кратчайших путей в взвешенном орграфе от заданой точки до остальных

def dijkstra(matrix, vertexNames, startVertex):
    # Переменная путей от начальной вершины
    vertexPath = {}
    # Указываем начальную точку до каждой вершины
    for v in vertexNames:
        vertexPath[v] = startVertex
    # Отмеченные вершины, в виде ее индекса
    markedVertex = [vertexNames.index(startVertex)]

    resultMatrixWeight = matrix[vertexNames.index(startVertex)]
    while len(markedVertex) != len(matrix):
        # Взять неотмеченную вершину с мин расстоянием от startVertex
        i = 0
        minPath = None
        nextMarkedVertexIndex = None
        for vertex in resultMatrixWeight:
            # Если индекс вершины еще не отмечен берем ее
            if i not in markedVertex:
                if minPath is None or (vertex is not None and vertex < minPath):
                    nextMarkedVertexIndex = i
                    minPath = vertex
            i += 1

        markedVertex.append(nextMarkedVertexIndex)
        markedVertexName = vertexNames[nextMarkedVertexIndex]
        # Устанавливаем финальный путь до этой вершины
        if minPath is None:   # Если вершина не ведет ни в одну другую, закрываем ее
            vertexPath[markedVertexName] = 'None'
            continue
        else:
            prevMarkedVertexPath = vertexPath[markedVertexName]
            vertexPath[markedVertexName] = prevMarkedVertexPath + markedVertexName

        nextMatrix = matrix[nextMarkedVertexIndex]
        vertexIndex = 0
        for vertex in nextMatrix:
            # Если от текущей вершины есть путь до следующей
            if vertexIndex not in markedVertex and vertex is not None:
                path = vertex + minPath
                # Если раньше не было пути или путь был больше, обновляем его вес
                if resultMatrixWeight[vertexIndex] is None or path < resultMatrixWeight[vertexIndex]:
                    resultMatrixWeight[vertexIndex] = path
                    # Обновляем строковый путь до еще неотмеченных путей
                    vertexPath[vertexNames[vertexIndex]] = vertexPath[markedVertexName]
            vertexIndex += 1
    print "result weights", resultMatrixWeight
    print "result path", vertexPath


def test_dijkstra():
    matrix = [
    #    A     B     C     D     E     F
        [0,    2,    None, 3,    None, None], #A
        [None, 0,    1,    None, 4,    None], #B
        [None, None, 0,    None, None, 5   ], #C
        [None, None, None, 0,    2,    None], #D
        [None, None, None, None, 0,    1   ], #E
        [None, None, None, None, None, 0   ]  #F
    ]
    vertexNames = ['A', 'B', 'C', 'D', 'E', 'F']
    dijkstra(matrix, vertexNames, 'B')

test_dijkstra()