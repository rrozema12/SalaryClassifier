import util
import constants

def getDeptEnergyRating(x):
    """ Returns the dept of energy number rating"""

    # Gets the range values for the DOE rankings
    keys     = util.getValues(constants.DOE_RATINGS)

    # Gets the left-end of the range x belongs in
    lowRange = util.getLowRange(keys, x)

    # Flips the dictionary, so we can query by value
    byValue  = util.flipKeyValues(constants.DOE_RATINGS)

    return byValue[lowRange]


def getNHTSASize(x):
    """ Returns the NHTSA Vehicle size """

    # Gets the range values for the DOE rankings
    keys     = util.getValues(constants.NHTSA)

    # Gets the left-end of the range x belongs in
    lowRange = util.getLowRange(keys, x)

    # Flips the dictionary, so we can query by value
    byValue  = util.flipKeyValues(constants.NHTSA)

    return byValue[lowRange]


def convertRowIntoIndexValuePairs(row):
    """ Converts [x, y, z, ...] into [(0, x), (1, y), (2, z)]
    for use in the classifiers in their "where" statements
    """
    return [ (index, value) for index, value in enumerate(row)]


def getNamedTuples(row, names):
    """ Gets a bunch of tuples by their name
    Ex: getNamedColsFromRow(row, 'mpg', 'origin', 'weight')
        might return [(0, 18.0), (4, 3504), (7, 1)]
    WARNING: These don't necessarily return in any specific order.
    """
    tuples = []
    namesIndexes = [constants.INDICES[name] for name in names]
    for index, value in enumerate(row):
        if index in namesIndexes:
            tuples.append((index, value))
    return tuples


def get_survived_value(x):
    """ returns the int value for the nominal value survived

    :param x: a value that is either 'yes' or 'no'
    :return: returns 1 if x is yes, or 0 if x is no
    """
    if x == 'yes':
        return 1
    else:
        return 0

def get_sex_value(x):
    """ returns the int value for the nominal value sex

    :param x: a value that is either 'male' or 'female'
    :return: returns 1 if x is male, or 0 if x is female
    """
    if x == 'male':
        return 1
    else:
        return 0


def get_age_value(x):
    """ returns the int value for the nominal value age

    :param x: a value that is either 'adult' or 'child'
    :return: returns 1 if x is adult, or 0 if x is fchild
    """
    if x == 'adult':
        return 1
    else:
        return 0


def get_class_value(x):
    """ returns the int value for the ordinal value class

    :param x: a value that is either 'crew', 'first', 'second', or 'third'
    :return: returns 3 if 'crew', 2 if first, etc.
    """
    if x == 'crew':
        return 3
    elif x == 'first':
        return 2
    elif x == 'second':
        return 1
    else:
        return 0



if __name__ == '__main__':
    row = [18.0,8,307.0,130.0,3504,12.0,70,1,"chevrolet chevelle malibu",2881]
    print getNamedTuples(row, 'mpg', 'origin', 'weight')
