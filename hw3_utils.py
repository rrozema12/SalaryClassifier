import file_system
import constants
import math_utils
import numpy
from operator import itemgetter
import random
import util
from random import randint
import classifiers
import dataOperations as dataOp
from collections import Counter
import tabulate

# Gets by name instead of by index
def get(row, name):
    index = constants.INDICES[name]
    return row[index]

# Gets a 2d array of points, from the index
# names.
#
# Example:
#   getPoints(table, 'name', 'msrp')
# would give
# [['chevrolet monte carlo', 3123], ['nameofcar', 2312]]
#
def getPoints(table, *names):
    points = []
    for row in table:
        point = []
        for name in names:
            point.append(get(row, name))
        points.append(point)
    return points

# Gets a number of random instances from the table
def getInstances(table, num):
    return random.sample(table, num)

# Returns training, then test sets
def splitInstances(table, numTraining):
    indices = range(len(table))
    trainingIndices = random.sample(indices, numTraining)
    testIndices = [item for item in indices if item not in trainingIndices]
    return ([table[i] for i in trainingIndices],
        [table[i] for i in testIndices])

# Returns test then training sets
def holdout_partition(table):
    randomized = table[:]
    n = len(table)
    for i in range(n):
        j = randint(0, n-1)
        randomized[i], randomized[j] = randomized[j], randomized[i]
    n0 = (n * 2)/3
    return randomized[0:n0], randomized[n0:]

# Creates stratified cross validation folds where
# the fold's data has the same class label
def stratFolds(table, byLabelIndex, numOfPartitions):
    randomized = table[:]
    partitions = {}

    for row in table:
        label = row[byLabelIndex]
        try:
            partitions[label].append(row)
        except KeyError:
            partitions[label] = [row]

    folds = {}
    index = 0
    for key, table in partitions.iteritems():
        for row in table:
            try:
                folds[index].append(row)
            except KeyError:
                folds[index] = [row]
            index += 1
            if index > numOfPartitions:
                index = 0
    return util.dictionaryToArray(folds)

# Gets a number of random instances from the table
def getInstances(table, num):
    numInstances = len(table)
    choices = numpy.random.choice(numInstances, num)
    return [table[i] for i in choices]

# Splits the dataset so 2/3 of the data is in the
# training set and 1/3 of athe data is in the
# test set.
def splitDataset(filename, split, trainingSet=[] , testSet=[]):
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    for x in range(len(dataset)-1):
	        for y in range(4):
	            dataset[x][y] = float(dataset[x][y])
	        if random.random() < split:
	            trainingSet.append(dataset[x])
	        else:
	            testSet.append(dataset[x])

# Finds the euclidean distance
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length):
		distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

# Get the array as a comma seperated string, then kill
# the last comma
def getInstanceString(instance):
    return ''.join(str(i)+', ' for i in instance).strip()[:-1]

def printInstance(instance):
    print 'instance:', getInstanceString(instance)

def printClassActual(classValue, actualValue):
    print 'class:', classValue, 'actual:', actualValue

def printHeader(text):
    print '==========================================='
    print text
    print '==========================================='

def accuracy(classValues, actualValues):
    total = len(classValues)
    correct = 0
    for i in range(len(classValues)):
        if classValues[i] == actualValues[i]:
            correct += 1
    return correct*1.0/total*1.0

def knn(trainingSet, testSet, k):
    classValues = []
    actualValues = []
    for index, instance in enumerate(testSet):
        classValue  = classifiers.k_nn(trainingSet,
            instance, len(instance), k, constants.INDICES['mpg'])
        classValues.append(dataOp.getDeptEnergyRating(classValue))
        actualValue = get(instance, 'mpg')
        actualValues.append(dataOp.getDeptEnergyRating(actualValue))

    acc = accuracy(classValues, actualValues)
    error = 1 - acc

    return acc, error

def linearRegression(trainingSet, testSet):

    # Make the linear regression funtion to get MPG
    getMPG = math_utils.linear_regression(trainingSet)

    classValues = []
    actualValues = []
    for instance in testSet:
        classValue  = getMPG(get(instance, 'weight'))
        classValue  = dataOp.getDeptEnergyRating(classValue)
        classValues.append(classValue)
        actualValue = get(instance, 'mpg')
        actualValue = dataOp.getDeptEnergyRating(actualValue)
        actualValues.append(actualValue)

    acc = accuracy(classValues, actualValues)
    error = 1 - acc
    return acc, error

def randomSubsampleLinear(table, k):
    accs = []
    errors = []
    for i in range(k):
        trainingSet, testSet = holdout_partition(table)
        accuracy, error = linearRegression(trainingSet, testSet)
        accs.append(accuracy)
        errors.append(error)

    return numpy.mean(accs), numpy.mean(errors)

def randomSubsampleKnn(table, k):
    accs = []
    errors = []
    for i in range(k):
        trainingSet, testSet = holdout_partition(table)
        accuracy, error = knn(trainingSet, testSet, 4)
        accs.append(accuracy)
        errors.append(error)

    return numpy.mean(accs), numpy.mean(errors)

def crossFoldLinear(table):
    folds = stratFolds(table, constants.INDICES['mpg'], 10)

    accs = []
    errors = []
    for fold in folds:
        trainingSet, testSet = holdout_partition(fold)
        accuracy, error = linearRegression(trainingSet, testSet)
        accs.append(accuracy)
        errors.append(error)

    return numpy.mean(accs), numpy.mean(errors)

def crossFoldKnn(table):
    folds = stratFolds(table, constants.INDICES['mpg'], 10)

    accs = []
    errors = []
    for fold in folds:
        trainingSet, testSet = holdout_partition(fold)
        accuracy, error = knn(trainingSet, testSet, 4)
        accs.append(accuracy)
        errors.append(error)

    return numpy.mean(accs), numpy.mean(errors)

def knnForActuals(trainingSet, testSet, k):
    points = []
    for index, instance in enumerate(testSet):
        classValue  = classifiers.k_nn(trainingSet,
            instance, len(instance), k, constants.INDICES['mpg'])
        classes = dataOp.getDeptEnergyRating(classValue)

        actualValue = get(instance, 'mpg')
        actual = dataOp.getDeptEnergyRating(actualValue)

        points.append([actual, classes])

    return points

def confusionMatrixTable(table):
    folds = stratFolds(table, constants.INDICES['mpg'], 10)

    pointsList = []

    for fold in folds:
        trainingSet, testSet = holdout_partition(fold)
        points = knnForActuals(trainingSet, testSet, 4)
        pointsList.extend(points)

    # Add core data
    graphData = [[0 for i in xrange(11)] for i in xrange(10)]
    for point in pointsList:
        graphData[point[1]-1][point[0]] += 1

    # Add Total
    for row in graphData:
        row.append(sum(row))

    # Add Recognition %
    for index, row in enumerate(graphData):
        total = row[-1]
        guessedRight = row[index]

        if total != 0:
            row.append(guessedRight * 1.0 / total)
        else:
            row.append(0)

    # Add left side
    for index, row in enumerate(graphData):
        row[0] = index + 1

    return graphData


if __name__ == "__main__":
    table = [
        [1, 2, 'hi'],
        [0, 2, 'hi'],
        [1, 1, 'hi'],
        [1, 2, 'by'],
        [1, 2, 'by'],
        [1, 3, 'by'],
        [13, 2, 'by'],
        [1, 2, 'hi'],
    ]
