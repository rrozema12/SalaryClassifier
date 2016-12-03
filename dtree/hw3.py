import file_system
import constants
import math_utils
import numpy
import hw3_utils as hw3
import dataOperations as dataOp
import classifiers
import util
import csv
import random
import math
import tabulate

# Step 1
#
# Build a linear regression from
# weight to MPG points,
# then use that to predict the mpg
def linearRegressionClassifier(table):

    # Create a list of 2d points with weight and mpg
    points = hw3.getPoints(table, 'weight', 'mpg')

    # Make the linear regression funtion to get MPG
    getMPG = math_utils.linear_regression(points)

    # Get 5 random instances
    instances = hw3.getInstances(table, 5)

    for instance in instances:
        hw3.printInstance(instance)
        classValue  = getMPG(hw3.get(instance, 'weight'))
        classValue  = dataOp.getDeptEnergyRating(classValue)
        actualValue = hw3.get(instance, 'mpg')
        actualValue = dataOp.getDeptEnergyRating(actualValue)
        hw3.printClassActual(classValue, actualValue)

# Step 2
# Builds a K-Nearest-Neighbor
def kNearestNeighborClassifier(table):
    normalizedTable = util.normalizeTable(table, constants.INDICES['mpg'])
    trainingSet, testSet = hw3.splitInstances(normalizedTable, len(normalizedTable)-5)

    k = 5

    for index, instance in enumerate(testSet):
        hw3.printInstance(table[index])
        classValue  = classifiers.k_nn(trainingSet,
            instance, len(instance), k, constants.INDICES['mpg'])
        classValue  = dataOp.getDeptEnergyRating(classValue)
        actualValue = hw3.get(instance, 'mpg')
        actualValue = dataOp.getDeptEnergyRating(actualValue)
        hw3.printClassActual(classValue, actualValue)

# Step 3
# Builds predictive accuracy
def computePredictiveAccuracy(table):
    normalizedTable = util.normalizeTable(table, constants.INDICES['mpg'])
    knn_acc, knn_error = hw3.randomSubsampleKnn(normalizedTable, 10)
    lin_acc, lin_error = hw3.randomSubsampleLinear(normalizedTable, 10)
    knn_c_acc, knn_c_error = hw3.crossFoldKnn(normalizedTable)
    lin_c_acc, lin_c_error = hw3.crossFoldLinear(normalizedTable)

    space = '   '
    knn = 'k Nearest Neighbors: accuracy ='
    linreg = 'Linear Regression: accuracy ='
    print "Random Subsample"
    print space, linreg, lin_acc, 'error rate=', lin_error
    print space, knn, knn_acc, 'error rate =', knn_error
    print "Stratified 10-Fold Cross Validation"
    print space, linreg, lin_c_acc, 'error rate=', lin_c_error
    print space, knn, knn_c_acc, 'error rate=', knn_c_error

def confusionMatrix(table):
    headers = ['MPG', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Total', 'Recognition (%)']
    left = list(xrange(1, 10, 1))

    normalizedTable = util.normalizeTable(table, constants.INDICES['mpg'])
    confusionTable = hw3.confusionMatrixTable(normalizedTable)

    print tabulate.tabulate(confusionTable, headers, tablefmt='rst')


def main():
    table = file_system.loadTable('auto-data-removedNA.csv')

    # Step 1
    hw3.printHeader('STEP 1: Linear Regression MPG Classifer')
    linearRegressionClassifier(table)

    # Step 2
    hw3.printHeader('STEP 2: k=5 Nearest Neighbor MPG Classifier')
    kNearestNeighborClassifier(table)

    # Step 3
    hw3.printHeader('STEP 3: Predictive Accuracy')
    computePredictiveAccuracy(table)

    hw3.printHeader('STEP 4: Confusion Matrix')
    confusionMatrix(table)


if __name__ == "__main__":
    main()
