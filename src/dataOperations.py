import util
import numpy
import collections
import constants

def getDeptEnergyRating(x):
    # Gets the range values for the DOE rankings
    keys     = util.getValues(constants.DOE_RATINGS)

    # Gets the left-end of the range x belongs in
    lowRange = util.getLowRange(keys, x)

    # Flips the dictionary, so we can query by value
    byValue  = util.flipKeyValues(constants.DOE_RATINGS)

    return byValue[lowRange]


# Approach 1
def getFreqDictByDOE(col):
    # Create empty dict
    keys = range(1, 11)
    freq = util.createDict(keys, [0] * len(keys))

    for el in col:
        rating = getDeptEnergyRating(el)
        freq[rating] += 1
    return freq

# Approach 2
def getFreqByEqualWidths(col, num_bins):
    keys = sorted(util.getBins(col, num_bins))
    dictionary = util.createDict(keys, [0] * len(keys))
    freq = collections.OrderedDict(sorted(dictionary.items()))

    for el in col:
        key = util.getLowRange(keys, el)
        freq[key] += 1
    return freq

def getAllOfOrigin(originDict, origin):
    return [value[origin] for key, value in originDict.iteritems()]


if __name__ == '__main__':
    print '10 =', getDeptEnergyRating(50)
    print '1 =', getDeptEnergyRating(0)
    print '7 =', getDeptEnergyRating(28)
