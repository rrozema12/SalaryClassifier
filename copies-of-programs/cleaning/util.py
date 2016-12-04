import itertools

# Return a col list
def getCol(table, index):
    col = []
    for row in table:
        if (row[index] == 'NA'): continue
        col.append(row[index])
    return col

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

# Gets the values of a dictionary
def getValues(dictionary):
    values = []
    for key, value in dictionary.iteritems():
        values.append(value)
    return values

# Gets the keys of a dictionary
def getKeys(dictionary):
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


if __name__ == '__main__':
    table = [[1, "cats"], [2, "dogs"], [1, "tvs"]]
    print getColBy(table, 1, 0, 1)
