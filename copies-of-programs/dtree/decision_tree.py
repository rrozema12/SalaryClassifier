import table_utils
from util import these, appendToDict
import math

# Key words
ATTRIBUTE = 'Attribute'
VALUE = 'Value'
LEAVES = 'Leaves'

def classify(training, test, class_index, att_indexes, att_domains):
    indexes = att_indexes[:]
    tree = tdidt(training, indexes, att_domains, class_index)

    return [(row[class_index], get_label(tree, row)) for row in test]


def get_label(decision_tree, instance):
    """  predicts the label of the given instance from the decision tree

    :param decision_tree: the decision tree to make the prediction from
    :param instance: a row to predict the class_label of
    :return: the predicted label for the instance
    """
    if decision_tree[0] == 'Leaves':
        # get the predicted class value
        return _majority_voting(decision_tree)
    elif decision_tree[0] == 'Attribute':
        # otherwise we check an attribute
        instance_value = instance[decision_tree[1]]
        for i in range(2, len(decision_tree)):
            if instance_value == decision_tree[i][1]:
                return get_label(decision_tree[i][2], instance)
    else:
        # something is wrong with the tree
        print 'Failed label on ' + instance
        return -1


def _majority_voting(leaves):
    """ Given leaf nodes it will return the most probable class_label

    :param leaves: leaf nodes
    :return: class label
    """
    highest_prob = None
    highest_class_value = None
    for i in range(1, len(leaves)):
        if (highest_prob == None or
                    highest_prob < leaves[i][3]):
            highest_prob = leaves[i][3]
            highest_class_value = leaves[i][0]
    return highest_class_value


def print_rules(tree, names, class_name='class'):
    """ Prints the rules of the tree in the format of
    IF att == val AND ... THEN class = label
    IF att == val AND ... THEN class = label

    :param tree: a decision tree in the format of the tdidt function
    :param names: the names of the indexes
    :param class_name: the names of the class_label
    """
    if tree[0] == 'Leaves':
        _print_rules_helper(tree, '', names, class_name)
    else:
        current_name = names[tree[1]]
        rule = 'IF ' + str(current_name) + ' == '
        for i in range(2, len(tree)):
            new_rule = rule
            current_value = tree[i][1]
            new_rule += str(current_value) + ' '
            _print_rules_helper(tree[i][2], new_rule, names, class_name)


def _print_rules_helper(tree, old_rule, names, class_name):
    """ Prints the rules of the tree in the format of
    IF att == val AND ... THEN class = label
    IF att == val AND ... THEN class = label

    :param tree: a decision tree in the format of the tdidt function
    :param old_rule: the current base rule that the printer is on
    :param names: the names of the indexes
    :param class_name: the names of the class_label
    """
    if tree[0] == 'Leaves':
        print old_rule + 'THEN ' + class_name + ' = ' + _majority_voting(tree)
    else:
        current_name = names[tree[1]]
        rule = 'AND ' + str(current_name) + ' == '
        for i in range(2, len(tree)):
            new_rule = old_rule
            new_rule += rule
            current_value = tree[i][1]
            new_rule += str(current_value) + ' '
            _print_rules_helper(tree[i][2], new_rule, names, class_name)


def tdidt(table, att_indexes, att_domains, class_index):
    """ creates a decision tree for the table
    tree format:
    [`Attribute', `0',
        [`Value', `1', [`Leaves', [`yes',20,20,100%]]]
        [`Value', `2',
            [`Attribute', `2',
                [`Value', `fair',
                    [`Leaves', [`yes',4,10,40%], [`no',6,10,60%]]]
            ]
        ]
    ]

    :param table: a table (assuming it is not empty
    :param att_indexes: the attributes to be partitioned on
    :param att_domains: the values of the corresponding att_domains (in a dict)
    :param class_index: the index of the class_label
    :return: the decision tree
    """
    # First check for if there should be a leaf node
    stats = partition_stats(table, class_index)
    # check to see if there is only one class label present
    # or there are still attributes to partition on
    if same_class(table, class_index) or att_indexes == []:
        return create_leaf_node(stats)

    # check to make sure all partitions have instances
    index = select_best_partition_index(table, att_indexes, class_index)
    partitions = partition_instances(table, index)
    have_instances = True

    if len(att_domains[index]) > len(partitions):
        # this means that there wasn't a partition for one of the attribute values
        return create_leaf_node(stats)

    # Partition Recursion Time!
    att_indexes.remove(index)

    tree = ['Attribute', index]
    for att_value, partition in partitions.items():
        # For each partition will do recursive creation
        subtree = ['Value', att_value]
        subtree.append(tdidt(partition, att_indexes, att_domains,class_index))
        tree.append(subtree)
    return tree


