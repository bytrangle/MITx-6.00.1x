def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    if contains_digits(s) == True:
        digitSum = 0
        for i in s:
            try:
                digitSum += int(i)
            except:
                pass
        return digitSum
    else:
        raise ValueError
def contains_digits(s):
    return any(i.isdigit() for i in s)
