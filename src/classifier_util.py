# classifier_util.py
# used for classification approaches

import util
import numpy
import table_utils

def _split(labels):
    """ Divides up the labels by their actual label
    returns a dictionary of labels
    """
    groups = {}

    for label in labels:
        actual, predicted = label

        try:
            groups[actual].append((actual, predicted))
        except KeyError:
            groups[actual] = [(actual, predicted)]

    return groups

def accuracy(labels):
    """
    Returns multiclass accuracy

    :param labels: list of tuples with [(actual, predicted), ...]
    :return: accuracy
    """
    correct = 0
    all_labels = list(set([labels[i][0] for i in range(len(labels))]))  # set of all the possible labels
    accuracies = [0] * len(all_labels)  # accuracies of each label

    for i in range(len(accuracies)):
        current_label = all_labels[i]
        for label in labels:
            actual, predicted = label
            if actual == current_label and predicted == current_label:
                accuracies[i] += 1  # true positives
            elif actual != current_label and predicted != current_label:
                accuracies[i] += 1  # true negatives

    length = len(labels)
    # Does the mean of all the (TP + TN) / (All labels)
    return numpy.mean([float(an_accuracy) / float(length) for an_accuracy in accuracies])


def _findFalses(splitLabels, forLabel):
    """ Takes an array of labels, counts the number of FP and FN """

    falses = 0
    for row in splitLabels:
        for actual, predicted in row:

            # If either the predicted or actual is the label we care about
            if actual == forLabel:
                if actual != predicted: #if label is false
                    falses += 1
            elif predicted == forLabel:
                if actual != predicted:
                    falses += 1
    return falses
