import util
import collections

# Returns an OrderedDict of frequency
#
def frequency(col):
    data = collections.OrderedDict()
    col = sorted(col)

    for el in col:
        if util.getFromDict(data, el) == None:
            data[el] = 1
        else:
            data[el] += 1 #Add to the count
    return data

def valsByMPG(table, index, comparedIndex):
    vals = []

    for row in table:
        x = row[index]
        y = row[comparedIndex]
        vals.append([x,y])
    return vals

def frequencies_for_cutoffs(col, cutoffs):
    # Sets each frequency to 0 by default
    freqs = [0] * len(cutoffs)

    for el in col:
        for i in range(len(cutoffs)):
            if el <= cutoffs[i]:
                freqs[i] += 1
                break
    return freqs

def points(table, x_index, y_index):
    vals = []
    for row in table:
        x = row[x_index]
        y = row[y_index]
        if x == 'NA' or y == 'NA':
            continue
        vals.append([x,y])
    return vals

def groupBy(table, att_index):
    grouping_values = list(set(getCol(table, att_index)))

    for val in grouping_values:
        result.append([])

    for row in table:
        result[grouping_values.index(row[att_index])].append(row[i])

    return results;

if __name__ == '__main__':
    col = [23, 23, 24, 24, 24, 25, 28, 29, 40, 40]
    print frequency(col)
