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
import operator

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
<<<<<<< HEAD
#
# Get the nearest neigbbors by using a
# test set, training set, and the table
                
def kNearestNeighborClassifier(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = hw3.euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
        return neighbors


# Step 3
#
# Get the accuracy of our data
def getAccuracy(table):
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
       
   TP = hw3.getTP(classValue, actualValue)
   TN = hw3.getTN(classValue, actualValue)
   FP = hw3.getFP(classValue, actualValue)
   FN = hw3.getFN(classValue, actualValue)
   P = TP + FP
   N = TN + FN
   
   accuracy = (TP + TN) / (P + N)
   errorRate = (FP + FN) / (P + N)
   #precision = TP / (TP + FP)
   #recall = TP / (TP + FN)
   #fMeasure = (2 * precision * recall) / (precision + recall)
   
   
    
=======
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
>>>>>>> 91bf375f9d7131bd8745c2bda9ac70781caacc3a

def main():
    table = file_system.loadTable('auto-data-removedNA.csv')

    # Step 1
    hw3.printHeader('STEP 1: Linear Regression MPG Classifer')
    linearRegressionClassifier(table)

    # Step 2
    hw3.printHeader('STEP 2: k=5 Nearest Neighbor MPG Classifier')
<<<<<<< HEAD
    #trainingSet = []
    #testSet = []
    #hw3.splitDataset(table, 0.67, trainingSet, testSet)
    #kNearestNeighborClassifier(trainingSet, testSet, 5)
    
    # Step 3
    hw3.printHeader('STEP 3: Predictive Accuracy')
    getAccuracy(table)
=======
    kNearestNeighborClassifier(table)

>>>>>>> 91bf375f9d7131bd8745c2bda9ac70781caacc3a
if __name__ == "__main__":
    main()
