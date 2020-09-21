#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())
    n_bin = bin(n)[2:]
    
    cnt = 0
    max_cnt = 0
    for b in n_bin:
        if b == '1':
            cnt += 1
            max_cnt = max(max_cnt, cnt)
        else:
            cnt = 0
    
    print(max_cnt)