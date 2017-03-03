# clean.py
# used to clean the dataset

# Removes any rows that have a missing value
def removeNA(table):
    newTable = []
    for row in table:
        if not hasMissing(row):
            newTable.append(row)
    return newTable

# Finds out if the row has a missing value
def hasMissing(array):
    for el in array:
        if (el == 'NA'):
            return True
    return False

# Removes the spces after the comments
def removeSpaces(table):
    newTable = []
    with open(table, 'wb') as csvfile:
        writer = csv.writer(csvfile , skipinitialspace = False, delimiter=',')
        for row in table:
            writer.writerow(row)
        return newTable
