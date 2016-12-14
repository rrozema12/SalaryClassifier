import util
import constants
import table_utils

def print_confusion_matrix(labels, class_label_name):
    """ Prints the confusion matrix of the given labels

    :param labels: A list of tuples of class labels [(actual, predicted),...]
    :param class_label_name: The name of the class label
    """
    class_labels = list(set(table_utils.getCol(labels, 0)))  # all the actual class labels
    the_headers = [class_label_name]
    the_headers.extend(class_labels)
    the_headers.extend(['Total', 'Recognition (%)'])

    # makes an table filled with zeros of #columns = len(the_headers) and #rows = len(class_labels)
    confusion_matrix = [[0] * len(the_headers) for i in range(len(class_labels))]

    # fills out the confusion matrix with the predicted vs. actual
    for a_label_point in labels:
        actual, predicted = a_label_point
        confusion_matrix[class_labels.index(actual)][the_headers.index(predicted)] += 1

    # add the rest of the values to the confusion matrix
    for i in range(len(confusion_matrix)):
        row = confusion_matrix[i]  # current row

        # adding total to the confusion matrix
        total = sum(row)
        row[the_headers.index('Total')] = total  # add the total in for the row

        row[0]= class_labels[i]  # adds the class label for the row to the beginning of row

        # adding recognition to the confusion matrix (% of guesses in row that are correct
        recognition = row[the_headers.index(class_labels[i])] # TP
        recognition /= float(total)
        recognition *= 100
        row[the_headers.index('Recognition (%)')] = recognition

    # prints the table
    print tabulate(confusion_matrix, headers = the_headers, tablefmt="rst")

def stratified_cross_fold(table, k, class_index, classify, *opts):
    """
    Uses stratified crossfolding to predict labels
    :param table: Table of data
    :param k: Number of folds
    :param class_index: the class's index
    :param classify: a function to classify on
    :param opts: anything else you'd like to pass into the classify
    :return: labels in format list of tuples [(actual, predicted),...]
    """

    labels = []
    folds = strat_folds(table, class_index, k)
    for index in range(len(folds)):
        test = folds[index]  # creates the test from one fold
        training = []

        # meshes the rest of the folds together to make the training set
        for training_index in range(len(folds)):
            if training_index != index:
                training.extend(folds[training_index])

        labels.extend(classify(training, test, class_index, *opts))
    return labels

def strat_folds(table, by_label_index, k):
    """
    Creates fold where each fold has the same distrubution of class labels as the origonal table

    :param table: table of data
    :param by_label_index: the class label index
    :param k: the number of partitions to create
    :return: a list of tables where each table is a folds, i.e.: [[P1],[P2],..., [Pnum]] where each P is a table
    """
    labels_to_rows = {}

    # spreads the data out into a dictionary where the key is the class label and the data is a table consisting of
    # rows with that class label {class_label:rows_with_class_label
    for row in table:
        label = row[by_label_index]
        try:
            labels_to_rows[label].append(row)
        except KeyError:
            labels_to_rows[label] = [row]

    # creates folds by evenly distributing the rows of each class label to the number of partitions
    folds = {}
    index = 0
    for key, table in labels_to_rows.iteritems():
        for row in table:
            try:
                folds[index].append(row)
            except KeyError:
                folds[index] = [row]
            index += 1
            if index > k:
                index = 0
    return util.dictionaryToArray(folds)


def getAgeRating(x):
    """ Returns the dept of energy number rating"""

    # Gets the range values for the DOE rankings
    keys     = util.getValues(constants.AGE_RATINGS)

    # Gets the left-end of the range x belongs in
    lowRange = util.getLowRange(keys, x)

    # Flips the dictionary, so we can query by value
    byValue  = util.flipKeyValues(constants.AGE_RATINGS)

    return byValue[lowRange]


def getNHTSASize(x):
    """ Returns the NHTSA Vehicle size """

    # Gets the range values for the DOE rankings
    keys     = util.getValues(constants.NHTSA)

    # Gets the left-end of the range x belongs in
    lowRange = util.getLowRange(keys, x)

    # Flips the dictionary, so we can query by value
    byValue  = util.flipKeyValues(constants.NHTSA)

    return byValue[lowRange]


def convertRowIntoIndexValuePairs(row):
    """ Converts [x, y, z, ...] into [(0, x), (1, y), (2, z)]
    for use in the classifiers in their "where" statements
    """
    return [ (index, value) for index, value in enumerate(row)]


def getNamedTuples(row, names):
    """ Gets a bunch of tuples by their name
    Ex: getNamedColsFromRow(row, 'mpg', 'origin', 'weight')
        might return [(0, 18.0), (4, 3504), (7, 1)]
    WARNING: These don't necessarily return in any specific order.
    """
    tuples = []
    namesIndexes = [constants.INDICES[name] for name in names]
    for index, value in enumerate(row):
        if index in namesIndexes:
            tuples.append((index, value))
    return tuples


