import numpy as np
import math


def quick_sort(arr):
    if len(arr) > 1:
        arr, l, r = pick_pivot(arr, 3)
        arr_l, pivot, arr_r, c = partition(arr, l, r)
        arr_l, cl = quick_sort(arr_l)
        arr_r, cr = quick_sort(arr_r)
        return arr_l + [pivot] + arr_r, c + cl + cr
    else:
        return arr, 0


def pick_pivot(arr, method):
    if 2 == method:
        swap(arr, 0, -1)

    if 3 == method:
        md_index = math.ceil(len(arr) / 2) - 1
        md = np.median([arr[0], arr[-1], arr[md_index]])
        if md == arr[md_index]:
            swap(arr, 0, md_index)
        if md == arr[-1]:
            swap(arr, 0, -1)

    return arr, 0, len(arr) - 1


def partition(arr, l, r):
    pivot = arr[l]
    i = l + 1
    for j in range(l+1, r+1):
        if arr[j] < pivot:
            arr = swap(arr, i, j)
            i += 1
    arr = swap(arr, l, i-1)
    return arr[l:i-1], arr[i-1], arr[i:r+1], r-l


def swap(arr, l, r):
    temp = arr[l]
    arr[l] = arr[r]
    arr[r] = temp
    return arr


fh = open('QuickSort.txt', 'r')
numbers = fh.readlines()
num = [int(x) for x in numbers]
res = quick_sort(num)
print(res[1])