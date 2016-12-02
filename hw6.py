import table_utils
import file_system
import homework_util as homework
from constants import INDICES
from random_forest import run_a_table
import output_util as output
from classifier_util import accuracy
from decision_tree import classify
from homework_util import print_confusion_matrix


def map_auto_cols(table):
    """ Discretizes the auto_table

    :param table: the auto_table
    :return: discretized table
    """
    mpg_index = INDICES['mpg']
    table = table_utils.mapCol(table, mpg_index, homework.getDeptEnergyRating)
    weight_index = INDICES['weight']
    table = table_utils.mapCol(table, weight_index, homework.getNHTSASize)

    return table


def step_two(auto_table, titanic_table):
    output.printHeader('Step Two: N = 20, M = 7, F = 2')
    # Titanic stuff
    titanic_indexes = [INDICES['age'], INDICES['sex'], INDICES['class']]
    titanic_domains = table_utils.get_domains(titanic_table, titanic_indexes)
    titanic_forest_labels, titanic_train, titanic_test = \
                run_a_table(titanic_table, titanic_indexes,
                    INDICES['survived'], 20, 7, 2)
    titanic_forest_accuray = accuracy(titanic_forest_labels)
    titanic_tree_labels = classify(titanic_train, titanic_test,
                                   INDICES['survived'], titanic_indexes,
                                   titanic_domains)
    titanic_tree_accuracy = accuracy(titanic_tree_labels)

    print('Titanic:')
    print('\tRandom Forest')
    print('\t\tAccuracy = ' + str(titanic_forest_accuray))
    print_confusion_matrix(titanic_forest_labels, 'SURVIVED')
    print('\tDecision Tree')
    print('\t\tAccuracy = ' + str(titanic_tree_accuracy))
    print_confusion_matrix(titanic_tree_labels, 'SURVIVED')

    # auto stuff
    auto_indexes = [INDICES['cylinders'], INDICES['weight'], INDICES['year']]
    auto_domains = table_utils.get_domains(auto_table, auto_indexes)
    auto_forest_labels, auto_train, auto_test = run_a_table(auto_table, auto_indexes,
                    INDICES['mpg'], 20, 7, 2)
    auto_forest_accuray = accuracy(auto_forest_labels)
    auto_tree_labels = classify(auto_train, auto_test,
                                   INDICES['mpg'], auto_indexes,
                                   auto_domains)
    auto_tree_accuracy = accuracy(auto_tree_labels)

    print('Auto:')
    print('\tRandom Forest')
    print('\t\tAccuracy = ' + str(auto_forest_accuray))
    print_confusion_matrix(auto_forest_labels, 'MPG')
    print('\tDecision Tree')
    print('\t\tAccuracy = ' + str(auto_tree_accuracy))
    print_confusion_matrix(auto_tree_labels, 'MPG')


def step_three(auto_table, titanic_table, n, m, f):
    output.printHeader('Step Three: Vary N, M, and F')
    print("N = " + str(n) + " M = " + str(m) + " F = " + str(f))
    # Titanic stuff
    titanic_indexes = [INDICES['age'], INDICES['sex'], INDICES['class']]
    titanic_domains = table_utils.get_domains(titanic_table, titanic_indexes)
    titanic_forest_labels, titanic_train, titanic_test = \
                run_a_table(titanic_table, titanic_indexes,
                    INDICES['survived'], n, m, f)
    titanic_forest_accuray = accuracy(titanic_forest_labels)
    titanic_tree_labels = classify(titanic_train, titanic_test,
                                   INDICES['survived'], titanic_indexes,
                                   titanic_domains)
    titanic_tree_accuracy = accuracy(titanic_tree_labels)

    print('Titanic:')
    print('\tRandom Forest')
    print('\t\tAccuracy = ' + str(titanic_forest_accuray))
    print_confusion_matrix(titanic_forest_labels, 'SURVIVED')
    print('\tDecision Tree')
    print('\t\tAccuracy = ' + str(titanic_tree_accuracy))
    print_confusion_matrix(titanic_tree_labels, 'SURVIVED')

    # auto stuff
    auto_indexes = [INDICES['cylinders'], INDICES['weight'], INDICES['year']]
    auto_domains = table_utils.get_domains(auto_table, auto_indexes)
    auto_forest_labels, auto_train, auto_test = run_a_table(auto_table, auto_indexes,
                    INDICES['mpg'], n, m, f)
    auto_forest_accuray = accuracy(auto_forest_labels)
    auto_tree_labels = classify(auto_train, auto_test,
                                   INDICES['mpg'], auto_indexes,
                                   auto_domains)
    auto_tree_accuracy = accuracy(auto_tree_labels)

    print('Auto:')
    print('\tRandom Forest')
    print('\t\tAccuracy = ' + str(auto_forest_accuray))
    print_confusion_matrix(auto_forest_labels, 'MPG')
    print('\tDecision Tree')
    print('\t\tAccuracy = ' + str(auto_tree_accuracy))
    print_confusion_matrix(auto_tree_labels, 'MPG')


def main():
    titanic_table = file_system.loadTable('titanic.txt')
    auto_table = map_auto_cols(file_system.loadTable('auto-data-removedNA.csv'))

    step_two(auto_table, titanic_table)

    #Each of these N, M, and F values were tested 10 times to find the accuracy
    #score for the Random Forest.

    # 1000, 800, 2 = 76-77%
    # 1500, 1000, 2 = 71-77%
    # 800, 200, 3 = 75-77%
    # 400, 300, 3 = 76-77% (most consistently 77%, the winner out of the tested sets)
    # 3000, 2000, 1 = 71-77%
    # 3000, 1500, 2 = 72-77%
    # 1000, 750, 3 = 75-77%
    # 600, 200, 3 = 71-76 #
    step_three(auto_table, titanic_table, 400, 300, 3)
if __name__ == "__main__":
    main()
