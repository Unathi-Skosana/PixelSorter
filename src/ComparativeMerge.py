''' Module for comparative merge sorting '''
from numpy import zeros, array

def merge(pri_items, sec_items, pri_aux, sec_aux, lowerbound, upperbound):
    ''' docstring '''
    less = lambda value_one, value_two : value_one > value_two
    mid = int(lowerbound + (upperbound - lowerbound)/2)
    i = lowerbound
    j = mid + 1
    for k in range(lowerbound, upperbound + 1):
        pri_aux[k], sec_aux = pri_items[k], sec_items[k]
    for index in range(lowerbound, upperbound + 1):
        if i > mid:
            pri_items[index], sec_items[index] = pri_aux[j], sec_aux[j]
            j += 1
        elif j > upperbound:
            pri_items[index], sec_items[index] = pri_aux[i], sec_aux[i]
            i += 1
        elif less(pri_aux[i], pri_aux[j]):
            pri_items[index], sec_items[index] = pri_aux[j], sec_aux[j]
            j += 1
        else:
            pri_items[index], sec_items[index] = pri_aux[i], sec_aux[i]
            i += 1

def comparative_merge_sort(pri_items, sec_items):
    ''' docstring '''
    pri_aux = zeros((len(pri_items,), dtype=float))
    sec_aux = zeros((len(pri_items,), dtype=float))
    sort(pri_items, sec_items, pri_aux, sec_aux, 0, len(pri_items) - 1)
    assert is_sorted(pri_items)

def sort(pri_items, sec_items, pri_aux, sec_aux, lowerbound, upperbound):
    ''' docstring '''
    if upperbound <= lowerbound:
        return
    mid = int(lowerbound + (upperbound - lowerbound)/2)
    sort(pri_items, sec_items, pri_aux, sec_aux, lowerbound, mid)
    sort(pri_items, sec_items, pri_aux, sec_aux, mid + 1, upperbound)
    merge(pri_items, sec_items, pri_aux, sec_aux, lowerbound, upperbound)

def is_sorted(pri_items):
    ''' docstring '''
    for i in range(1, len(pri_items)):
        if pri_items[i] < pri_items[i-1]:
            return False
    return True
