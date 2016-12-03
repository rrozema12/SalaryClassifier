# data-mining-homework-1
This is our project. Be good to it.

```
//
//                       _oo0oo_
//                      o8888888o
//                      88" . "88
//                      (| -_- |)
//                      0\  =  /0
//                    ___/`---'\___
//                  .' \\|     |// '.
//                 / \\|||  :  |||// \
//                / _||||| -:- |||||- \
//               |   | \\\  -  /// |   |
//               | \_|  ''\---/''  |_/ |
//               \  .-\__  '-'  ___/-. /
//             ___'. .'  /--.--\  `. .'___
//          ."" '<  `.___\_<|>_/___.' >' "".
//         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
//         \  \ `_.   \_ __\ /__ _/   .-` /  /
//     =====`-.____`.___ \_____/___.-`___.-'=====
//                       `=---='

```

# Wiki
The project is split up into many "util" modules to help keep organized.

### Rules:
1. If you're making a new classifier, put it in it's own module.
2. Use `module-level private` functions with a single underscore `_myPrivate()`
3. Delete things. (It's all saved to git anyway)
4. Comment (I haven't been so good about this), and add to wiki if you make
a new module

### Guidelines:
1. If you can be general, be general. For example:

```
# BAD
def getMPGs():
  ...

# GOOD
def getColByName():
  """ getColByName('mpg') """
  ...
```


## Modules
A list of modules.

### util.py
Hyper general functions that don't fall into any of the below
categories.

#### Good utility function:
```
def dictionaryToArray(dictionary):
    return [ value for key, value in dictionary.iteritems()]
```

#### Bad utility function:
```
def normalizeTable(table, exceptFor=None):
  ...
```

### constants.py
Only for constant variables. No functions please.

### file_system.py
Only for reading/writing files.

### math_utils.py
Only for math. Just math math math math.

### table_utils.py
For manipulating a 2d array (table).

### hwX_util.py
`hw<number>.py` is to be used for utilities specific to a single homework
assignment. Becareful with this. Don't abuse this.

### homework_util.py
Put functions in here that are specific to a homework assignment. If you ask
yourself the question "Would I need this in a personal project?" and you
say "no", then put it in `homework_util`. Don't abuse this. Be more general
if you can.

### naive_bayes.py
This is the naive_bayes module. Duh?

### knn.py
Contains functions pertaining to knn

### classifier_util.py
This is utilities that can apply to any classifier. For example: accuracy,
error rate, ect.

### partition.py
If you're splitting up a table, put it here
