import file_system
import analysis
import diagram
import util
import dataOperations
import constants
import numpy
import table_utils
import homework_util as homework

indexDictionary = {
    'age'           : 0,  # income dataset
    'job-type'      : 1,
    'degree'        : 2,
    'marital-status': 3,
    'ethnicity'     : 4,
    'gender'        : 5,
    'country'       : 6,
    'salary'        : 7
}

# Step 1
def makeFreqs(table):
    col = util.getCol(table, indexDictionary['degree'])
    freqDict = analysis.frequency(col)
    diagram.frequency(freqDict, 'degree', 'Degree')

# Step 2
def makePies(table):

    col = util.getCol(table, indexDictionary['degree'])
    freqDict = analysis.frequency(col)
    diagram.pie(freqDict, 'degree', 'Degree')

# Step 4
def makeDiscretizedFreq(table):
    # Approach two
    col = util.getCol(table, indexDictionary['degree'])
    freqDict = dataOperations.getFreqByEqualWidths(col, 5)
    labels = util.getRangeStrings(util.getKeys(freqDict))
    diagram.frequencyWithRanges(freqDict, 'mpg-discrete-approach-2', labels, 'step-4-app-2')

# Step 5
def makeHist(table):
    col = util.getCol(table, indexDictionary['age'])
    freqDict = analysis.frequency(col)
    diagram.hist(freqDict, name, 'step-5-' + name )

# Step 6

def main():
    table = file_system.loadTable('incomeDataNoNA.csv')

    table = table_utils.mapCol(table, constants.INDICES['job-type'],
                               homework.get_job_type)
    table = table_utils.mapCol(table, constants.INDICES['degree'],
                               homework.get_degree)
    table = table_utils.mapCol(table, constants.INDICES['marital-status'],
                               homework.get_marital_status)
    table = table_utils.mapCol(table, constants.INDICES['ethnicity'],
                               homework.get_ethnicity)
    table = table_utils.mapCol(table, constants.INDICES['gender'],
                               homework.get_gender)
    table = table_utils.mapCol(table, constants.INDICES['country'],
                               homework.get_country)
    table = table_utils.mapCol(table, constants.INDICES['salary'],
                               homework.get_salary)
    makeFreqs(table)
    makePies(table)
    makeHist(table)
    makeDiscretizedFreq(table)

if __name__ == '__main__':
    main()
