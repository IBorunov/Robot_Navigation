import random
import heapq
import matplotlib.pyplot as plt
import numpy as np


def generate_map(size, obstacle_chance=0.3):
    """Функция генерации карты и препятствий на ней"""
    _map = []
    for i in range(size):
        row = []
        for j in range(size):
            if random.random() < obstacle_chance:
                row.append(1)  # препятствие
            else:
                row.append(0)  # свободная ячейка
        _map.append(row)

    # проверяем, нет ли у нас препятствий в начальной и конечной точке
    _map[0][0] = 0
    _map[size-1][size-1] = 0
    return _map


def find_neighbouring_nodes(node, _map):
    """Функция определения соседних узлов"""
    neighbours = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # вверх, вниз, влево, вправо
    for direction in directions:
        neighbour = (node[0] + direction[0], node[1] + direction[1])
        # проверяем, не выходим ли мы за границы карты
        if 0 < neighbour[0] < len(_map) and 0 < neighbour[1] < len(_map):
            neighbours.append(neighbour)
    return neighbours


def heuristic(node, goal):
    """ Эвристическая функция для A* (манхэттенское расстояние) """
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])


def a_star(_map, start, goal):
    """
    Реализация алгоритма A* для поиска кратчайшего пути на сетке.
    Возвращает:
    list of tuple of int - содержащий кратчайший путь от start до goal, или пустой список, если путь не найден.
    """
    open_set = []
    heapq.heappush(open_set, (0, start))  # Начальная точка добавляется в open_set с оценкой 0
    came_from = {}  # Словарь для сохранения пути
    g_score = {start: 0}  # Стоимость пути от начала до текущей точки
    f_score = {start: heuristic(start, goal)}  # Оценочная стоимость от начала до цели через текущую точку

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current)  # Если текущий узел - цель, восстанавливаем путь

        for neighbour in find_neighbouring_nodes(current, _map):
            if _map[neighbour[0]][neighbour[1]] == 1:
                continue  # Пропускаем, если соседний узел - препятствие

            tentative_g_score = g_score[current] + 1  # Предварительная стоимость пути до соседнего узла

            if neighbour not in g_score or tentative_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = tentative_g_score
                f_score[neighbour] = tentative_g_score + heuristic(neighbour, goal)
                heapq.heappush(open_set, (f_score[neighbour], neighbour))  # Добавляем соседний узел в open_set

    return []  # Если все узлы обработаны и цель не достигнута, возвращаем пустой список