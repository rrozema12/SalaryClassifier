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
