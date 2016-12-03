import util

attributeNames = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'year', 'origin', 'name', 'msrp']

def arrayWithLineEnds(array):
    string = ""
    for row in array:
        string += str(row) + "\n"
    return string

def printHeader():
    print "Summary Stats:"
    print "=============  =======  =======  =======  =======  ========"
    print "attribute      min      max      mid      avg      med"
    print "=============  =======  =======  =======  =======  ========"

def printSummaryRow(attribute, min_, max_, mid, avg, med):
    print attribute.ljust(13), '', str(min_).ljust(7), '', str(max_).ljust(7), '', str(mid).ljust(7), '', str(avg).ljust(7), '', str(med).ljust(9)

def summary(table):
    printHeader()
    for index, attribute in enumerate(attributeNames):
        calcAttribute(table, index)

def calcAttribute(table, attributeIndex):

    isNA = table[0][attributeIndex] == 'NA'
    isString = isinstance(table[0][attributeIndex], basestring)
    if (isString and not(isNA)):
        return

    _min = None
    _max = None
    mid  = None
    for row in table:

        # Skip NA values
        isNA = row[attributeIndex] == "NA"
        if isNA:
            continue

        # min
        if (_min == None or _min > row[attributeIndex]):
            _min = row[attributeIndex]

        # max
        if (_max == None or _max < row[attributeIndex]):
            _max = row[attributeIndex]

    col = util.getCol(table, attributeIndex)
    med = round(util.median(col), 2)
    mid = round((_max - _min)/2, 2)
    avg = round(util.mean(col), 2)

    printSummaryRow(attributeNames[attributeIndex], _min, _max, mid, avg, med)

if __name__ == '__main__':
    table = [[3.0, 8, 454.0, 220.0, 4354, 9.0, 70, 1, 'chevrolet impala', 3132],
    [2.0, 81, 4534.0, 20.0, 454, 93.0, 40, 4, 'ewjiofjieow impala', 4023]]
    summary(table)
