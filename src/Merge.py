'''Merge sort'''
from numpy import zeros
def merge(items, aux, l_bound, u_bound):
    ''' docstring '''
    mid = int(l_bound + (u_bound - l_bound)/2)
    less = lambda val1, val2: val1 > val2
    i = l_bound
    j = mid + 1
    for k in range(l_bound, u_bound + 1):
        aux[k] = items[k]
    for index in range(l_bound, u_bound + 1):
        if i > mid:
            items[index] = aux[j]
            j += 1
        elif j > upperbound:
            items[index] = aux[i]
            i += 1
        elif less(aux[i], aux[j]):
            items[index] = aux[j]
            j += 1
        else:
            items[index] = aux[i]
            i += 1

def merge_sort(items):
    ''' docstring '''
    sort(items, zeros(len(items)), 0, len(items) - 1)
    assert is_sorted(items)

def sort(items, aux, l_bound, u_bound):
    ''' docstring '''
    if u_bound <= l_bound:
        return
    mid = int(l_bound + (u_bound - l_bound)/2)
    sort(items, aux, l_bound, mid)
    sort(items, aux, mid + 1, u_bound)
    merge(items, aux, l_bound, u_bound)

def is_sorted(items):
    ''' docstring '''
    for i in range(1, len(items)):
        if items[i] < items[i-1]:
            return False
    return True
