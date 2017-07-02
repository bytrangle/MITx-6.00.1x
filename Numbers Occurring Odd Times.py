def largest_odd_times(L):
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

