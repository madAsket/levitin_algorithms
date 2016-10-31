# -*- coding: utf-8 -*-

# Алгоритм поиска минимальной охватывающей окружности для N точек на плоскости.
import random
from math import sqrt
from time import sleep

# Вспомогательная функция нахождения окружности по двум точкам
def circle_by_2_points((x1, y1), (x2, y2)):
    # Найдем середину отрезка - центр окружности
    Cx = (x1 + x2)/2
    Cy = (y1 + y2)/2
    # Радиус окружности - расстояние от одной точки до центра окружности
    radius = points_distance((x1, y1), (Cx, Cy))
    return [(Cx, Cy), radius]

# Вспомогательная функция нахождения  окружности по трем точкам
def circle_by_3_points((x1, y1), (x2, y2), (x3, y3)):
    A = x2 - x1
    B = y2 - y1
    C = x3 - x1
    D = y3 - y1
    E = A * (x1 + x2) + B * (y1 + y2)
    F = C * (x1 + x3) + D * (y1 + y3)
    G = 2 * (A * (y3 - y2) - B * (x3 - x2))
    if G == 0:
        return None
    Cx = (D * E - B * F) / G
    Cy = (A * F - C * E) / G
    radius = points_distance((x1, y1), (Cx, Cy))
    return [(Cx, Cy), radius]

# Вспомогательная функция нахождения расстояниям между двумя точками
def points_distance((x1, y1), (x2, y2)):
    return sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))


def get_far_point(current_point, points):
    far_point = None
    far_point_distance = 0
    # 4. Находим самую удалённую точку от первой.
    for p in points:
        dist = points_distance(current_point, p)
        if dist > far_point_distance:
            far_point_distance = dist
            far_point = p
    return far_point, far_point_distance


# Описание алгоритма:


# 8. Если к-во опорных точек текущей окружности было равным 3, то переходим к пункту 9. Иначе проверим выходит
# ли неиспользованная опорная точка за пределы текущей окружности.
# Если не выходит, то заменяем её на новую точку ( к-во опорных точек останется равным 2 ).
# Иначе добавляем новую точку в опорные и строим окружность по трём точкам. Переходим к пункту 10.

# 9. Находим из двух неиспользованных точек самую удаленную от центра текущей окружности.
# Если эта точка лежит вне круга, то она будет третьей опорной и тогда строим окружность по трём новым опорным точкам.
# Иначе опорных точек останется две.

# 10. Если радиус окружности не вырос за время цикла, то конец алгоритма, иначе идём на начало цикла.

# Основная функция
# @return [(circleX, circleY), radius]
def min_circle_around_points(points):
    # Если к-во входных точек равно 0, то возвращаем неопределённую окружность.
    if len(points) == 0:
        return None
    first_point = points[0]
    # Если к-во входных точек равно 1, то возвращаем окружность с центром в этой точке и нулевым радиусом.
    if len(points) == 1:
        return [first_point, 0]

    # Если к-во входных точек равно 2, то возвращаем окружность с центром в середине между
    # этими точками и соответсвующим радиусом.
    if len(points) == 2:
        return circle_by_2_points(*points)
    # Находим самую удалённую точку от первой.
    far_point, far_point_distance = get_far_point(first_point, points)
    # Если это расстояние будет равно 0, то возвращаем окружность с центром в первой точке и нулевым радиусом.
    if far_point_distance == 0:
        return [first_point, 0]
    # Иначе считаем эти точки опорными и строим по ним окружность
    basis_points = [first_point, far_point]
    target_circle = circle_by_2_points(*basis_points)

    # Начало цикла.
    while True:
        # Находим самую удаленную точку от центра текущей окружности.
        far_point, far_point_distance = get_far_point(target_circle[0], points)
        # Если это расстояние не больше, чем радиус текущей окружности
        # или индекс самой удалённой точки равен одному из индексов опорных точек, то выходим из цикла.
        if far_point_distance <= target_circle[1] or far_point in basis_points:
            return target_circle
        # Иначе будем включать эту точку в число опорных
        basis_candidate = far_point

        # Найдём среди опорных точек самую удаленную от новой точки
        far_point, far_point_distance = get_far_point(basis_candidate, basis_points)
        # Построим текущую окружность по двум точкам ( новой и найденной ).
        new_circle = circle_by_2_points(basis_candidate, far_point)

        # Если к-во опорных точек текущей окружности было равным 3
        if len(basis_points) == 3:
            # Находим из двух неиспользованных точек самую удаленную от центра текущей окружности.
            other_basis_points = []
            for bp in basis_points:
                if bp != far_point:
                    other_basis_points.append(bp)
            unused_far_point, unused_far_point_distance = get_far_point(new_circle[0], other_basis_points)
            distance_to_bp = points_distance(unused_far_point, new_circle[0])
            # Если эта точка лежит вне круга, то она будет третьей опорной и тогда строим окружность
            # по трём новым опорным точкам.
            basis_points = [far_point, basis_candidate]
            if distance_to_bp > new_circle[0]:
                basis_points.append(unused_far_point)
                new_circle = circle_by_3_points(*basis_points)
                if new_circle[1] > target_circle[1]:
                    target_circle = new_circle
                    continue
                return new_circle
        else:
            # Проверим выходит ли неиспользованная опорная точка за пределы текущей окружности.
            other_basis_point = None
            other_basis_point_index = 0
            for bp in basis_points:
                if bp != far_point:
                    other_basis_point = bp
                    break
                other_basis_point_index += 1

            distance_to_bp = points_distance(other_basis_point, new_circle[0])
            # Если выходит - добавляем новую точку в опорные и строим окружность по трём точкам.
            if distance_to_bp > new_circle[1]:
                basis_points.append(basis_candidate)
                new_circle = circle_by_3_points(*basis_points)
                # Если радиус окружности не вырос за время цикла, то конец алгоритма, иначе идём на начало цикла.
                if new_circle[1] > target_circle[1]:
                    target_circle = new_circle
                    continue
                return new_circle
            # Если не выходит, то заменяем её на новую точку (к-во опорных точек останется равным 2).
            else:
                basis_points[other_basis_point_index] = basis_candidate
                target_circle = new_circle


def test():
    points = [
        (4.0, 4.0), (3.0, 3.0), (5.0, 7.0), (3.0, 10.0), (8.0, 8.0), (7.0, 5.0)
    ]
    resultCircle = min_circle_around_points(points)
    print "Result: %s"%resultCircle
test()