import matplotlib
matplotlib.use('pdf')
import matplotlib.pyplot as pyplot
import numpy
import util
import analysis
import math_utils
import dataOperations

figureFolder = 'graphs/'


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
    pyplot.savefig(filename)
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
    labels = [r'High School', r'Bachelors', r'masters', r'doctorate', r'dropout'
        , r'Assiciate', r'Middleschool', r'Elementary', r'Prof-school', r'other']
    pyplot.legend(labels)
    pyplot.legend(loc=2, prop={'size':6})
    pyplot.tight_layout()

    # Save plot
    filename = str(step) + '-pie-' + name + '.pdf'
    pyplot.savefig(filename)

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
