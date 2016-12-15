# analysis.py
# used for data visualization

import util
import collections

# Returns an Ordered Dictionary of frequency
def frequency(col):
    data = collections.OrderedDict()
    col = sorted(col)

    for el in col:
        if util.getFromDict(data, el) == None:
            data[el] = 1
        else:
            data[el] += 1 #Add to the count
    return data

# Sets cutoffs for the frequencies
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
