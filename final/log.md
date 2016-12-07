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
 - I ran into a problem where there were a lot of spces in my code.  This was
   a very simple fix by deleting all the spaces by hand using excel with the
   find and replace functionality.

##Data Visualization


##Classifiers


###K-Nearest Neighbors
 - For K-Nearest Neighbors, I basically used the code from assignment three.
   Because the majority of my code was categorical data, I needed to go through
   and map each of the columns to give them a number.
 - This helped me do the calculations as well as print out the confusion matrix
   much easier.
 - After running the program multiple times, the highest accuracy for K-NN 
   classification is 79.43179% with a random sample, and a 79.832297% accuracy
   with the stratified cross folds.
 - The highest recognition in the conusion matrix was 91.767676% for salary 
   0 (greater than 50k) and 43.7136% recognition for salary 1 (less than 
   or equal to 50k).


###Naive Bayes
 - For Naive Bayes, I basically used the code from assignment four.
   Because the majority of my code was categorical data, I needed to go through
   and map each of the columns to give them a number.
 - This helped me do the calculations as well as print out the confusion matrix
   much easier.
 - After running the program multiple times, the highest accuracy for K-NN 
   classification is 77.206679% with a random sample, and a 77.490241% accuracy
   with the stratified cross folds.
 - The highest recognition in the conusion matrix was 91.9792% for salary 
   0 (greater than 50k) and 33.6438% recognition for salary 1 (less than
   or equal to 50k).


###Decision Trees


###Random Forests
