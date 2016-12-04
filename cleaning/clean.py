def removeNA(table):
    newTable = []
    for row in table:
        if not hasMissing(row):
            newTable.append(row)
    return newTable

def hasMissing(array):
    for el in array:
        if (el == ' NA'):
            return True
    return False

def removeSpaces(table):
    newTable = []
    with open(table, 'wb') as csvfile:
        writer = csv.writer(csvfile , skipinitialspace = False, delimiter=',',quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        for row in table:
            writer.writerow(row)
        return newTable
