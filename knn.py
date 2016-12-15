# knn.py
# does knn calculations

import table_utils
import numpy
from random import randint


def _get_top_k(row_distances, k):
    """ Gets the top k tuples with the smallest distance by
    continually trying to replace the tuple with the highest distance
    with a tuple with lower distance

    :param row_distances: a list in the form of [(dist, row),...]
    :param k: the number of top rows to pick
    :return: Returns the top k tuples with the smallest distance
    """
    smallest_tuples = []

    for tup in row_distances:
        if len(smallest_tuples) < k:
            smallest_tuples.append(tup)
            continue
        largest_index, largest = _largest(smallest_tuples)
        if tup[0] < largest[0]:
            smallest_tuples[largest_index] = tup
        elif tup[0] == largest[0] and randint(1,2) == 1:  # randomly select to tie break
            smallest_tuples[largest_index] = tup
    return smallest_tuples


def _largest(smallest_tuples):
    """ Finds the tuple with the largest distance and
    The index that it is located

    :param smallest_tuples: a list in the form of [(dist, row),...]
    :return: the index of the tuple with the highest distance and the tuple
    """
    index = None
    large_tuple = None
    for the_index in range(len(smallest_tuples)):
        if index == None or large_tuple[0] < smallest_tuples[the_index][0]:
            index = the_index
            large_tuple = smallest_tuples[the_index]
    return index, large_tuple


def _select_class_label(top_k_rows, label_index):
    """ Gets the class label based on majority voting

    :param top_k_rows: a list in the form of [(dist, row),...]
    :param label_index: the index in the rows where the label is located
    :return: the most common label
    """
    labels = []
    for tuple in top_k_rows:
        dist, row = tuple
        labels.append(row[label_index])
    return max(set(labels), key=labels.count)  #calculates mode of the instances


def _distance(row, instance, labelIndex):
    """ Calculates euclidean distance
    If the two items are catigorical, it will
    say a distance of 0 if they are the same,
    and a distance of 1 if they are different

    :param row: a row from a dataset
    :param instance: a row from the dataset to compare distance to
    :param labelIndex: the index
    :return: the distance between the row and distance
    """
    parts = []
    for i in range(len(instance)):
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
    return numpy.sqrt(float(sum(parts)))


def get_label_k_nn(training_set, instance, k, label_index):
    """ Calculates a label using K_nn

    :param training_set: a table of data
    :param instance: an instance to be fitted to the training_set
    :param k: the number of nearest neighbors
    :param label_index: the index where the class label is located
    :return: the class label prediction
    """
    row_distances = []
    for row in training_set:
        d = _distance(row, instance, label_index)
        row_distances.append((d, row))
    top_k_rows = _get_top_k(row_distances, k)
    label = _select_class_label(top_k_rows, label_index)
    return label

def knn(training, test, k, class_index):
    """ Predicts the labels in test set based on knn

    :param training: a training table
    :param test: a test table
    :param k: number of nearest neighbors
    :param class_index: the index where the label is
    :return: a lis of tuples depicting the actual class label and the predicted one
    """

    labels = []
    for instance in test:
        actual = instance[class_index]
        predicted = get_label_k_nn(training, instance,  k, class_index)
        labels.append((actual,predicted))
    return labels


def normalized_value(xs):
    """ normalizes a list of numbers

    :param xs: a list of numbers
    :return: a normalized list
    """
    minval = min(xs)
    maxval = max(xs)
    minmax = (maxval-minval) * 1.0
    return [(x - minval) / minmax for x in xs]


def normalize_table(table, except_for=None):
    """ Assumes table has been cleaned of all NA values

    :param table: a data_table
    :param except_for: a list of indexes to not normalize in the table
    :return: A normalized table
    """
    new_table = [[] for i in range(len(table))]

    indexes = range(len(table[0]))  # number of indexes in a row

    for index in indexes:
        data_column = table_utils.getCol(table, index)
        if index not in except_for:
            data_column = normalized_value(data_column)  # normalize data in column

        # puts the values of the data column into the new_table
        for row_index in range(len(table)):
            new_table[row_index].append(data_column[row_index])

    return new_table
