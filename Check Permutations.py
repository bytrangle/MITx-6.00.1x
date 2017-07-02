#Write a Python function that takes in two lists and calculates whether they are permutations of each other. 
#The lists can contain both integers and strings. 
#We define a permutation as follows:
  #the lists have the same number of elements
  #list elements appear the same number of times in both lists
#If the lists are not permutations of each other, the function returns False. 
#If they are permutations of each other, the function returns a tuple consisting of the following elements:
  #the element occuring the most times
  #how many times that element occurs
  #the type of the element that occurs the most times
#If both lists are empty return the tuple (None, None, None). 
#If more than one element occurs the most number of times, you can return any of them.

def is_list_permutation(L1, L2):
  '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
    If they are permutations of each other, returns a 
    tuple of 3 items in this order: 
    the element occurring most, how many times it occurs, and its type
    '''
    maxcount = 0
    if len(L1) == 0 and len(L2) == 0:
        return (None, None, None)
    if len(L1) == len(L2):
        for i in L1:
            if i in L2:
                ls1cnt = L1.count(i)
                ls2cnt = L2.count(i)
                if ls1cnt == ls2cnt:
                    if ls1cnt > maxcount:
                        maxcount = ls1cnt
                        result = i
                        permutype = type(i)
                        wantedtup = (result, maxcount, permutype)
                else:
                    return False
        return wantedtup
    else:
        return False
