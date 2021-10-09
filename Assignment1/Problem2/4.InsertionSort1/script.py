#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def insertionSort1(n, arr):
    # Write your code here
    probe = arr[-1]

    for ind in range(len(arr)-2, -1, -1):
        if arr[ind] > probe:
            arr[ind+1] = arr[ind]
            print(" ".join(map(str, arr)))
        else:
            arr[ind+1] = probe
            print(" ".join(map(str, arr)))
            break

    if arr[0] > probe:
        arr[0] = probe
        print(" ".join(map(str, arr)))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
