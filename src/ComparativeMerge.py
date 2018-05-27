''' Module for comparative merge sorting '''
from numpy import zeros, array

def merge(pri_items, sec_items, pri_aux, sec_aux, lowerbound, upperbound):
    print "before merge"
    print pri_items
    print sec_items
    ''' docstring '''
    mid = int(lowerbound + (upperbound - lowerbound)/2)
    i, j = lowerbound, mid + 1
    for k in range(lowerbound, upperbound + 1):
        pri_aux[k] = pri_items[k]
        sec_aux[k] = sec_items[k]
    for index in range(lowerbound, upperbound + 1):
        if i > mid:
            print "i > mid"
            pri_items[index] = pri_aux[j]
            sec_items[index] = sec_aux[j]
            j += 1
        elif j > upperbound:
            print 'j > upperbound'
            pri_items[index] = pri_aux[i]
            sec_items[index] = sec_aux[i]
            i += 1
        elif pri_aux[i] > pri_aux[j]:
            print " pri_aux[i] > pri_aux[j]"
            pri_items[index] = pri_aux[j] ; sec_items[index] = sec_aux[j]
            j += 1
        else:
            print "else "
            pri_items[index] = pri_aux[i] ; sec_items[index] = sec_aux[i]
            i += 1
    print "after merge"
    print pri_items
    print sec_items

def comparative_merge_sort(pri_items, sec_items):
    ''' docstring '''
    sort(pri_items, sec_items, zeros(len(pri_items), dtype=int), zeros(len(sec_items), dtype='i,i,i'), 0, len(pri_items) - 1)
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
if __name__ == "__main__":
    #testing the comparative_merge_sorter
    #need to put this in the test class created by unathi
    t = [1, 3, 5, 4, 0, 2, 6]
    v = [(1, 30, 50), (3,  90, 10), (5, 40 ,130), (4, 30, 50), (0, 80, 1), (2, 100, 0), (6, 23, 32)]
    #print 't = ',t
    #print 'v = ',v
    tv = zip(t, v)
    print tv
    tv = sorted(tv)
    print "\n\nsorted\n", tv
    print "tv[0][1]= {}\ntv[-1][1] = {}".format(tv[0][1], tv[-1][1])
    #comparative_merge_sort(t, v)
    #print "\nt' = ", t
    #print "v' = ", v
