# Classification Algorithims on CSV Datasets

## Description of the Goal and how to Execute
The goal of the project is to develop and evaluation classifiers for a dataset.

Given a new person with some of the attributes from the table, I will be
predicting whether that person will make more or less than 50k per year.

This dataset has a little more than 7,000 instances and has seven attributes.

Run this program by entering the following: `python classify.py > ../output/output_file_name`
  - This will generate an output file with all of the classifier information in a file name
    of your choosing.
  - The visualization part of this project can be found in the graphs folder once the
    program has run to completion.
  - The "output_file_name" part of the program execution is not necessary.  It is there
    because there is a matplotlib warning in the output that I can not find a solution
    for.  Until I find a solution, the "prettiest" way to see the output is if you
    direct the output to a file.

### Requirements - Download and Install:
1. numpy  
    ```
    pip install numpy
    ```
2. matplotlib
    ```
    pip install matplotlib
    ```
3. tabulate  
    ```
    pip install tabulate
    ```

## Details about the Sample Dataset
For my project I will be using a dataset with 20,000 instances that will help predict whether a particular person makes more than 50k a year based on particular qualities. The descriptions of these attributes are defined below.

1. **Age**   
    > The current age of each person when the data was collected.   

2. **Degree**   
    > The highest level of education that each person had when the data was collected. This can be High School, Bachelors, Masters, Doctorate, College Drop Out, Associate, Middle School, Elementary, or Professional School.  

3. **Marital Status**   
    > The current marital status of each person when the data was collected.  This can be Never Married, Married, Divorced, Spouse Absent, Widowed, or Seperated.

4. **Ethnicity**  
    > The ethnicity of each person that had their data collected. This can be White, Black, Native American, or Asian.

5. **Gender**  
    > The gender of each person that had their data collected. This can be Male or Female.

6. **Country**  
    > The current country that each person resided at the time of the data was collected. This could be the United States, the Philippines, Puerto Rico, Mexico, the Dominican Republic, Portugal, Canada, Taiwan, Cuba, or Jamaica.

7. ***Salary***: *The attribute that we will classify on*
    > The current salary that each person made at the time the data is collected.  This will be the attribute that we are classifying on. This could be either >50k or <=50k.

**Note**: Every attribute (besides age) are categorical.  This meant that I needed to go through the entire data set and discretize it, making a temporary dataset that has continuous attributes that represent categorical data.

## File Names and Descriptions
### constants.py
Only for constant variables. No functions please.

### file_system.py
Only for reading/writing files.

### math_utils.py
Only for math. Just math math math math.

### table_utils.py
For manipulating a 2d array (table).

### homework_util.py
Put functions in here that are specific to a homework assignment.

### naive_bayes.py
This is the naive_bayes module.

### knn.py
Contains functions pertaining to KNN

### classifier_util.py
This is utilities that can apply to any classifier. For example: accuracy,
error rate, ect.

### partition.py
If you're splitting up a table, put it here

### decision_tree.py
Functions for decision tree stuff

### random_forest.py
Functions for random forest stuff

## Output
```
===========================================
Rows with NAs have been removed.
===========================================

===========================================
Data visualization complete.
===========================================

===========================================
K-Nearest Neighbors
===========================================
	Random Subsample
		Accuracy = 0.784615384615, error rate = 0.215384615385
	Stratified Cross Folds (5)
		Accuracy = 0.8, error rate = 0.2

===========================================
Confusion Matrix
===========================================
========  ===  ===  =======  =================
  Salary    1    0    Total    Recognition (%)
========  ===  ===  =======  =================
       1    0    8        8                  0
       0    0   32       32                100
========  ===  ===  =======  =================

===========================================
Naive Bayes
===========================================
	Random Subsample
		Accuracy = 0.757692307692, error rate = 0.242307692308
	Stratified CrossFolding
		Accuracy = 0.8, error rate = 0.2

===========================================
Confusion Matrix
===========================================
========  ===  ===  =======  =================
  Salary    1    0    Total    Recognition (%)
========  ===  ===  =======  =================
       1    2    6        8              25
       0    2   30       32              93.75
========  ===  ===  =======  =================

===========================================
Decision Tree
===========================================
IF degree == 1 THEN salary = 0
IF degree == 2 THEN salary = 0
IF degree == 3 THEN salary = 1
IF degree == 4 THEN salary = 1
IF degree == 5 THEN salary = 0
IF degree == 6 THEN salary = 0
IF degree == 7 THEN salary = 0


Stratified CrossFolding
	Accuracy = 0.825, error rate = 0.175



===========================================
Confusion Matrix
===========================================
========  ===  ===  =======  =================
  Salary    1    0    Total    Recognition (%)
========  ===  ===  =======  =================
       1    2    6        8             25
       0    1   31       32             96.875
========  ===  ===  =======  =================

===========================================
Random Forest
===========================================
N = 3000 M = 215 F = 2
	Accuracy = 0.8

===========================================
Confusion Matrix
===========================================
========  =======  ======  =======  =================
Salary      <=50K    >50K    Total    Recognition (%)
========  =======  ======  =======  =================
<=50K           8       0        8                100
>50K            2       0        2                  0
======== ======= ====== ======= =================
```
## Sources
The dataset is from: http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
