import csv
import file_system
import util
import copy
import summary
import join
import clean

# Here to keep consistent breaks
LINE_BREAK = '----------------'

# Makes an array pretty printable
def arrayWithLineEnds(array):
    string = ""
    for row in array:
        string += str(row) + "\n"
    return string

# Prints out a file with duplicates and counts
def printFile(filename, matches, header):
    """ Prints out those header files in Step 2"""
    fileObj = file_system.loadFile(filename, matches)
    print LINE_BREAK
    print header
    print LINE_BREAK
    print 'No. of instances: ',  str(fileObj['count'])
    duplicates = arrayWithLineEnds(fileObj['duplicates'])
    if not duplicates.strip(): duplicates = '[]'
    print 'Duplicates:', duplicates

# Prints out a header
def printHeader(text):
    print LINE_BREAK
    print text
    print LINE_BREAK

# Creates combined column
def setup():
    # Left side is auto-mpg col index
    # Right side is auto-prices col index
    onColumns = {8 : 0, 6 : 1}

    # Join the clean data
    mpgTable = file_system.loadTable('auto-mpg-clean.csv')
    pricesTable = file_system.loadTable('auto-prices-clean.csv')
    combinedTable = join.fullOuter(mpgTable, pricesTable, onColumns)

    file_system.write(combinedTable, 'auto-data.csv')

def main():
    setup()

    printFile('auto-mpg-nodups.csv', [8, 6], 'auto-mpg-nodups.csv')
    print ''
    printFile('auto-prices-nodups.csv', [0, 1], 'auto-prices-nodups.csv')
    print ''
    printFile('auto-mpg-clean.csv', [8, 6], 'auto-mpg-clean.csv')
    print ''
    printFile('auto-prices-clean.csv', [0, 1], 'auto-prices-clean.csv')
    print ''
    printFile('auto-data.csv', [8, 6], 'Combined table (saved as auto-data.csv)')
    print ''

    # Cleaned Combined data
    cleaned = file_system.loadFile('auto-data.csv', [8, 6])['table']
    cleaned = util.tableToCorrectType(cleaned)
    summary.summary(cleaned)

    # Combined table with rows missing
    removedRowsTable = clean.removeNA(cleaned)
    printHeader('Combined table (rows w/ missing values removed):')
    summary.summary(removedRowsTable)

    # Combined tables with average values
    averageRowsTable = clean.replaceWithAverages(cleaned)
    printHeader('Combined table (rows w/ average values):')
    summary.summary(averageRowsTable)

    # Combined Table with average values by row
    averageByYearTable = clean.replaceWithAveragesRelativeToYear(cleaned)
    printHeader('Combined table (rows w/ average values as year):')
    summary.summary(averageByYearTable)

if __name__ == '__main__':
    main()
