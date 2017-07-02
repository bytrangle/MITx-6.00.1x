def dict_invert(d):
  '''
  d: dict
  Returns an inverted dictionary according to the instructions above
  '''
    reverseDict = {}
    for k, v in d.items():
        reverseDict[v] = reverseDict.get(v, [])
        reverseDict[v].append(k)
        reverseDict[v] = sorted(reverseDict[v])
    return reverseDict