def create_leaf_node(stats):
    """ Creates a leaf node

    :param stats: stats on the partition
    :return: a leaf node in the form ['Leaves', ['yes', 4, 10, 40%],...]
    """
    tree = ['Leaves']
    for row in stats:
        if (row[1] > 0):
            tree.append(row)
    return tree


def same_class(instances, class_index):
    """ Determines if all the instances have the same class label

    :param instances: table
    :param class_index: index of the class label
    :return: True if all have same class label flase otherwise
    """
    label = instances[0][class_index]
    for row in instances:
        if row[class_index] != label:
            return False
    return True


def partition_stats(instances, class_index):
    """ Returns the stas of the class_labels in partition

    :param instances: table
    :param class_index: index of class_label
    :return: list of stats ex:[['yes', 4, 10], ...]
    """

    # Count instances of class label
    counts = {}
    for row in instances:
        class_value = row[class_index]
        try:
            counts[class_value] += 1
        except KeyError:
            counts[class_value] = 1

    # Create stats from count dictionary
    stats = []
    total = len(instances)
    for label, count in counts.iteritems():
        stats.append([str(label), count, total, count / (total * 1.0)])

    return stats


def partition_instances(table, att_index):
    """ partitions the table based on an attribute

    :param table: a table
    :param att_index: the index of attribute to be partitioned on
    :return: dictionary {att_val1: part1, att_val2: part2, ...}
    """
    partitions = {}
    for row in table:
        att_value = row[att_index]
        partitions = appendToDict(partitions, att_value, row)

    return partitions


def select_best_partition_index(instances, att_indexes, class_index):
    """ determines the best attribute to partition on

    :param instances: a table
    :param att_indexes: the indexes of the attributes
    :param class_index: the index of the class_label
    :return: the index of the attribute to partition on
    """
    best_index = None
    lowest_e_new = None

    for index in att_indexes:
        e_new = calc_e_new(instances, index, class_index)
        if lowest_e_new == None or lowest_e_new > e_new:
            lowest_e_new = e_new
            best_index = index

    return best_index


def calc_e_new(instances, att_index, class_index):
    """ calculates Enew for what partitioning on the instnace would give

    :param instances: a table
    :param att_index: index to calculate partition on
    :param class_index: index of the class label
    :return: Enew
    """
    # get the length of the partition
    D = len(instances)
    # calculate the partition stats for att_index (see below)
    freqs = att_freqs(instances, att_index, class_index)
    # find E_new from freqs (calc weighted avg)
    E_new = 0
    for att_val in freqs:
        D_j = float(freqs[att_val][1])
        probs = [(c / D_j) for (_, c) in freqs[att_val][0].items()]
        # changed this to handle when p < 0 because log(anything less than 0)
        # is undefined and will throw an error.
        E_D_j = -sum([p * math.log(p, 2) for p in probs if p > 0])
        E_new += (D_j / D) * E_D_j
    return E_new


def att_freqs(instances, att_index, class_index):
    """ gives the stats the distribution of class_labels given an index

    :param instances: a table
    :param att_index: the index of the attribute to get class_label stats on
    :param class_index: the index of the class_labels
    :return: {att_val:[{class1: freq, class2: freq, ...}, total], ...}
    """
    # get unique list of attribute and class values
    att_vals = list(set(table_utils.getCol(instances, att_index)))
    class_vals = list(set(table_utils.getCol(instances, class_index)))
    # initialize the result
    result = {v: [{c: 0 for c in class_vals}, 0] for v in att_vals}
    # build up the frequencies
    for row in instances:
        label = row[class_index]
        att_val = row[att_index]
        result[att_val][0][label] += 1
        result[att_val][1] += 1
    return result


if __name__ == "__main__":
    table = [[1,1],[1,1],[0,2],[0,2]]
    print partition_stats(table, 1)
