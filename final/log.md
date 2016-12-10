#Log
This is a log of each step I took to complete the final project.

##Data Cleaning
 - Cut the dataset down significantly; more specifically I cut it down to 7500.
   It was much bigger before, around 50,000. I cut it down to minimize time on
   the running of my program.  I believe that 7500 was small enough to be
   efficient but also large enough to capture the values of the whole dataset.
 - I began cleaning the dataset by hand. If there were any missing values
   in the data set then they were previously identified as a "?". I changed
   this because the scripts that we wrote in class were built to take care
   of missing values labeled with "NA".
 - I used my data cleaning script to remove the instances that contained an NA.
   I do this because I need my scripts to be able to run without errors, and
   missing (NA) values will cause me lots of problems.  Because most of the
   important attributes are not populated with numbers, I can not replace them
   with the averages, so I elected to get rid of them.
 - Changed the values of some of the instances so that it is easier for someone
   who is viewing the table can easily understand what is going on in the
   dataset.
 - I eliminated some attributes because I felt like they were not as important
   to the dataset.
 - I ran into a problem where there were a lot of spaces in my code, especially after
   the commas. This was a very simple fix by deleting all the spaces by hand using
   excel with the find and replace functionality.

##Data Visualization
  - I was able to use a couple of the pyplot functions that we used in homework
    two to graph some of my data.  some of the most interesting graphs were the
    frequency diagram and the pie chart.
  - These two diagrams show specific characteristics about each attribute.  For
    example, there are a lot more high school degrees in the dataset than I would
    have expected.  Each of these graphs accurately show the number of times that
    each degree occurs and the percentage it occurs.  I decided to keep these two
    in my report for this reason.   

##Classifiers
These are a couple classifiers and one ensemble method that I used on my dataset.

###K-Nearest Neighbors
 - For K-Nearest Neighbors, I basically used the code from assignment three.
   Because the majority of my code was categorical data, I needed to go through
   and map each of the columns to give them a number.
 - This helped me do the calculations as well as print out the confusion matrix
   much easier.
 - After running the program multiple times, the highest accuracy for K-NN
   classification is 79.43179% with a random sample, and a 79.832297% accuracy
   with the stratified cross folds.
 - The highest recognition in the confusion matrix was 91.767676% for salary
   0 (less than or equal to 50k) and 43.7136% recognition for salary 1
   (greater than 50k).

###Naive Bayes
 - For Naive Bayes, I basically used the code from assignment four.
   Because the majority of my code was categorical data, I needed to go through
   and map each of the columns to give them a number.
 - This helped me do the calculations as well as print out the confusion matrix
   much easier.
 - After running the program multiple times, the highest accuracy for Naive Bayes
   classification is 77.206679% with a random sample, and a 77.490241% accuracy
   with the stratified cross folds.
 - The highest recognition in the confusion matrix was 91.9792% for salary
   0 (less than or equal to than 50k) and 33.6438% recognition for salary 1
   (greater than 50k).

###Decision Trees
- For Decision Trees, I basically used the code from assignment five.
  Because the majority of my code was categorical data, I had to repeat the same
  step of discretization as I did for K-Nearest Neighbors and Naive Bayes
  and map each of the columns to give them a number.
- This helped me do the calculations as well as print out the confusion matrix
  much easier.
- After running the program multiple times, the highest accuracy for Decision Trees
  classification is 77.3890414% accuracy with the stratified cross folds.
- The highest recognition in the confusion matrix was 95.9223% for salary
  0 (less than or equal to 50K) and 21.3038% recognition for salary 1
  (greater than 50k).
- The rules that I generated rose some interesting associations.  (Finish!!!!)

###Random Forests
- For Random Forests, I basically used the code from assignment six.
  Because the majority of my code was categorical data, I had to repeat the same
  step of discretization and map each of the columns to give them a number.
- I picked very specific N, M, and F values that gave me the highest accuracy.
- N = 6000, M = 215, F = 2 gave me an accuracy of 77.6749566%
- The highest recognition in the confusion matrix was 95.6923% for salary
  0 (less than or equal to 50k) and 20.7459% recognition for salary 1
  (greater than 50k).
- One error that I continued to run into was that sometimes my confusion matrix
  wouldn't print out the guesses for a salary >50K.  I was able to fix this by not
  discretizing the columns.
