import file_system
import analysis
import diagram
import util
import dataOperations
import constants
import numpy

indexDictionary = {
    'mpg'          : 0,
    'cylinders'    : 1,
    'displacement' : 2,
    'horsepower'   : 3,
    'weight'       : 4,
    'acceleration' : 5,
    'year'         : 6,
    'origin'       : 7,
    'name'         : 8,
    'msrp'         : 9
}

categoricalData = ['cylinders', 'year', 'origin']
continuousData  = ['mpg', 'displacement', 'horsepower', 'weight',
    'acceleration', 'msrp']

# Step 1
def makeFreqs(table):
    for name in categoricalData:
        col = util.getCol(table, indexDictionary[name])
        freqDict = analysis.frequency(col)
        diagram.frequency(freqDict, name, 'step-1-' + name)

# Step 2
def makePies(table):
    for name in categoricalData:
        col = util.getCol(table, indexDictionary[name])
        freqDict = analysis.frequency(col)
        diagram.pie(freqDict, name, 'step-2-' +name)

# Step 3
def makeDots(table):
    for name in continuousData:
        col = util.getCol(table, indexDictionary[name])
        freqDict = analysis.frequency(col)
        diagram.dot(freqDict, name, 'step-3-' +name)

# Step 4
def makeDiscretizedFreq(table):
    # Approach one
    col = util.getCol(table, indexDictionary['mpg'])
    freqDict = dataOperations.getFreqDictByDOE(col)
    labels = util.getRangeStrings(util.getValues(constants.DOE_RATINGS))
    diagram.frequencyWithRanges(freqDict, 'mpg-discrete-approach-1', labels, 'step-4-app-1')

    # Approach two
    col = util.getCol(table, indexDictionary['mpg'])
    freqDict = dataOperations.getFreqByEqualWidths(col, 5)
    labels = util.getRangeStrings(util.getKeys(freqDict))
    diagram.frequencyWithRanges(freqDict, 'mpg-discrete-approach-2', labels, 'step-4-app-2')

# Step 5
def makeHist(table):
    for name in continuousData:
        col = util.getCol(table, indexDictionary[name])
        freqDict = analysis.frequency(col)
        diagram.hist(freqDict, name, 'step-5-' + name )

# Step 6
def makeScatter(table):
    for name in continuousData:
        points = analysis.points(table, indexDictionary[name],
            indexDictionary['mpg'])
        diagram.scatter(points, name, 'step-6-' + name)

# Step 7
def makeLinearRegressions(table):
    for name in continuousData:
        points = analysis.points(table, indexDictionary[name],
            indexDictionary['mpg'])
        diagram.scatterWithLine(points, name, 'step-7-' + name)

    points = util.getXbyY(table, indexDictionary['weight'],
        indexDictionary['displacement'])
    diagram.scatterWithLine(points, 'displacement-weight', 'step-7-' + 'displace'
        'displacement', 'weight', False)

# Step 8
def makeBox(table):
    years = util.getCol(table, indexDictionary['year'])
    uniqueYears = numpy.unique(years)

    arrays = []
    for year in numpy.unique(years):
        col = util.getColBy(table,
            indexDictionary['mpg'], indexDictionary['year'], year)
        arrays.append(util.filterNA(col))

    diagram.box(arrays, 'MPG by year', uniqueYears, 'step-8-')

def makeCountryListDiagram(table):
    years = util.getCol(table, indexDictionary['year'])
    uniqueYears = numpy.unique(years)

    dictionary = {}
    for year in numpy.unique(years):
        col = util.getColBy(table,
            indexDictionary['origin'], indexDictionary['year'], year)
        dictionary[year] = (util.filterNA(col))

    finishedDict = {}
    for key, value in dictionary.iteritems():
        countDict = util.getCountDictionary(value)
        originDict = {
          constants.ORIGINS[1] : countDict[1],
          constants.ORIGINS[2] : countDict[2],
          constants.ORIGINS[3] : countDict[3]
        }
        finishedDict[key] = originDict

    diagram.countryListFreq(finishedDict)

def main():
    table = file_system.loadTable('auto-data.csv')
    makeCountryListDiagram(table)
    makeFreqs(table)
    makePies(table)
    makeDots(table)
    makeHist(table)
    makeScatter(table)
    makeDiscretizedFreq(table)
    makeLinearRegressions(table)
    makeBox(table)

if __name__ == '__main__':
    main()
