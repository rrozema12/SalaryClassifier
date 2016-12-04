import csv
import file_system
import util
import copy
import summary

# Here to keep consistent breaks
LINE_BREAK = '----------------'

def rowMatchesTable(row, table, onColumns):
    for index, testRow in enumerate(table):
        if rowsMatch(row, testRow, onColumns):
            return index
    return -1

# Returns true if the rows match `onColumns`
def rowsMatch(row1, row2, onColumns):
    count = 0
    for r1_index, r2_index in onColumns.iteritems():
        if row1[r1_index] == row2[r2_index]:
            count += 1
    return count == len(onColumns)

# Combines the rows and removes the duplicate columns defined in
# onColumns
def newRow(row1, row2, onColumns):
    removalIndices = util.getValues(onColumns)
    row2Copy = copy.copy(row2)
    row2Copy = util.deleteMany(row2Copy, removalIndices)
    return [row1 + row2Copy]

# Sets the small row in a bed of 'NA's and puts its elements
# where they're supposed to be.
def floatLeftSmallRow(row2, onColumns, newRowSize):
    canvas = util.dummyList('NA', newRowSize)
    leftIndexes = util.getKeys(onColumns)
    rightIndexes = util.getValues(onColumns)
    return util.multiReplace(canvas, leftIndexes, util.multiGet(row2, rightIndexes))

def fullOuter(table1, table2, onColumns):
    newTable = []
    table1Len = len(table1[0])
    table2Len = len(table2[0])

    # From left side perspective
    for index, row1 in enumerate(table1):
        matchedRow = rowMatchesTable(row1, table2, onColumns)
        if (matchedRow != -1):
            row2 = table2[matchedRow]
            newTable += newRow(row1, row2, onColumns)
            del table2[matchedRow]
        else:
            row1 += util.dummyList('NA', table2Len-len(onColumns))
            newTable += [row1]

    # From right side 
    for index, row2 in enumerate(table2):
        matchedRow = rowMatchesTable(row2, table1, util.flipKeyValues(onColumns))
        if (matchedRow != -1):
            row1 = table1[matchedRow]
            print row1
        else:
            newRowSize = table2Len + table1Len - len(row2)
            row2 = table2[index]
            incompleteRow = floatLeftSmallRow(row2, onColumns, newRowSize)
            newTable += newRow(incompleteRow, row2, onColumns)

    return newTable

if __name__ == '__main__':

    onColumns = {8 : 0, 6 : 1}
    left = [[18.0, 8, 307.0, 130.0, 3504, 12.0, 70, 1, 'chevrolet chevelle malibu'],
    [15.0, 8, 350.0, 165.0, 3693, 11.5, 70, 1, 'buick skylark 320']]

    right = [['plymouth satellite', 70, 2831],
    ['buick skylark', 77, 3865],
    ['chevrolet chevelle malibu', 70, 2881]]
    table = fullOuter(left, right, onColumns)
    util.prettyPrint(table)
