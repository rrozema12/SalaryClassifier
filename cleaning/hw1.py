import csv
import file_system
import clean

# Here to keep consistent breaks
LINE_BREAK = '-------------------------------------------------'

# Makes an array pretty printable
def arrayWithLineEnds(array):
    string = ""
    for row in array:
        string += str(row) + "\n"
    return string

# Prints out a header
def printHeader(text):
    print '\n'
    print LINE_BREAK
    print text
    print LINE_BREAK
    print '\n'

def main():
    newTable = file_system.loadTable("income.csv")

    #for row in newTable:
    #    print row

    removedRowsTable = clean.removeNA(newTable)
    #]for row in removedRowsTable:
    #    print row

    incomeDataNoNA = file_system.write(removedRowsTable, "incomeDataNoNA.csv")


    printHeader('Rows with missing values (NA) have been removed.')

if __name__ == '__main__':
    main()
