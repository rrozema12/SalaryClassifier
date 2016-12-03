import csv
import util

def findDuplicates(row, table, keyValues):
    """ Super terrible way to check duplicates
    returns - item rows if duplicates exist
    returns - empty array if no duplicate
    """
    duplicates = []
    for testRow in table:

        # calculate matches
        matches = None
        for key in keyValues:
            test = (row[key] == testRow[key])
            if (matches == None):
                matches = test
                continue
            else:
                matches = matches and test

            if (not(matches)): break

        # If matches, append the row to duplicates
        if matches:
            duplicates.append(row)
            duplicates.append(testRow)
    return duplicates

# Load a table from a file with no fuss
def loadTable(filename):
    the_file = open(filename, 'r')
    the_reader = csv.reader(the_file, dialect='excel')
    table = []
    for row in the_reader:
        if len(row) > 0:
            table.append(util.listToCorrectType(row))
    the_file.close()
    return table

def write(table, filename):
    with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        for row in table:
            writer.writerow(row)

def loadFile(filename, matches):
    """ Loads a csv file

    filename - just the name of the file
    returns - an object with all the table information in it
    """
    the_file = open(filename, 'r')
    the_reader = csv.reader(the_file, dialect='excel')
    table = []
    count = 0
    duplicates = []
    for row in the_reader:
        if len(row) > 0:
            count += 1
            duplicate = findDuplicates(row,table, matches)
            if (len(duplicate) > 0):
                duplicates.append(duplicate)
            table.append(row)
    the_file.close()
    return {'table' : table, 'name' : filename, 'count' : count,
        'duplicates' : duplicates}
