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
