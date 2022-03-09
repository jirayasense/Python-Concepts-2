import itertools as it
from collections import Counter
from textwrap import fill
from functools import reduce
import heapq


def all_equal1(iterable):
    g = it.groupby(iterable)
    return next(g, True) and not next(g, False)

def all_equal2(lst):
    c = Counter(lst)
    return c[lst[0]] == len(lst)


def segregate_into_groups(lst, grpSize=2):
    ''' Eg -> 
          lst = [1,2,3,4,5] 
          size = 2 
          => ans := [(1,2), (3,4), (5, None)] 
    '''
    lst_iter = iter(lst)
    return it.zip_longest(*it.repeat(lst_iter, grpSize), fillvalue=None)

def segregate_into_groups2(lst, grpSize=2):
    ''' Eg -> 
          lst = [1,2,3,4,5] 
          size = 2 
          => ans := [[1,2], [3,4], [5, None]] 
    '''
    full, remain = divmod(len(lst), grpSize)
    f = full*grpSize  # index till full groups

    # Group down the full possible groups
    res = [lst[i:i+grpSize] for i in range(0, f, grpSize)]
    
    if remain: # (Edge Case to fill empty Slots with None)
        res.append([*lst[f:], *[None]*(grpSize-remain)])
    
    return res


def argsort(l, mapper, reverse=False):
    '''
        :param l: -> can be any object that cann be indexed (ie list, array, dictionary, tuple)
        :param mapper: -> applied to each element of original arr {l} to extract new element
                          if None then original element will be used itself
                          mapper takes 1 arg & return a val
                          mapper :- is kinda ValueChanged typedef alike 
        :param fun: -> fun to be applied on entire mapped list {ml} after mapper is applied to all elem
        :returns arr: array of indexes where each element-val-idx corresp to element in original array {l}

    '''
    ml = l 
    if mapper:
        ml = list(map(mapper, l))
    return sorted(range(len(l)), key=ml.__getitem__, reverse=reverse)

if __name__ == '__main__':
    #all_equal2([2,2,2])

    l = [1,2,3,4,5]
    # t1, t2 = it.repeat(iter(l), 2)

    # print(next(t1))
    # print(next(t2))

    *t, = segregate_into_groups(l, 1)
    print(t)

    t2 = segregate_into_groups2(l, 1)
    print(t2)


    # ------

    a = [1, 10, 20, 40, 22, 15]
    n = argsort(a, lambda x: abs(x-20))
    print(n)  # [2, 4, 5, 1, 0, 3]
  
