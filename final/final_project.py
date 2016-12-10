import csv
import file_system
import clean
import naive_bayes as bayes
import table_utils
import homework_util as homework
import constants
import analysis
import diagram
from constants import INDICES, INCOME
import partition
from partition import holdout
import output_util as output
import classifier_util
import hw4_util
import knn
import util
import decision_tree
from decision_tree import classify
from random_forest import run_a_table
from util import these, flipKeyValues
from functools import partial
from classifier_util import accuracy
import numpy


def _printConfusionMatrix(labels, name):
    """ Prints a confusion matrix for given labels """
    output.printHeader('Confusion Matrix')
    hw4_util.print_confusion_matrix(labels, name)

def data_vis():

    table = file_system.loadTable('incomeDataNoNA.csv')

    col = util.getCol(table, INDICES['ethnicity'])
    freqDict = analysis.frequency(col)
    diagram.frequency(freqDict, 'ethnicity', 'Frequency-Ethnicity')
    diagram.pie(freqDict, 'ethnicity', 'Pie-Ethnicity')

    col = util.getCol(table, INDICES['marital-status'])
    freqDict = analysis.frequency(col)
    diagram.frequency(freqDict, 'marital-status', 'Frequency-Marital-Status')
    diagram.pie(freqDict, 'marital-status', 'Marital-Status')

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

def decisiontree(table):
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


    output.printHeader('Decision Tree')

    attributes = these(INDICES, 'degree', 'ethnicity', 'gender')
    domains = table_utils.get_domains(table, attributes)
    tree = decision_tree.tdidt(table, attributes, domains, INDICES['salary'])

    decision_tree.print_rules(tree, ['age', 'job-type', 'degree', 'marital-status',
                    'ethnicity', 'gender', 'country', 'salary'],
                              'salary')

    attributes = these(INDICES, 'degree', 'ethnicity', 'gender')

    # Creates a myClassifier function that's paritally filled out
    # From decision_tree.classify
    # Essentially a new function:
    # myClassifier(training, test, class_index)
    myClassifier = partial(decision_tree.classify, att_indexes=attributes, att_domains=domains)

    labels = homework.stratified_cross_fold(table, 10, INDICES['salary'],
       myClassifier)

    acc = accuracy(labels)
    print('\n')
    print('Stratified CrossFolding')
    print('\tAccuracy = ' + str(acc) + ', error rate = ' + str(1 - acc))
    print('\n')

    # Confusion Matrix
    _printConfusionMatrix(labels, 'Salary')

def randomforest(table, n, m, f):

    output.printHeader('Random Forest')
    print("N = " + str(n) + " M = " + str(m) + " F = " + str(f))
    indexes = [INDICES['degree'], INDICES['ethnicity'], INDICES['gender']]
    domains = table_utils.get_domains(table, indexes)
    forest_labels, train, test = \
                run_a_table(table, indexes,
                    INDICES['salary'], n, m, f)
    forest_accuray = accuracy(forest_labels)

    print('\tAccuracy = ' + str(forest_accuray))
    _printConfusionMatrix(forest_labels, 'Salary')


def main():
    # Data Preprocessing
    newTable = file_system.loadTable("income.csv")
    removedRowsTable = clean.removeNA(newTable)
    incomeDataNoNA = file_system.write(removedRowsTable, "incomeDataNoNA.csv")
    print('\nRows with missing values (NA) have been removed.\n')

    data_vis()

    table = file_system.loadTable('incomeDataNoNA.csv')
    knn_and_naive(table)

    table = file_system.loadTable('incomeDataNoNA.csv')
    decisiontree(table)

    table = file_system.loadTable('incomeDataNoNA.csv')
    randomforest(table, 6000, 215, 2)

if __name__ == '__main__':
    main()
