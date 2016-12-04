import naive_bayes as bayes
import table_utils
import file_system
import homework_util as homework
import constants
import partition
import output_util as output
import classifier_util
import hw4_util
import knn


def _printExamples(table):
    """ Prints 5 example instances """
    test, training = partition.cut(table, 5)
    for instance in test:
        output.printInstance(instance)  # Print original instance

        # Calculate the actual and bayes predicted
        actual = instance[constants.INDICES['mpg']]

        # change the instance to the values we are testing from
        instance = homework.getNamedTuples(instance, ['cylinders', 'weight', 'year'])
        predicted, probability = bayes.predict_label(training, instance, constants.INDICES['mpg'])

        output.printClassActual(actual, predicted)  # Print results


def _printAccuracy(table):
    """ Compares subsample accuracy with crossfolding accuracy
    Returns the labels for crossfolding because ...
    """
    test_by_names = ['cylinders', 'weight', 'year']
    output.printHeader('Predicitive Accuracy Naive Bayes')
    accuracy = classifier_util.accuracy(
        hw4_util.random_subsample_naive_bayes(table, 10, constants.INDICES['mpg'], test_by_names))

    print('\tRandom Subsample')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))

    labels = hw4_util.stratified_cross_fold_naive_bayes(table, 10,
                                                        constants.INDICES['mpg'], test_by_names)
    accuracy = classifier_util.accuracy(labels)

    print('\tStratified CrossFolding')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))

    return labels


def _printConfusionMatrix(labels, name):
    """ Prints a confusion matrix for given labels """
    output.printHeader('Confusion Matrix')
    hw4_util.print_confusion_matrix(labels, name)


def step_one(table):
    """ Performs step one of homework 4 """
    output.printHeader("STEP 1: MPG Classified by Naive Bayes for Categorial")

    weight_index = constants.INDICES['weight']
    table = table_utils.mapCol(table, weight_index, homework.getNHTSASize)

    # Part 1 - Print 5 examples
    _printExamples(table)

    # Part 2 - Print Accuracy comparisons
    labels = _printAccuracy(table)

    # Part 3 - Print confusion matrix
    _printConfusionMatrix(labels, 'MPG')


def step_two(table):
    """ Performs step two of homework 4 """
    output.printHeader("STEP 2: Leave 'weight' as a continous attribute")

    # Part 1 - Print examples
    test, training = partition.cut(table, 5)
    for instance in test:
        output.printInstance(instance)  # Print original instance

        # Calculate the actual and bayes predicted
        actual = instance[constants.INDICES['mpg']]

        # change the instance to the values we are testing from
        instance = homework.getNamedTuples(instance, ['cylinders', 'weight', 'year'])
        predicted, probability = bayes.predict_label(training,
            instance, constants.INDICES['mpg'], [constants.INDICES['weight']])

        output.printClassActual(actual, predicted)  # Print results

    # Part 2
    test_by_names = ['cylinders', 'weight', 'year']
    output.printHeader('Predicitive Accuracy Naive Bayes')
    accuracy = classifier_util.accuracy(
        hw4_util.random_subsample_naive_bayes(table, 10, constants.INDICES['mpg'],
                                              test_by_names,
                                              [constants.INDICES['weight']]))

    print('\tRandom Subsample')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))

    labels = hw4_util.stratified_cross_fold_naive_bayes(table, 10, constants.INDICES['mpg'],
                                                        test_by_names,
                                                        [constants.INDICES['weight']])
    accuracy = classifier_util.accuracy(labels)

    print('\tStratified CrossFolding')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))

    _printConfusionMatrix(labels, 'MPG')


def step_three(table):
    """ Analyzes the table based on Knn and Naive Bayes

    :param table: the table of the titanic dataset
    :return: nothing
    """
    output.printHeader("STEP 3: Titanic, Knn vs Naive Bayes")
    table = table_utils.mapCol(table, constants.INDICES['class'],
                               homework.get_class_value)
    table = table_utils.mapCol(table, constants.INDICES['age'],
                               homework.get_age_value)
    table = table_utils.mapCol(table, constants.INDICES['sex'],
                               homework.get_sex_value)
    table = table_utils.mapCol(table, constants.INDICES['survived'],
                               homework.get_survived_value)
    table = knn.normalize_table(table, [1,2,3])

    # KNN
    print('K_NN')

    labels = hw4_util.random_subsample_knn(table, 5, 10, constants.INDICES['survived'])
    accuracy = classifier_util.accuracy(labels)
    print('\tRandom Subsample (5)')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))

    labels = hw4_util.stratified_cross_fold_knn(table, 5, 10, constants.INDICES['survived'])
    accuracy = classifier_util.accuracy(labels)
    print('\tStratified Cross Folds (5)')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))
    _printConfusionMatrix(labels, 'Survived')

    # Naive Bayes
    print('\nNaive Bayes')
    test_by_names = ['class', 'age', 'sex']

    accuracy = classifier_util.accuracy(
        hw4_util.random_subsample_naive_bayes(table, 10, constants.INDICES['survived'],
                                              test_by_names))

    print('\tRandom Subsample')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))

    labels = hw4_util.stratified_cross_fold_naive_bayes(table, 10, constants.INDICES['survived'],
                                                        test_by_names)
    accuracy = classifier_util.accuracy(labels)

    print('\tStratified CrossFolding')
    print('\t\tAccuracy = ' + str(accuracy) + ', error rate = ' + str(1 - accuracy))
    _printConfusionMatrix(labels, 'Survived')




def main():
    table = file_system.loadTable('auto-data-removedNA.csv')

    # Convert the weights in the table to their NHTSA discretization
    mpg_index = constants.INDICES['mpg']
    table = table_utils.mapCol(table, mpg_index, homework.getDeptEnergyRating)

    step_one(table)

    table = file_system.loadTable('auto-data-removedNA.csv')
    table = table_utils.mapCol(table, mpg_index, homework.getDeptEnergyRating)

    step_two(table)

    table = file_system.loadTable('titanic.txt')
    step_three(table)


if __name__ == "__main__":
    main()
