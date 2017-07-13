'''Merge sort'''

def merge(items, aux, lowerbound, upperbound):
    ''' docstring '''
    mid = int(lowerbound + (upperbound - lowerbound)/2)
    i = lowerbound
    j = mid + 1
    for k in range(lowerbound, upperbound + 1):
        aux[k] = items[k]
    for index in range(lowerbound, upperbound + 1):
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
    aux = []
    for i in range(len(items)):
        aux.append(0)
    upperbound = len(items) - 1
    lowerbound = 0
    sort(items, aux, lowerbound, upperbound)
    assert is_sorted(items)

def sort(items, aux, lowerbound, upperbound):
    ''' docstring '''
    if upperbound <= lowerbound:
        return
    mid = int(lowerbound + (upperbound - lowerbound)/2)
    sort(items, aux, lowerbound, mid)
    sort(items, aux, mid + 1, upperbound)
    merge(items, aux, lowerbound, upperbound)

def is_sorted(items):
    ''' docstring '''
    for i in range(1, len(items)):
        if items[i] < items[i-1]:
            return False
    return True

def less(value_one, value_two):
    ''' docstring '''
    return value_one > value_two
