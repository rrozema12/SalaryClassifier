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
    n0 = (len(table) * 2) / 3
    return randomized[0:n0], randomized[n0:]


def cut(table, numTest):
    """ Splits the table into a specific number of training sets
    returns test, training
    """
    randomized = _randomize(table)
    return randomized[0:numTest], randomized[numTest:]


def _bag(table):
    return [table[randint(0, len(table) - 1)] for _ in range(len(table))]


def bagging(table, n):
    """ Generates n test and remanider sets with replacement

    :param table: a table
    :param n: number of pairs of samples to create
    :return: A list of tuples in the form
            [(training1, test1), ... , (trainingn, testn)]
    """
    bags = []
    size_test = int(.63 * len(table))
    for i in range(n):
        current_bag = _bag(table)
        bags.append((current_bag[:size_test], current_bag[size_test:]))
    return bags