
def findMax(seq):
    maxValue = seq[0]
    for a in seq:
        if a > maxValue:
            maxValue = a
    return(maxValue)


def findMin(seq):
    minValue = seq[0]
    for a in seq:
        if a < minValue:
            minValue = a
    return(minValue)
