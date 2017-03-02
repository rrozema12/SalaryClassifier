# Data-Mining-Final-Project
The goal of the project is to develop and evaluation classifiers for a dataset.

Given a new person with some of the attributes from the table, I will be
predicting whether that person will make more or less than 50k per year.

Run this program by entering the following: python final_project.py > "output_file_name"
  - This will generate an output file with all of the classifier information in a file name
    of your choosing.
  - The visualization part of this project can be found in the graphs folder once the
    program has run to completion.
  - The "output_file_name" part of the program execution is not necessary.  It is there
    because there is a matplotlib warning in the output that I can not find a solution
    for.  Until I find a solution, the "prettiest" way to see the output is if you
    direct the output to a file.

## Details
For my project I will be using a dataset corresponding to whether a particular
person makes more than 50k a year based on particular qualities.

Some of the attributes that I will be using are:
   - age
   - degree
   - marital status
   - position in company
   - ethnicity
   - gender
   - country
   - salary

Every attribute (besides age) are categorical.  This meant that I needed to go through
the entire data set and discretize it, making a temporary dataset that has
continuous attributes that represent categorical data.


## Sources
The dataset is from: http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data

# Wiki
The project is split up into many "util" modules to help keep organized.

### Rules:
1. If you're making a new classifier, put it in it's own module.
2. Use `module-level private` functions with a single underscore `_myPrivate()`
3. Delete things. (It's all saved to git anyway)
4. Comment (I haven't been so good about this), and add to wiki if you make
a new module

### Guidelines:
1. If you can be general, be general. For example:

```
# BAD
def getMPGs():
  ...

# GOOD
def getColByName():
  """ getColByName('mpg') """
  ...
```


## Modules
A list of modules.

### util.py
Hyper general functions that don't fall into any of the below
categories.

#### Good utility function:
```
def dictionaryToArray(dictionary):
    return [ value for key, value in dictionary.iteritems()]
```

#### Bad utility function:
```
def normalizeTable(table, exceptFor=None):
  ...
```

### constants.py
Only for constant variables. No functions please.

### file_system.py
Only for reading/writing files.

### math_utils.py
Only for math. Just math math math math.

### table_utils.py
For manipulating a 2d array (table).

### homework_util.py
Put functions in here that are specific to a homework assignment. If you ask
yourself the question "Would I need this in a personal project?" and you
say "no", then put it in `homework_util`. Don't abuse this. Be more general
if you can.

### naive_bayes.py
This is the naive_bayes module. Duh?

### knn.py
Contains functions pertaining to knn

### classifier_util.py
This is utilities that can apply to any classifier. For example: accuracy,
error rate, ect.

### partition.py
If you're splitting up a table, put it here

### decision_tree.py
Functions for decision tree stuff

### random_forest.py
Functions for random forest stuff

