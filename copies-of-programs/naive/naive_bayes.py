import table_utils
import math_utils as math

def _applyGaussian(table, indices):
    for index in indices:
        col = table_utils.getCol(table, index)
        applyGaussian = math.get_gaussian_application(col)
        table = table_utils.mapCol(table, index, applyGaussian)
    return table

def _probabilityOfXGivenH(table, x, h):
    """ Calculates P(X|H)
    - x is a tuple of (index, value)
    - h is a tuple of (index, value)
    """

    # Get table given H
    tableOfH = table_utils.getWhere(table, [h])

    # Get all the X instances where H
    tableOfXGivenH = table_utils.getWhere(tableOfH, [x])

    return (1.0 * len(tableOfXGivenH))/ (1.0 * len(tableOfH))

def _totalCases(table, label):
    """ Returns the total number of cases
    in the table where table[attrIndex]
    equals 'test'

    - label is a tuple of (index, value)
    """

    filteredTable = table_utils.getWhere(table, [label])
    return len(filteredTable)

def _priorProbability(table, label):
    """ Calculates P(X)
    where X is attribute at table[attrIndex] that
    equals 'test'

    - label is a tuple of (index, value)
    """

    total = len(table)
    count = _totalCases(table, label)
    return count*1.0/total*1.0

def probability(table, instance, label, contIndices = []):
    """ Calculates P(H|X) or Bayes Theorem
    - instance is an array of tuples [(index, value), (index2, value2), ...]
    - label is a tuple (index, value)
    """
    prior = _priorProbability(table, label)
    probabilities = [prior]

    for attribute in instance:
        index, value = attribute

        # Calculate probablity based on cont or cat
        prob = None
        if index in contIndices:
            temp_table = table_utils.getWhere(table, [label])
            col = table_utils.getCol(temp_table, index)
            prob = math.gaussian_probability(value, col)
        else:
            prob = _probabilityOfXGivenH(table, attribute, label)

        probabilities.append(prob)

    return math.prod(probabilities)

def predict_label(training, instance, label_index, contIndices=[]):
    """ Predicts a label for the instance based on the training set
    - instance is an array of tuples [(index, value), (index2, value2), ...]
    - labelIndex is the column where the label is

    Returns the label and it's probability
    """
    all_labels = set(table_utils.getCol(training, label_index))
    most_likely_label = None
    most_likely_probability = None
    for label_value in all_labels:
        label = (label_index, label_value)
        prob = probability(training, instance, label, contIndices)

        # If this label is more likely, let's return it
        if most_likely_probability == None or prob > most_likely_probability:
            most_likely_probability = prob
            most_likely_label = label_value

    return most_likely_label, most_likely_probability