def get_survived_value(x):
    """ returns the int value for the nominal value survived

    :param x: a value that is either 'yes' or 'no'
    :return: returns 1 if x is yes, or 0 if x is no
    """
    if x == 'yes':
        return 1
    else:
        return 0

def get_sex_value(x):
    """ returns the int value for the nominal value sex

    :param x: a value that is either 'male' or 'female'
    :return: returns 1 if x is male, or 0 if x is female
    """
    if x == 'male':
        return 1
    else:
        return 0


def get_age_value(x):
    """ returns the int value for the nominal value age

    :param x: a value that is either 'adult' or 'child'
    :return: returns 1 if x is adult, or 0 if x is fchild
    """
    if x == 'adult':
        return 1
    else:
        return 0


def get_class_value(x):
    """ returns the int value for the ordinal value class

    :param x: a value that is either 'crew', 'first', 'second', or 'third'
    :return: returns 3 if 'crew', 2 if first, etc.
    """
    if x == 'crew':
        return 3
    elif x == 'first':
        return 2
    elif x == 'second':
        return 1
    else:
        return 0


"""NEW FINAL PROJECT MAPPING STUFF"""
def get_age(x):
    if age > 90:
        return 1
    elif age <= 90 and age > 70:
        return 2
    elif age <= 70 and age > 50:
        return 2
    else:
        return 0

def get_job_type(x):
    """ returns the int value for the nominal value survived

    :param x: a value that is either 'yes' or 'no'
    :return: returns 1 if x is yes, or 0 if x is no
    """
    if x == 'Government':
        return 1
    elif x == 'Private':
        return 2
    elif x == 'Self-employed':
        return 3
    else:
        return 0

def get_degree(x):
    """ returns the int value for the nominal value sex

    :param x: a value that is either 'male' or 'female'
    :return: returns 1 if x is male, or 0 if x is female
    """
    if x == 'HS':
        return 1
    elif x == 'Bachelors':
        return 2
    elif x == 'Masters':
        return 3
    elif x == 'Doctorate':
        return 4
    elif x == 'College-drop-out':
        return 5
    elif x == 'Associate':
        return 6
    elif x == 'Middleschool':
        return 7
    elif x == 'Elementary':
        return 8
    elif x == 'Prof-school':
        return 9
    else:
        return 0


def get_marital_status(x):
    """ returns the int value for the nominal value age

    :param x: a value that is either 'adult' or 'child'
    :return: returns 1 if x is adult, or 0 if x is fchild
    """
    if x == 'Never-married':
        return 1
    elif x == 'Married-civ-spouse':
        return 2
    elif x == 'Divorced':
        return 3
    elif x == 'Married-spouse-absent':
        return 4
    elif x == 'Widowed':
        return 5
    elif x == 'Separated':
        return 6
    elif x == 'Married-AF-spouse':
        return 7
    else:
        return 0


def get_ethnicity(x):
    """ returns the int value for the ordinal value class

    :param x: a value that is either 'crew', 'first', 'second', or 'third'
    :return: returns 3 if 'crew', 2 if first, etc.
    """
    if x == 'White':
        return 1
    elif x == 'Black':
        return 2
    elif x == 'Amer-Indian-Eskimo':
        return 3
    elif x == 'Asian-Pac-Islander':
        return 4
    else:
        return 0

def get_gender(x):
    """ returns the int value for the ordinal value class

    :param x: a value that is either 'crew', 'first', 'second', or 'third'
    :return: returns 3 if 'crew', 2 if first, etc.
    """
    if x == 'Male':
        return 1
    else:
        return 0

def get_country(x):
    """ returns the int value for the ordinal value class

     :param x: a value that is either 'crew', 'first', 'second', or 'third'
     :return: returns 3 if 'crew', 2 if first, etc.
     """
    if x == 'United-States':
        return 1
    elif x == 'Philippines':
        return 2
    elif x == 'Puerto-Rico':
        return 3
    elif x == 'Mexico':
        return 4
    elif x == 'Dominican-Republic':
        return 5
    elif x == 'Portugal':
        return 6
    elif x == 'Canada':
        return 7
    elif x == 'Taiwan':
        return 8
    elif x == 'Cuba':
        return 9
    elif x == 'Jamaica':
        return 10
    else:
        return 0

def get_salary(x):
    """ returns the int value for the ordinal value class

    :param x: a value that is either 'crew', 'first', 'second', or 'third'
    :return: returns 3 if 'crew', 2 if first, etc.
    """
    if x == '>50K':
        return '1'
    else:
        return '0'

def get_salary_box(x):
    """ returns the int value for the ordinal value class

    :param x: a value that is either 'crew', 'first', 'second', or 'third'
    :return: returns 3 if 'crew', 2 if first, etc.
    """
    if x == '>50K':
        return 1
    else:
        return 0

if __name__ == '__main__':
    row = [18.0,8,307.0,130.0,3504,12.0,70,1,"chevrolet chevelle malibu",2881]
    print getNamedTuples(row, 'mpg', 'origin', 'weight')
