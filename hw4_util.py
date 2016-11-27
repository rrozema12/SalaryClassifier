from tabulate import tabulate
import homework_util as homework
import naive_bayes as bayes
import util
import table_utils
import partition
import knn

def random_subsample_naive_bayes(table, k, class_index, test_by_names, contIndices=[]):
    """ Uses Naive Bayes and Random Subsampling to find labels """
    return _random_subsample(table, k, predict_labels, class_index, test_by_names, contIndices)


def random_subsample_knn(table, num_holdout, k, class_index):
    """ Uses knn and random subsampling to predict labels

    :param table: a table of data
    :param num_holdout: the number of random subsamples to run
    :param k: the number of nearest nieghbors
    :param class_index: the index where the class label is
    :return: eturns a list of tuples of the labels in the form [(actual, predicted),...]
    """
    labels = []

    # repeats the subsampling k times
    for i in range(num_holdout):
        test_set, training_set = partition.holdout(table)

        # gets the lables
        labels.extend(knn.knn(training_set, test_set, k, class_index))
    return labels

def stratified_cross_fold_knn(table, num_folds, k, class_index):
    """ Uses knn and stratified cross folding to predict labels

    :param table: a table of data
    :param num_folds: the number of folds to calculate
    :param k: the number of nearest nieghbors
    :param class_index: the index where the class label is
    :return: returns a list of tuples of the labels in the form [(actual, predicted),...]
    """
    labels = []
    folds = strat_folds(table, class_index, num_folds)
    for index in range(len(folds)):
        test = folds[index]  # creates the test from one fold
        training = []

        # meshes the rest of the folds together to make the training set
        for training_index in range(len(folds)):
            if training_index != index:
                training.extend(folds[training_index])

        labels.extend(knn.knn(training, test, k, class_index))
    return labels

def _random_subsample(table, k, classify, class_index, test_by_names, contIndices=[]):
    """
    Uses random subsampling to test labels on classify
    :param table: Table of data
    :param k: Number of times to run holdout method
    :return: labels in format list of tuples [(actual, predicted),...]
    """
    labels = []

    # repeats the subsampling k times
    for i in range(k):
        test_set, training_set = partition.holdout(table)

        # gets the lables
        labels.extend(classify(training_set, test_set, class_index, test_by_names, contIndices))
    return labels


def predict_labels(training, test, class_index, test_by_names, contIndices=[]):
    """ Using Naive Bayes it will predict values in test by using training

    :param training: A table of data
    :param test: A table of data in the same format as training
    :return: labels in format list of tuples [(actual, predicted),...]
    """
    labels = []
    for instance in test:
        actual = instance[class_index]  # the actual label of the instance

        # change the instance to the values we are testing from
        instance = homework.getNamedTuples(instance, test_by_names)

        # gets the predicted label
        predicted, probability = bayes.predict_label(training,
            instance, class_index, contIndices)

        # records the two labels
        labels.append((actual, predicted))
    return labels


def stratified_cross_fold_naive_bayes(table, k, class_index, test_by_names, contIndices=[]):
    """ Runs naive bayes on k stratified cross folds """
    return _stratified_cross_fold(table, k, predict_labels, class_index, test_by_names, contIndices)


def _stratified_cross_fold(table, k, classify, class_index, test_by_names, contIndices=[]):
    """
    Uses stratified crossfolding to create the training and test sets
    :param table: Table of data
    :param k: Number of folds
    :return: labels in format list of tuples [(actual, predicted),...]
    """
    labels = []
    folds = strat_folds(table, class_index, k)
    for index in range(len(folds)):
        test = folds[index]  # creates the test from one fold
        training = []

        # meshes the rest of the folds together to make the training set
        for training_index in range(len(folds)):
            if training_index != index:
                training.extend(folds[training_index])

        labels.extend(classify(training, test, class_index, test_by_names, contIndices))
    return labels


def strat_folds(table, by_label_index, k):
    """
    Creates fold where each fold has the same distrubution of class labels as the origonal table

    :param table: table of data
    :param by_label_index: the class label index
    :param k: the number of partitions to create
    :return: a list of tables where each table is a folds, i.e.: [[P1],[P2],..., [Pnum]] where each P is a table
    """
    labels_to_rows = {}

    # spreads the data out into a dictionary where the key is the class label and the data is a table consisting of
    # rows with that class label {class_label:rows_with_class_label
    for row in table:
        label = row[by_label_index]
        try:
            labels_to_rows[label].append(row)
        except KeyError:
            labels_to_rows[label] = [row]

    # creates folds by evenly distributing the rows of each class label to the number of partitions
    folds = {}
    index = 0
    for key, table in labels_to_rows.iteritems():
        for row in table:
            try:
                folds[index].append(row)
            except KeyError:
                folds[index] = [row]
            index += 1
            if index > k:
                index = 0
    return util.dictionaryToArray(folds)


def print_confusion_matrix(labels, class_label_name):
    """ Prints the confusion matrix of the given labels

    :param labels: A list of tuples of class labels [(actual, predicted),...]
    :param class_label_name: The name of the class label
    """
    class_labels = list(set(table_utils.getCol(labels, 0)))  # all the actual class labels
    the_headers = [class_label_name]
    the_headers.extend(class_labels)
    the_headers.extend(['Total', 'Recognition (%)'])

    # makes an table filled with zeros of #columns = len(the_headers) and #rows = len(class_labels)
    confusion_matrix = [[0] * len(the_headers) for i in range(len(class_labels))]

    # fills out the confusion matrix with the predicted vs. actual
    for a_label_point in labels:
        actual, predicted = a_label_point
        confusion_matrix[class_labels.index(actual)][the_headers.index(predicted)] += 1

    # add the rest of the values to the confusion matrix
    for i in range(len(confusion_matrix)):
        row = confusion_matrix[i]  # current row

        # adding total to the confusion matrix
        total = sum(row)
        row[the_headers.index('Total')] = total  # add the total in for the row

        row[0]= class_labels[i]  # adds the class label for the row to the beginning of row

        # adding recognition to the confusion matrix (% of guesses in row that are correct
        recognition = row[the_headers.index(class_labels[i])] # TP
        recognition /= float(total)
        recognition *= 100
        row[the_headers.index('Recognition (%)')] = recognition

    # prints the table
    print tabulate(confusion_matrix, headers = the_headers, tablefmt="rst")
