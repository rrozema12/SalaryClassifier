# final_project.py
# does all of the work

import csv
import file_system
import clean
import naive_bayes as bayes
import table_utils
import partition_util as homework
import constants
import analysis
import diagram
from constants import INDICES, INCOME
import partition
from partition import holdout
import output_util as output
import classifier_util
import partition_util
import knn
import util
import decision_tree
from decision_tree import classify
from random_forest import run_a_table
from util import these, flipKeyValues
from functools import partial
from classifier_util import accuracy
import numpy

accuracy_values = []

"""
 Function that discretizes the table to make it usable for the
 classification functions and classifiers

 Parameter: income dataset
 Return: nothing
"""
def map_columns_table(table):
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

"""
 Helper function to print the confusion matrix

 Parameters: labels: the labels for the conusion matrix
             name: the name to be displayed for the labels
 Return: a formatted confusion matrix
"""
def _printConfusionMatrix(labels, name):
    """ Prints a confusion matrix for given labels """
    output.printHeader('Confusion Matrix')
    partition_util.print_confusion_matrix(labels, name)

"""
 Function that does all of the data visualization. In the case of this
 project, freqency diagrams and pie charts are used to displat how
 many times and how often a particular column appears in the table.

 Parameters: None
 Return: matplotlib graphs of selected columns of the dataset.
"""
def data_vis():
    table = file_system.loadTable('../datasets/incomeNoNA.csv')

    col = util.getCol(table, INDICES['degree'])
    freqDict = analysis.frequency(col)
    diagram.pie(freqDict, 'Degree', 'Pie-Degree')

    col = util.getCol(table, INDICES['ethnicity'])
    freqDict = analysis.frequency(col)
    diagram.pie(freqDict, 'Ethnicity', 'Pie-Ethnicity')

    col = util.getCol(table, INDICES['marital-status'])
    freqDict = analysis.frequency(col)
    diagram.pie(freqDict, 'Marital Status', 'Marital-Status')

    col = util.getCol(table, INDICES['gender'])
    freqDict = analysis.frequency(col)
    diagram.pie(freqDict, 'Gender', 'Gender')

    col = util.getCol(table, INDICES['age'])
    freqDict = analysis.frequency(col)
    diagram.dot(freqDict, 'Age', 'Dot-Age')

    table = table_utils.mapCol(table, constants.INDICES['degree'],
                               homework.get_degree)
    table = table_utils.mapCol(table, constants.INDICES['marital-status'],
                               homework.get_marital_status)
    table = table_utils.mapCol(table, constants.INDICES['ethnicity'],
                               homework.get_ethnicity)
    table = table_utils.mapCol(table, constants.INDICES['salary'],
                               homework.get_salary_continuous)
    table = table_utils.mapCol(table, constants.INDICES['gender'],
                               homework.get_gender)

    col = util.getCol(table, INDICES['degree'])
    freqDict = analysis.frequency(col)
    diagram.frequency(freqDict, 'Degree', 'Frequency-Degree')

    col = util.getCol(table, INDICES['marital-status'])
    freqDict = analysis.frequency(col)
    diagram.frequency(freqDict, 'Marital Status', 'Frequency-Marital-Status')

"""
 Function that does all of the calculations, accuracies, and confusion
 matrices for both KNN and Naive Bayes.

 Parameters: income dataset
 Return: accuracies and confusion matrices for KNN and Naive Bayses classifiers.
"""
def knn_and_naive(table):
    """ Analyzes the table based on Knn and Naive Bayes

    :param table: the table of the titanic dataset
    :return: nothing
    """
    map_columns_table(table)
    table = knn.normalize_table(table, [5,7])

    # KNN
    output.printHeader('K-Nearest Neighbors')

    labels = partition_util.random_subsample_knn(table, 5, 10, constants.INDICES['salary'])
    accuracy = classifier_util.accuracy(labels)
    print('\tRandom Subsample')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))

    labels = partition_util.stratified_cross_fold_knn(table, 5, 10, constants.INDICES['salary'])

    accuracy = classifier_util.accuracy(labels)
    accuracy_values.append(accuracy)
    print('\tStratified Cross Folds (5)')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))

    _printConfusionMatrix(labels, 'Salary')

    # Naive Bayes
    output.printHeader('Naive Bayes')
    test_by_names = ['degree', 'ethnicity', 'gender']

    accuracy = classifier_util.accuracy(
        partition_util.random_subsample_naive_bayes(table, 10, constants.INDICES['salary'],
                                              test_by_names))

    print('\tRandom Subsample')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))

    labels = partition_util.stratified_cross_fold_naive_bayes(table, 10, constants.INDICES['salary'],
                                                        test_by_names)
    accuracy = classifier_util.accuracy(labels)
    accuracy_values.append(accuracy)
    print('\tStratified CrossFolding')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))
    _printConfusionMatrix(labels, 'Salary')

"""
 Function that does all of the decision tree calculations and confusion matrix
 for Decision Trees

 Parameters: income dataset
 Return: accuracies and confusion matrices for the decision tree classifier.
"""
def decisiontree(table):
    map_columns_table(table)

    output.printHeader('Decision Tree')

    attributes = these(INDICES, 'ethnicity', 'degree', 'gender')
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
    accuracy_values.append(acc)
    print('\n')
    print('Stratified CrossFolding')
    print('\tAccuracy = ' + str(acc) + ', error rate = ' + str(1 - acc))
    print('\n')

    # Confusion Matrix
    _printConfusionMatrix(labels, 'Salary')

"""
 Function that does all of the decision tree calculations and confusion matrix
 for Random Forests

 Parameters: dataset
             number of trees to be generated
             number of trees to uses
             number of elements in random subsets
 Return: accuracies and confusion matrices for the random forests classifier.
"""
def randomforest(table, n, m, f):
    output.printHeader('Random Forest')
    print("N = " + str(n) + " M = " + str(m) + " F = " + str(f))
    indexes = [INDICES['degree'], INDICES['ethnicity'], INDICES['gender']]
    domains = table_utils.get_domains(table, indexes)
    forest_labels, train, test = \
                run_a_table(table, indexes,
                    INDICES['salary'], n, m, f)
    forest_accurcay = accuracy(forest_labels)

    print('\tAccuracy = ' + str(forest_accurcay))
    _printConfusionMatrix(forest_labels, 'Salary')


def main():
    # Data preprocessing
    newTable = file_system.loadTable("../datasets/income.csv")
    removedRowsTable = clean.removeNA(newTable)
    incomeDataFullNoNA = file_system.write(removedRowsTable, "../datasets/incomeNoNA.csv")
    output.printHeader('Rows with NAs have been removed.')

    # Data visualization
    data_vis()
    output.printHeader('Data visualization complete.')

    # KNN and Naive Bayes classifiers
    table = file_system.loadTable('../datasets/incomeNoNA.csv')
    knn_and_naive(table)

    # Decision Tree classifier
    table = file_system.loadTable('../datasets/incomeNoNA.csv')
    decisiontree(table)

    # Random Forest classifier
    table = file_system.loadTable('../datasets/incomeNoNA.csv')
    randomforest(table, 3000, 215, 2) #N, M, and F vals

if __name__ == '__main__':
    main()
