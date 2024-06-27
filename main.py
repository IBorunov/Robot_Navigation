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

