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


"""NEW FINAL PROJECT MAPPING STUFF"""
def get_job_type(x):
    """ returns the int value for the nominal value survived

    :param x: a value that is either 'yes' or 'no'
    :return: returns 1 if x is yes, or 0 if x is no
    """
    if x == 'Government':
        return 1
    elif x == 'Priavte':
        return 2
    elif x == 'Self-Employed':
        return 3
    else:
        return 0

def get_degree(x):
    """ returns the int value for the nominal value sex

    :param x: a value that is either 'male' or 'female'
    :return: returns 1 if x is male, or 0 if x is female
    """
    if x == 'HS':
        return 1
    elif x == 'Bachelors':
        return 2
    elif x == 'Masters':
        return 3
    elif x == 'Doctorate':
        return 4
    elif x == 'College-drop-out':
        return 5
    elif x == 'Associate':
        return 6
    elif x == 'Middleschool':
        return 7
    elif x == 'Elementary':
        return 8
    else:
        return 0


def get_marital_status(x):
    """ returns the int value for the nominal value age

    :param x: a value that is either 'adult' or 'child'
    :return: returns 1 if x is adult, or 0 if x is fchild
    """
    if x == 'Never-married':
        return 1
    elif x == 'Married-civ-spouse':
        return 2
    elif x == 'Divorced':
        return 3
    elif x == 'Married-spouse-absent':
        return 4
    elif x == 'Widowed':
        return 5
    elif x == 'Seperated':
        return 6
    else:
        return 0


def get_ethnicity(x):
    """ returns the int value for the ordinal value class

    :param x: a value that is either 'crew', 'first', 'second', or 'third'
    :return: returns 3 if 'crew', 2 if first, etc.
    """
    if x == 'White':
        return 1
    elif x == 'Black':
        return 2
    elif x == 'Amer-Indian-Eskimo':
        return 3
    elif x == 'Asian-Pac-Islander':
        return 4
    else:
        return 0

def get_gender(x):
    """ returns the int value for the ordinal value class

    :param x: a value that is either 'crew', 'first', 'second', or 'third'
    :return: returns 3 if 'crew', 2 if first, etc.
    """
    if x == 'Male':
        return 1
    else:
        return 0

def get_country(x):
    """ returns the int value for the ordinal value class

     :param x: a value that is either 'crew', 'first', 'second', or 'third'
     :return: returns 3 if 'crew', 2 if first, etc.
     """
    if x == 'United-States':
        return 1
    elif x == 'Philippines':
        return 2
    elif x == 'Puerto-Rico':
        return 3
    elif x == 'Mexico':
        return 4
    elif x == 'Dominican-Republic':
        return 5
    elif x == 'Portugal':
        return 6
    elif x == 'Canada':
        return 7
    elif x == 'Taiwan':
        return 8
    else:
        return 0

def get_salary(x):
    """ returns the int value for the ordinal value class

    :param x: a value that is either 'crew', 'first', 'second', or 'third'
    :return: returns 3 if 'crew', 2 if first, etc.
    """
    if x == '>50K':
        return 1
    else:
        return 0




if __name__ == '__main__':
    row = [18.0,8,307.0,130.0,3504,12.0,70,1,"chevrolet chevelle malibu",2881]
    print getNamedTuples(row, 'mpg', 'origin', 'weight')
