def largest_odd_times(L):
    """ 
    Assumes L is a non-empty list of ints
    Returns the largest element of L that occurs an odd number 
    of times in L. If no such element exists, returns None
    """
    maxoccur = 0
    wantednum = 0
    for i in L:
        occurence = L.count(i)
        if occurence % 2 != 0 and i > wantednum:
            wantednum = i
            maxoccur = occurence
    if maxoccur % 2 != 0:
        return wantednum
    else:
        return

