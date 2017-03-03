# random_forest.py
# does the random forest calcutlaions

import decision_tree
import partition
import heapq
import table_utils
import classifier_util
from homework_util import strat_folds


def run_a_table(table, indexes, class_index, N, M, F):
    """ Takes a table, splits it into a training and test set. Creates a
    random forest for the training set. Then tests the forest off of
    the test set

    :param table: a table of values
    :param indexes: The indexes to partition on
    :param class_index: The index of the label to predict
    :param N: Number of trees to produce
    :param M: Number of the best trees to choose
    :param F: Subset size of random attributes
    :return: Returns a list of tuples. Of the actual, predicted label and
            training and test
             [(actual1,predicted1), (actual2,predicted2), ...], training, test
    """
    domains = table_utils.get_domains(table, indexes)
    folds = strat_folds(table, class_index, 3)
    training = folds[0]
    training.extend(folds[1])
    test = folds[2]
    forest = _random_forest(test, indexes, class_index, domains, N, M, F)

    return [(row[class_index], predict_label(forest, row)) for row in test], \
           training, test


def _random_forest(table, indexes, class_index, att_domains, N, M, F):
    """ Generates a random forest classifier for a given table

    :param table: a table
    :param indexes: a list of indexes to partition on
    :param class_index: the index of the class label to predict
    :param N: Number of trees to produce
    :param M: Number of the best trees to choose
    :param F: Subset size of random attributes
    :return: A list of lists. Trees and thier accuracies
            [(accuracy1, tree1), ... , (accuracyM, treeM)]
    """

    # We store the accuracies and trees in a priority queue
    # lower numbers = higher priority
    priority_queue = [] # see: https://docs.python.org/3/library/heapq.html#basic-examples
    attributes = indexes

    # Uses a training and remainder set from bootsraping to create each tree
    bags = partition.bagging(table, N)
    for bag_set in bags:
        tree = decision_tree.tdidt_RF(bag_set[0], attributes, att_domains, class_index, F)
        acc = _accuracy_for_tree(tree,class_index, bag_set[1])
        heapq.heappush(priority_queue, (acc, tree))
        #push to the priorityQueue

    # Since our priority queue is backwards (and I dunno how to reverse that)
    # we pop off all the ones we don't need. N - M
    for i in range(N - M):
        heapq.heappop(priority_queue)

    # Now our priority queue will be our list that we can return
    return priority_queue


def _accuracy_for_tree(tree, class_index, test_set):
    labels = decision_tree.classify_with_tree(tree, class_index, test_set)
    return classifier_util.accuracy(labels)


def predict_label(forest, instance):
    """ predicts the label of an instance given a forest using weighted
        voting with accuracies

    :param forest: a list of lists in te form returned by random_forest()
    :param instance: an row to have a class label predicted
    :return: a class label
    """
    labels = {}
    for acc_and_tree in forest:
        prediction = decision_tree.get_label(acc_and_tree[1], instance)
        # totals the accuracy predicted for each label
        try:
            labels[prediction] += acc_and_tree[0]
        except KeyError:
            labels[prediction] = acc_and_tree[0]

    # gets the label with the highest predicted value
    highest_value = 0
    highest_label = 0
    for current_label, value in labels.items():
        if value > highest_value:
            highest_label = current_label

    return highest_label
