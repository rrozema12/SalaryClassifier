# table_utils.py
# does some checks on the table

def get_domains(table, att_indexes):
    """ Based on a table gets the domains for the given att_indexes

    :param table: a table
    :param att_indexes: list of indexes to get domains for
    :return: a dictionary {att:domain, ...}
    """
    domains = {}
    for index in att_indexes:
        att_vals = list(set(getCol(table, index)))
        domains[index] = att_vals
    return domains


def _validRow(row, where):
    """ Returns True if row matches where

    - where is a 2d array of index, value tuples
        ex: [(0, 'cats'), (1, 230)]
    """
    for index, value in where:
        if row[index] != value:
            return False

    return True

def getWhere(table, where):
    """ Gets rows that match the points defined in "where"
    ex: getWhere(table, [(1, 'dogs'), (0, 20)]))

    - where is a 2d array of index, value tuples
        ex: [(0, 'cats'), (1, 230)]
        note: These are AND'd together.
    """

    newTable = []
    for row in table:
        if _validRow(row, where):
            newTable.append(row)
    return newTable

def getCol(table, index):
    """ Gets a col by an index
    Ignores "NA"
    """
    col = []
    for row in table:
        if (row[index] == 'NA'): continue
        col.append(row[index])
    return col

def mapCol(table, colIndex, function):
    """ Applys the function to every item in the column """
    for row in table:
        row[colIndex] = function(row[colIndex])
    return table

if __name__ == "__main__":
    table = [
    [25, 'cats', 300],
    [50, 'dogs', 3000],
    [75, 'chinchillas', 4000],
    [20, 'horses', 3200],
    [20, 'lizards', 1000],
    [20, 'bloops', 1500],
    [35, 'dogs', 5000],
    [20, 'dogs', 6000]
    ]

    where = [(1, 'dogs'), (0, 20)]
    print("GetWhere", getWhere(table, where))
    print("MapCol", mapCol(table, 2, lambda x: x**2))
