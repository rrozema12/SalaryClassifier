# util.py
# general utility stuff.

import itertools

# Return a col list
def getCol(table, index):
    col = []
    for row in table:
        if (row[index] == 'NA'): continue
        col.append(row[index])
    return col

def appendToDict(dictionary, key, arr):
    """ Appends to a dictionary with arrays """
    try:
        dictionary[key].append(arr)
    except KeyError:
        dictionary[key] = [arr]
    return dictionary

def these(dictionary, *keys):
    """ Gets all the values for a list of keys """
    return [dictionary[key] for key in keys]

def flipKeyValues(dictionary):
    newDict = {}
    for key, value in dictionary.iteritems():
        newDict[value] = key
    return newDict

# Will attempt to convert the element
# to its correct type
def toCorrectType(test):
    try:
        return int(test)
    except ValueError:
        try:
            return float(test)
        except ValueError:
            return test

# Calculate a median
def median(row):
    newRow = filterNA(row)
    middleIndex = len(newRow)/2

    if (len(newRow) % 2 != 0): # odd
        return sorted(newRow)[middleIndex]
    else: # even
        sortedCols = sorted(newRow)
        return (sortedCols[middleIndex] + sortedCols[middleIndex-1])/2

# Kills any "NA"s in the list
def filterNA(row):
    newList = []
    for col in row:
        if (col != "NA" and col != "'NA'"):
            newList.append(col)
    return newList

def mean(row):
    row = filterNA(row)
    return sum(row)/len(row)

def getValues(dictionary, sorted=True):
    """ Gets the values of a dictionary """
    values = []
    for key, value in dictionary.iteritems():
        values.append(value)
    return values

def getKeys(dictionary, sorted=True):
    """ Gets the keys of a dictionary """
    keys = []
    for key, value in dictionary.iteritems():
        keys.append(key)
    return keys

# Sets the value as the key and the key as the value
def flipKeyValues(dictionary):
    newDict = {}
    for key, value in dictionary.iteritems():
        newDict[value] = key
    return newDict

def multiReplace(array, indices, replacements):
    for replace_index, index in enumerate(indices):
        array[index] = replacements[replace_index]
    return array

def replaceWhere(array, oldValue, newValue):
    newArray = []
    for el in array:
        if el == oldValue:
            el = newValue
        newArray.append(el)
    return newArray

def multiGet(array, indices):
    returnable = []
    for i in indices:
        returnable.append(array[i])
    return returnable

def isString(test):
    return isinstance(test, basestring)

def colIsString(col):
    for item in col:
        if item == 'NA':
            continue
        elif isString(item):
            return True
    return False

def getFromDict(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None


# Creates a `length`-element list where each element is dummy
# Ex: dummyList("dummy", 3)  would return:
# ["dummy", "dummy", "dummy"]
def dummyList(dummy, length):
    returnable = []
    for _ in itertools.repeat(None, length):
        returnable.append(dummy)
    return returnable

# Deletes many indexes from a list
# Adapted from this
# http://stackoverflow.com/questions/497426/deleting-multiple-elements-from-a-list
# Question
def deleteMany(els, args):
    indexes = sorted(list(args), reverse=True)

    for index in indexes:
        del els[index]
    return els

def tryConvertFloat(test):
    try:
        x = float(test)
        return x
    except ValueError:
        return test

# Makes an array pretty printable
def arrayWithLineEnds(array):
    string = ""
    for row in array:
        string += str(row) + "\n"
    return string

def prettyPrint(table):
    print arrayWithLineEnds(table)

def listToCorrectType(array):
    newArray = []
    for el in array:
        newArray.append(toCorrectType(el))
    return newArray

def tableToCorrectType(table):
    newTable = []
    for row in table:
        newTable.append(listToCorrectType(row))
    return newTable

# Will attempt to convert the element
# to its correct type
def toCorrectType(test):
    try:
        return int(test)
    except ValueError:
        try:
            return float(test)
        except ValueError:
            return test

def problemRows(table):
    newTable = []
    for row in table:
        if 'NA' in row:
            newTable.append(row)
    return newTable

def hasMissing(array):
    for el in array:
        if (el == 'NA'):
            return True
    return False

# Returns col values at the colDesiredIndex
# where the col at the colTestIndex == colTestValue
def getColBy(table, colDesiredIndex, colTestIndex, colTestValue):
    cols = []
    for row in table:
        includeCol = False
        for colIndex, col in enumerate(row):
            if colIndex == colTestIndex:
                includeCol = (col == colTestValue)
        if (includeCol):
            cols.append(row[colDesiredIndex])
    return cols

def getBins(col, num_bins):
    min_value = int(min(col))
    max_value = int(max(col))

    width = (int(max_value) - int(min_value)) / num_bins
    tooHigh = list(range(min_value + width, max_value + 1, width))
    return map(lambda x: (x-width), tooHigh)

def createDict(keys, values):
    data = {}
    for i, key in enumerate(keys):
        data[key] = values[i]
    return data

# Takes a list of numbers (ranges) that
# define the low end of a series of ranges.
# Returns the low end of the range.
#
# If it's not within the range, return false
# If it is greater than the max, it will return
# the lowest end of the max
def getLowRange(ranges, test):
    for r in reversed(ranges):
        if test >= r:
            return r
    return False

def getRangeStrings(ranges):
    strings = []
    for i in range(len(ranges)-1):
        strings.append(str(ranges[i]) + "-" + str(ranges[i+1]))
    strings.append(str(ranges[len(ranges)-1]) + "+")
    return strings

def getXbyY(table, x_index, y_index, filterNA = True):
    points = []
    for row in table:
        x = row[x_index]
        y = row[y_index]
        if (filterNA):
            if (x == 'NA' or y == 'NA'):
                continue

        points.append([x, y])
    return points

def getCountDictionary(array):
    dictionary = {}
    for el in array:
        if getFromDict(dictionary, el) is None:
            dictionary[el] = 1
        else:
            dictionary[el] += 1
    return dictionary

def translate(array, dictionary):
    return [dictionary[el] for el in array]


def genNumbers(start, count, increment):
    array = []
    number = start
    for i in range(count):
        array.append(number)
        number = number + increment
    return array


def dictionaryToArray(dictionary):
    return [ value for key, value in dictionary.iteritems()]


if __name__ == '__main__':
    table = [[1, 2, 'hi', 500, 2.3], [0, 4, 'blonds', 400, 3.3], [4, 2, 'dudes', 300, 1.3]]
    print normalizeTable(table, 0)
