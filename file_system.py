import csv
import util

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
        writer = csv.writer(csvfile , skipinitialspace=False, delimiter=',')
        for row in table:
            writer.writerow(row)
