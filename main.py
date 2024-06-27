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
