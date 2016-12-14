import util
import numpy
import math
import operator
from functools import partial

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

def prod(iterable):
    """ basically sum() but for products """
    return reduce(operator.mul, iterable, 1)

def gaussian(x, mean, sdev):
    """ Computes a gaussian """
    first, second = 0, 0
    if sdev > 0:
        first = 1 / (math.sqrt(2 * math.pi) * sdev)
        second = math.e ** (-((x - mean) ** 2) / (2 * (sdev ** 2)))
    return first * second

def get_gaussian_application(col):
    """ Returns a function that applys the gaussian to X
    without recalculating the mean and sdev each time

    :param col Assumes instances of attribute for some label
    """

    mean = numpy.mean(col)
    sdev = numpy.std(col)
    return partial(gaussian, mean=mean, sdev=sdev)

def gaussian_probability(x, col):
    """ Gets the Gaussian probability
    WARNING: this is really inefficient in a loop becuase it will
    recalculate the mean and sdev each time. Just a heads up.
    """
    return get_gaussian_application(col)(x)


if __name__ == '__main__':
    table = [[6, 5, 183.0, 77.0, 3530, 20.1, 79, 2, 'mercedes benz 300d', 21497],
    [5, 8, 350.0, 125.0, 3900, 17.4, 79, 1, 'cadillac eldorado', 14668],
    [7, 4, 141.0, 71.0, 3190, 24.8, 79, 2, 'peugeot 504', 8040],
    [5, 8, 260.0, 90.0, 3420, 22.2, 79, 1, 'oldsmobile cutlass salon brougham', 5442],
    [8, 4, 105.0, 70.0, 2200, 13.2, 79, 1, 'plymouth horizon', 4469],
    [8, 4, 105.0, 70.0, 2150, 14.9, 79, 1, 'plymouth horizon tc3', 4864],
    [9, 4, 91.0, 69.0, 2130, 14.7, 79, 2, 'fiat strada custom', 4496],
    [7, 4, 151.0, 90.0, 2670, 16.0, 79, 1, 'buick skylark limited', 4462],
    [6, 6, 173.0, 115.0, 2700, 12.9, 79, 1, 'oldsmobile omega brougham', 4582],
    [8, 4, 151.0, 90.0, 2556, 13.2, 79, 1, 'pontiac phoenix', 4089]]

    import table_utils
    # filteredTable = table_utils.getWhere(table, [(1, 4)])
    # getGaussianProbability = get_gaussian_application(table_utils.getCol(filteredTable, 4))
    # print(getGaussianProbability(2200))
    #
    print(gaussian(2400 ,2482, 377))
