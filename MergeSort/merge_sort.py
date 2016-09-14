import math

def merge_sort(arr):
    if len(arr) >= 2:
        hlen = math.floor(len(arr) / 2)
        sarr_l = merge_sort(arr[:hlen])
        sarr_r = merge_sort(arr[hlen:])
        marr = merge(sarr_l[0], sarr_r[0])
        return marr[0], sarr_l[1] + sarr_r[1] + marr[1]
    else:
        return arr, 0


def merge(arr_l, arr_r):
    i = 0
    j = 0
    arr = []
    split_count = 0

    for _ in range(0, len(arr_l) + len(arr_r)):
        if arr_l[i] < arr_r[j]:
            arr.append([arr_l[i]])
            i += 1
            if i == len(arr_l):
                arr.append(arr_r[j:])
                return sum(arr, []), split_count
        else:
            arr.append([arr_r[j]])
            split_count += len(arr_l) - i
            j += 1
            if j == len(arr_r):
                arr.append(arr_l[i:])
                return sum(arr, []), split_count


fh = open('IntegerArray.txt', 'r')
numbers = fh.readlines()
num = [int(x) for x in numbers]
res = merge_sort(num)
print(res[1])
