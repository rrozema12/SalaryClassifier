#Department of energy ratings
DOE_RATINGS = {
    10: 45,
    9: 37,
    8: 31,
    7: 27,
    6: 24,
    5: 20,
    4: 17,
    3: 15,
    2: 14,
    1: 0
}

ORIGINS = {
    1 : "USA",
    2 : "Europe",
    3 : "Japan"
}

INDICES = {
    'mpg'          : 0,  # auto-data dataset
    'cylinders'    : 1,
    'displacement' : 2,
    'horsepower'   : 3,
    'weight'       : 4,
    'acceleration' : 5,
    'year'         : 6,
    'origin'       : 7,
    'name'         : 8,
    'msrp'         : 9,

    # It's a stupid idea to merge these.
    # He could throw a new dataset at us and then this
    # becomes unusable
    'class'        : 0,  # titanic dataset
    'age'          : 1,
    'sex'          : 2,
    'survived'     : 3
}

WISCONSIN = {
    'clump_thickness'   : 0,
    'cell_size'         : 1,
    'cell_shape'        : 2,
    'marginal_adhesion' : 3,
    'epithelial_size'   : 4,
    'bare_nuclei'       : 5,
    'bland_chromatin'   : 6,
    'normal_nucleoli'   : 7,
    'mitoses'           : 8,
    'tumor'             : 9
}

NHTSA = {
    5 : 3500,
    4 : 3000,
    3 : 2500,
    2 : 2000,
    1 : 0
}

AUTO_HEADERS = [
    'mpg', 'cylinders', 'displacement', 'horsepower', 'weight',
    'acceleration', 'modelyear', 'origin', 'carname', 'msrp'
]

TITANIC_HEADERS = [
    'class', 'age', 'sex', 'survived'
]
