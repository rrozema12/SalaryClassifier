import util

# Gets all col averages
def getColAverages(table):
    rowLength = len(table[0])
    averages = []
    for i in range(rowLength):
        col = util.getCol(table, i)
        if (util.colIsString(col)):
            averages.append('NA')
            continue # We can't replace averages for strings

        avg = util.mean(col)
        averages.append(avg)
    return averages

# Gets col averages where col[colTestIndex] == colTestValue
def getColAveragesBy(table, colTestIndex, colTestValue):
    rowLength = len(table[0])
    averages = []
    for i in range(rowLength):
        col = util.getColBy(table, i, colTestIndex, colTestValue)
        if (util.colIsString(col)):
            averages.append('NA')
            continue # We can't replace averages for strings

        avg = util.mean(col)
        averages.append(avg)
    return averages


# First approach removes all instances with missing values
def removeNA(table):
    newTable = []
    for row in table:
        if not util.hasMissing(row):
            newTable.append(row)
    return newTable


# Second approach computes the average for each missing value
def replaceWithAverages(table):
    averages = getColAverages(table)

    newTable = []
    for row in table:
        newRow = []
        for colIndex, col in enumerate(row):
            if (col == 'NA'):
                col = averages[colIndex]
            newRow.append(col)
        newTable.append(newRow)
    return newTable

# Third approach computers averages based on the year of the car
def replaceWithAveragesRelativeToYear(table):
    yearIndex = 6 #in combined datasets, this is the index

    newTable = []
    for row in table:
        year = row[yearIndex]
        averages = getColAveragesBy(table, yearIndex, year)

        newRow = []
        for colIndex, col in enumerate(row):
            if col == 'NA':
                col = averages[colIndex]
            newRow.append(col)
        newTable.append(newRow)
    return newTable

if __name__ == '__main__':
    table = [[0.0, 0, 0.0, 0.0, 0, 0.0, 70, 0, 'chevrolet impala', 0],
    [3.0, 34, 4344.0, 10.0, 452, 23.0, 40, 5, 'Raww impala', 5023],
    [2.0, 81, 4534.0, 20.0, 454, 93.0, 40, 4, 'ewjiofjieow impala', 4023],
    ['NA', 'NA', 'NA', 'NA', 'NA', 93.0, 40, 'NA', 'no Data', 'NA']]

    print replaceWithAveragesRelativeToYear(table)
