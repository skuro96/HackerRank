#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

# Write Your Code Here
cnt_swap = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            cnt_swap += 1

print('Array is sorted in', cnt_swap, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[n - 1])