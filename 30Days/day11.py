#!/bin/python3

import math
import os
import random
import re
import sys

def count_glass(array, x, y):
    cnt = 0
    for i in range(3):
        cnt += array[x][y + i]
        cnt += array[x + 2][y + i]
    cnt += array[x + 1][y + 1]
    return cnt

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_glass = -1000
    for i in range(4):
        for j in range(4):
            max_glass = max(max_glass, count_glass(arr, i, j))

    print(max_glass)