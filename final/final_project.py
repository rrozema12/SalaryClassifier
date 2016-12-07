import csv
import file_system
import clean
import naive_bayes as bayes
import table_utils
import homework_util as homework
import constants
import partition
import output_util as output
import classifier_util
import hw4_util
import knn
import util

def _printConfusionMatrix(labels, name):
    """ Prints a confusion matrix for given labels """
    output.printHeader('Confusion Matrix')
    hw4_util.print_confusion_matrix(labels, name)


def knn_and_naive(table):
    """ Analyzes the table based on Knn and Naive Bayes

    :param table: the table of the titanic dataset
    :return: nothing
    """

    table = table_utils.mapCol(table, constants.INDICES['job-type'],
                               homework.get_job_type)
    table = table_utils.mapCol(table, constants.INDICES['degree'],
                               homework.get_degree)
    table = table_utils.mapCol(table, constants.INDICES['marital-status'],
                               homework.get_marital_status)
    table = table_utils.mapCol(table, constants.INDICES['ethnicity'],
                               homework.get_ethnicity)
    table = table_utils.mapCol(table, constants.INDICES['gender'],
                               homework.get_gender)
    table = table_utils.mapCol(table, constants.INDICES['country'],
                               homework.get_country)
    table = table_utils.mapCol(table, constants.INDICES['salary'],
                               homework.get_salary)

    table = knn.normalize_table(table, [5,7])

    # KNN
    print('\nK_NN\n')

    labels = hw4_util.random_subsample_knn(table, 5, 10, constants.INDICES['salary'])
    accuracy = classifier_util.accuracy(labels)
    print('\tRandom Subsample (5)')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))

    labels = hw4_util.stratified_cross_fold_knn(table, 5, 10, constants.INDICES['salary'])

    accuracy = classifier_util.accuracy(labels)
    print('\tStratified Cross Folds (5)')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))
    _printConfusionMatrix(labels, 'Salary')

    # Naive Bayes
    print('\nNaive Bayes\n')
    test_by_names = ['degree', 'ethnicity', 'gender']

    accuracy = classifier_util.accuracy(
        hw4_util.random_subsample_naive_bayes(table, 10, constants.INDICES['salary'],
                                              test_by_names))

    print('\tRandom Subsample')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))

    labels = hw4_util.stratified_cross_fold_naive_bayes(table, 10, constants.INDICES['salary'],
                                                        test_by_names)
    accuracy = classifier_util.accuracy(labels)

    print('\tStratified CrossFolding')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))
    _printConfusionMatrix(labels, 'Salary')


def main():
    # Data Preprocessing
    newTable = file_system.loadTable("income.csv")
    removedRowsTable = clean.removeNA(newTable)
    incomeDataNoNA = file_system.write(removedRowsTable, "incomeDataNoNA.csv")
    print('\nRows with missing values (NA) have been removed.\n')

    table = file_system.loadTable('incomeDataNoNA.csv')
    knn_and_naive(table)

if __name__ == '__main__':
    main()
