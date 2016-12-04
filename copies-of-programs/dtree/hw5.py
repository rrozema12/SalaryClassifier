import table_utils
import file_system
import homework_util as homework
from constants import INDICES
from constants import TITANIC_HEADERS
from constants import AUTO_HEADERS
import output_util as output
import decision_tree
from util import these, flipKeyValues
from functools import partial
from classifier_util import accuracy


def map_to_ints_titanic(table):
    """ Maps the data_set to integer values

    :param table: titanic dataset
    :return: returns the mapped dataset
    """
    table = table_utils.mapCol(table, INDICES['class'],
                               homework.get_class_value)
    table = table_utils.mapCol(table, INDICES['age'],
                               homework.get_age_value)
    table = table_utils.mapCol(table, INDICES['sex'],
                               homework.get_sex_value)
    table = table_utils.mapCol(table, INDICES['survived'],
                               homework.get_survived_value)

    return table

def map_auto_cols(table):
    mpg_index = INDICES['mpg']
    table = table_utils.mapCol(table, mpg_index, homework.getDeptEnergyRating)
    weight_index = INDICES['weight']
    table = table_utils.mapCol(table, weight_index, homework.getNHTSASize)

    return table


def step_one(table):
    """ Decision Tree vs. Knn (k=10) for titanic data_set

    :param: titanic dataset
    :return: the decision tree
    """

    output.printHeader('Step One: Create a Decision Tree (Titanic)')

    attributes = these(INDICES, 'class', 'age', 'sex')
    domains = table_utils.get_domains(table, attributes)
    tree = decision_tree.tdidt(table, attributes, domains, INDICES['survived'])

    decision_tree.print_rules(tree, ['class', 'age', 'sex', 'survived'],
                              'survived')

    attributes = these(INDICES, 'class', 'age', 'sex')

    # Creates a myClassifier function that's paritally filled out
    # From decision_tree.classify
    # Essentially a new function:
    # myClassifier(training, test, class_index)
    myClassifier = partial(decision_tree.classify, att_indexes=attributes, att_domains=domains)

    labels = homework.stratified_cross_fold(table, 10, INDICES['survived'],
       myClassifier)

    acc = accuracy(labels)
    print('\n')
    print('Stratified CrossFolding')
    print('\tAccuracy = ' + str(acc) + ', error rate = ' + str(1 - acc))
    print('\n')

    # Confusion Matrix
    homework.print_confusion_matrix(labels, 'Survived')


def step_two(table):
    """ Decision Tree vs. Knn (k=10) for auto data_set

    :param: titanic dataset
    :return: the decision tree
    """
    output.printHeader('Step Two: Create a Decision Tree (Auto)')


    # Discretize Weight
    mpg_index = INDICES['mpg']
    table = table_utils.mapCol(table, mpg_index, homework.getDeptEnergyRating)
    weight_index = INDICES['weight']
    table = table_utils.mapCol(table, weight_index, homework.getNHTSASize)

    # Print tree
    attributes = these(INDICES, 'weight', 'cylinders', 'year')
    domains = table_utils.get_domains(table, attributes)
    tree = decision_tree.tdidt(table, attributes, domains, INDICES['mpg'])
    decision_tree.print_rules(tree, AUTO_HEADERS, 'mpg')

    attributes = these(INDICES, 'cylinders', 'weight', 'year')

    # Creates a myClassifier function that's paritally filled out
    # From decision_tree.classify
    # Essentially a new function:
    # myClassifier(training, test, class_index)
    myClassifier = partial(decision_tree.classify, att_indexes=attributes, att_domains=domains)

    labels = homework.stratified_cross_fold(table, 10, INDICES['mpg'],
       myClassifier)

    acc = accuracy(labels)
    print('\n')
    print('Stratified CrossFolding')
    print('\tAccuracy = ' + str(acc) + ', error rate = ' + str(1 - acc))
    print('\n')

    # Confusion Matrix
    labels = [(index, int(value)) for index, value in labels] #converts to ints
    homework.print_confusion_matrix(labels, 'Mpg')


def main():
    table = file_system.loadTable('titanic.txt')
    titanic_tree = step_one(table)

    table = file_system.loadTable('auto-data-removedNA.csv')
    step_two(table)


if __name__ == "__main__":
    main()
