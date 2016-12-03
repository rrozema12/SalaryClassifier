######## hw2.py

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


######### diagram.py
import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as pyplot
import numpy
import util
import analysis
import math_utils
import dataOperations

figureFolder = 'pdfs/'


def frequency(frequencyDict, name, title):
    pyplot.figure()

    # Create values
    ys = util.getValues(frequencyDict)
    xs = util.getKeys(frequencyDict)
    xrng = numpy.arange(len(xs))

    # Create plot
    pyplot.suptitle('Frequency of ' + name)
    pyplot.bar(xrng, ys, alpha=0.75, align='center')
    pyplot.xticks(xrng, xs)

    # Save plot
    filename = title + '.pdf'
    pyplot.savefig(figureFolder + filename)
    pyplot.xlabel(name)
    pyplot.ylabel('Count')

    pyplot.figure() # Reset for good measure
    pyplot.close()

def frequencyWithRanges(frequencyDict, name, xlabels, title):
    pyplot.figure()

    # Create values
    ys = util.getValues(frequencyDict)
    xs = util.getKeys(frequencyDict)
    xrng = numpy.arange(len(xs))

    # Create plot
    pyplot.suptitle(name)
    pyplot.bar(xrng, ys, alpha=0.75, align='center')
    pyplot.xticks(xrng, xlabels)
    pyplot.ylabel('Count')

    # Save plot
    filename = title + '.pdf'
    pyplot.savefig(figureFolder + filename)

    pyplot.figure() # Reset for good measure
    pyplot.close()

def pie(frequencyDict, name, step):
    pyplot.figure()

    # Create values
    ys = util.getValues(frequencyDict)
    xs = util.getKeys(frequencyDict)

    # Create plot
    pyplot.suptitle(name)
    pyplot.pie(ys, labels=xs, autopct='%1.1f%%')
    labels = [r'mpg', r'cylinders', r'displacement', r'horsepower', r'weight'
        , r'acceleration', r'year', r'origin', r'name', r'msrp']
    pyplot.legend(labels)
    pyplot.tight_layout()

    # Save plot
    filename = str(step) + '-pie-' + name + '.pdf'
    pyplot.savefig(figureFolder + filename)

    pyplot.figure() # Reset for good measure
    pyplot.close()

def dot(frequencyDict, name, step):
    pyplot.figure()

    # Create values
    xs = util.getKeys(frequencyDict)
    xs.sort() # Sort the x values
    ys = [1] * len(xs)

    # Create Plot
    pyplot.suptitle(name)
    pyplot.plot(xs, ys, 'b.', alpha=0.2, markersize=6)
    pyplot.gca().get_yaxis().set_visible(False)
    pyplot.xlabel(name)

     # Save plot
    filename = str(step) + '-dot-' + name + '.pdf'
    pyplot.savefig(figureFolder + filename)

    pyplot.figure() # Reset for good measure

def hist(frequencyDict, name, step):
    pyplot.figure()

    # Create values
    xs = util.getKeys(frequencyDict)
    max_val = max(xs)
    min_val = min(xs)
    increment = int((max_val - min_val)) / 10
    xticks = numpy.arange(min_val, max_val, float(increment))

    # Create plot
    pyplot.suptitle(name)
    pyplot.hist(xs, bins=10, alpha=0.95, color='r', align='left', rwidth=1)
    pyplot.xticks(xticks)

    # Save plot
    filename = str(step) + '-hist-' + name + '.pdf'
    pyplot.savefig(figureFolder + filename)
    pyplot.xlabel(name)
    pyplot.ylabel('Count')

    pyplot.figure() # Reset for good measure

def scatter(points, name, step):
    pyplot.figure()

    # Create values
    xs = util.getCol(points, 0)
    ys = util.getCol(points, 1)

    # Create plot
    pyplot.suptitle(name + ' vs. ' + 'MPG')
    pyplot.plot(xs, ys, 'b.')
    pyplot.xlim(0, int(max(xs) * 1.1))
    pyplot.ylim(0, int(max(ys) * 1.1))
    pyplot.grid(True)
    pyplot.ylabel('MPG')
    pyplot.xlabel(name)

    # Save plot
    filename = str(step) + '-scatter-' + name + '.pdf'
    pyplot.savefig(figureFolder + filename)
    pyplot.figure() # Reset for good measure
    pyplot.close()

def box(arrays, name, xlabels, step):
    pyplot.figure()
    fig, ax = pyplot.subplots()

    ax.boxplot(arrays)
    pyplot.xticks(numpy.arange(1, len(xlabels)+1, 1), xlabels)

    filename = str(step) + '-box-' + name + '.pdf'
    pyplot.savefig(figureFolder + filename)
    pyplot.close()

def countryListFreq(countriesDict):
    pyplot.figure()

    europes = dataOperations.getAllOfOrigin(countriesDict, 'Europe')
    japans = dataOperations.getAllOfOrigin(countriesDict, 'Japan')
    americas = dataOperations.getAllOfOrigin(countriesDict, 'USA')
    years = util.getKeys(countriesDict)

    fig, ax = pyplot.subplots()

    ind = numpy.arange(len(years))
    width = 0.2

    r1 = ax.bar(ind, europes, width, color='b')
    r2 = ax.bar(ind+width, japans, width, color='r')
    r3 = ax.bar(ind+(width*2), americas, width, color='g')

    ax.set_xticks(ind + (width*2))
    ax.set_xticklabels(years)
    ax.set_ylabel('Number of Cars')
    ax.set_xlabel('Year')

    ax.legend((r1[0], r2[0], r3[0]), ('Europe', 'Japan', 'USA'), loc=1)

    pyplot.savefig(figureFolder + 'step-8-country-list.pdf')
    pyplot.close()

