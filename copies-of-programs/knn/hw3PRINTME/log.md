# Files
The main core of the project is in `hw3.py`, but we stuck helper
functions in their own module called `hw3_utils.py`. We also
modularized the KNN classifier into a module named `classifiers`. 

# Steps

## Step 1
We created a classifier by using the linear regression function
we created in hw2, in `math_utils.py`. We randomly picked 5 instances
from the set, and then ran the function on each instance.

## Step 2
We created a nearest neighbor classifier for MPG using k = 5.
I'm not quite sure if this is as accurate as we'd like it to be,
I was hoping that it would be more accurate than the linear
regression, but so far it seems like the linear regression is
often much more accurate.

## Step 3
We used a random subsample and stratified 10-fold cross validation to
print the accuracy, which we calculated by taking the number of
correctly classified divided by the total number of instances. It
does seem like the KNN algorithm is on average much less accurate than
then linear regression. Is this the expected case?

## Step 4
We created a confusion matrix based on the stratified 10-fold cross
validation results. We chose to use the `tabulate` package.
