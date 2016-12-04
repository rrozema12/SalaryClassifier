# data-mining-homework-4
This README acts as the log addressed in the assignment.

# Files
## hw4
The main file. Does the homework.

## hw4_utils
A collection of general functions that are used across the project.

## classifier_util
Contains helper functions to compute the classifications.

## homework_util
Contains getter functions that are used in the classifications.

## dataOperations
Handles Step 4 with approach one and approach two.

## constants
Creates the constants to use throughout the rest of the assignment.

## file_system
Helper functions to load the table and write to a file.

## math_utils
Used to calculate the Gaussian Distribuiton.

## knn and naive_bayes
Files that help compute classifications.

## output
Pretty prints our output so it looks nice and readable.

# Log
## Hiccups
None.

## Steps

### Step 1
Created a Naive Bayes classifier that predicts mpg values based on cylinders, weight,
and model year.  We descritized the values for weight using the ranking system given
in the original project file.

### Step 2
Basically recreated step one: created a Naive Bayes classifier that predicts 
mpg values based on cylinders, weight, and model year.  This time we left the value for
weight continuous and plugged it into the Gaussian distribution function.

### Step 3
Compared the KNN accuracy to the Naieve Bayes accuracy.  Instead of using the auto data 
file we have been using for the past few assignements, we used the titanic dataset.  In 
this part, we had to predict whether someone survived or died after the titanic sunk, given
an instance where the survival was unknown.
