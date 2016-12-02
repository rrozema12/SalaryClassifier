import math
import util
import collections

# Gets the smallest element in the array of tuples
# and returns the index and value
def _smallest(rowTuples):
    smallest = None
    smallestIndex = None
    for index, tup in enumerate(rowTuples):
        if smallest == None or tup[0] < smallest:
            smallest = tup[0]
            smallestIndex = index
    return smallestIndex, smallest

# Gets the top k rows
def _get_top_k(rowTuples, k):
    tops = []

    for tup in rowTuples:
        # If we haven't filled tops yet, append it
        if len(tops) < k:
            tops.append(tup)
            continue

        smallestIndex, smallest = _smallest(tops)
        if (tup[0] > smallest):
            tops[smallestIndex] = tup

    return tops

def _findWhere(combinedRows, test):
    for index, combined in enumerate(combinedRows):
        distance, row = combined
        if distance == test:
            return combined
    return None

# Picks the most common class label
def _select_class_label(commonRows, labelIndex):
    distances = [combined[0] for combined in commonRows]
    mostCommonCombined = collections.Counter(distances).most_common()
    mostCommon = _findWhere(commonRows, mostCommonCombined[0][0])
    distance, row = mostCommon
    return row[labelIndex]


# Calculate distances
# If the two items are catigorical, it will
# say a distance of 0 if they are the same,
# and a distance of 1 if they are different
def _distance(row, instance, size, labelIndex):
    parts = []
    for i in range(size):
        # Don't include label in sum
        if i == labelIndex:
            continue

        ai = row[i]
        bi = instance[i]
        if isinstance(ai, basestring) or isinstance(bi, basestring):
            part = 0 if ai == bi else 1
            parts.append(pow(part, 2)) # raised to 2 for s's & g's
            continue
        else:
            parts.append(pow((ai - bi), 2))
            continue
    return sum(parts)


def k_nn(training_set, instance, n, k, labelIndex):
    row_distances = []
    for row in training_set:
        d = _distance(row, instance, n, labelIndex)
        row_distances.append((d, row))
    top_k_rows = _get_top_k(row_distances, k)
    label = _select_class_label(top_k_rows, labelIndex)
    return label

if __name__ == "__main__":
    distances = [(2, []), (7, []), (6, []), (3, [])]
    first = [2, 'hi']
    second = [3.5, 'hi']
    print 'dist', _distance(first, second, 2)