def scatterWithLine(points, name, step, ylabel='MPG', xlabel=None, usesMPG=True):
    pyplot.figure()

    xs = util.getCol(points, 0)
    ys = util.getCol(points, 1)

    correlationCoeff = str(round(math_utils.correlationCoeff(points), 2))
    covariance = str(round(math_utils.covariance(points), 2))

    vs = ''
    if (usesMPG):
        vs = 'vs. MPG; '

    firstPart = name + vs + ' Correlation: '
    title = firstPart + correlationCoeff + ' Covariance: ' + covariance

    # Create plot
    pyplot.suptitle(title)
    pyplot.plot(xs, ys, 'b.')
    pyplot.xlim(0, int(max(xs) * 1.1))
    pyplot.ylim(0, int(max(ys) * 1.1))
    pyplot.grid(True)
    pyplot.ylabel(ylabel)
    if not xlabel:
        pyplot.xlabel(name)
    else:
        pyplot.xlabel(xlabel)

    linePoints = math_utils.graphablePoints(points)
    lineXs = util.getCol(linePoints, 0)
    lineYs = util.getCol(linePoints, 1)
    pyplot.plot(lineXs, lineYs, 'r')

    # Save plot
    filename = str(step) + '-scatter-regression-' + name + '.pdf'
    pyplot.savefig(figureFolder + filename)

    pyplot.figure()
    pyplot.close()

######## math_utils.py

import util
import numpy
import math

def slope(points, x_bar, y_bar):
    top_values = []
    bot_values = []
    for point in points:
        x = point[0]
        y = point[1]
        top_values.append((x - x_bar)*(y - y_bar))
        bot_values.append((x - x_bar)*(x - x_bar))

    return sum(top_values)/sum(bot_values)

def correlationCoeff(points):
    xs = util.getCol(points, 0)
    ys = util.getCol(points, 1)
    x_bar = numpy.mean(xs)
    y_bar = numpy.mean(ys)

    x_delta = []
    y_delta = []
    x_bot_delta = []
    y_bot_delta = []
    for point in points:
        x = point[0]
        y = point[1]

        topX = (x - x_bar)
        topY = (y - y_bar)
        x_delta.append(topX)
        y_delta.append(topY)
        x_bot_delta.append(topX*topX)
        y_bot_delta.append(topY*topY)

    top = sum(x_delta)*sum(y_delta)
    bot = math.sqrt(sum(x_bot_delta)*sum(y_bot_delta))
    return top/bot

def covariance(points):
    xs = util.getCol(points, 0)
    ys = util.getCol(points, 1)
    x_bar = numpy.mean(xs)
    y_bar = numpy.mean(ys)

    def topPart(point):
        return math.pow((point[0] - x_bar),2) * math.pow((point[1] - y_bar),2)

    top = [ topPart(point) for point in points ]
    return sum(top)/(len(points)-1)

def linear_regression(points):
    xs = util.getCol(points, 0)
    ys = util.getCol(points, 1)
    x_bar = numpy.mean(xs)
    y_bar = numpy.mean(ys)

    m = slope(points, x_bar, y_bar)
    b = y_bar - m*x_bar

    def line(x):
        return m*x + b
    return line

def graphablePoints(points):
    xs = util.getCol(points, 0)
    max_x = max(xs)
    min_x = min(xs)
    getY = linear_regression(points)

    return [[min_x, getY(min_x)], [max_x, getY(max_x)]]

if __name__ == '__main__':
    print covariance([[0, 1], [1.5, 2], [2, 4], [8, 5]])


####### dataOperations
import util
import numpy
import collections
import constants

def getDeptEnergyRating(x):
    # Gets the range values for the DOE rankings
    keys     = util.getValues(constants.DOE_RATINGS)

    # Gets the left-end of the range x belongs in
    lowRange = util.getLowRange(keys, x)

    # Flips the dictionary, so we can query by value
    byValue  = util.flipKeyValues(constants.DOE_RATINGS)

    return byValue[lowRange]


# Approach 1
def getFreqDictByDOE(col):
    # Create empty dict
    keys = range(1, 11)
    freq = util.createDict(keys, [0] * len(keys))

    for el in col:
        rating = getDeptEnergyRating(el)
        freq[rating] += 1
    return freq

# Approach 2
def getFreqByEqualWidths(col, num_bins):
    keys = sorted(util.getBins(col, num_bins))
    dictionary = util.createDict(keys, [0] * len(keys))
    freq = collections.OrderedDict(sorted(dictionary.items()))

    for el in col:
        key = util.getLowRange(keys, el)
        freq[key] += 1
    return freq

def getAllOfOrigin(originDict, origin):
    return [value[origin] for key, value in originDict.iteritems()]


if __name__ == '__main__':
    print '10 =', getDeptEnergyRating(50)
    print '1 =', getDeptEnergyRating(0)
    print '7 =', getDeptEnergyRating(28)
