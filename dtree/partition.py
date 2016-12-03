from random import randint

def _randomize(table):
    """ Randomizes the table """
    randomized = table[:]
    n = len(table)
    for i in range(n):
        j = randint(0, n-1)
        randomized[i], randomized[j] = randomized[j], randomized[i]
    return randomized

def holdout(table):
    """ Splits the table into 1/3 test and 2/3 training set
    returns test, training
    """
    randomized = _randomize(table)
    n0 = (len(table) * 2)/3
    return randomized[0:n0], randomized[n0:]

def cut(table, numTest):
    """ Splits the table into a specific number of training sets
    returns test, training
    """
    randomized = _randomize(table)
    return randomized[0:numTest], randomized[numTest:]
