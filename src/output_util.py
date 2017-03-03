# output_util.py
# helps pretty print things

def _getInstanceString(instance):
    """ Get the array as a comma seperated string """
    return ''.join(str(i)+', ' for i in instance).strip()[:-1]

def printInstance(instance):
    print 'instance:', _getInstanceString(instance)

def printClassActual(actualValue, classValue):
    print 'class:', classValue, 'actual:', actualValue

def printHeader(text):
    print ' '
    print '==========================================='
    print text
    print '==========================================='

def printDivider():
    print '-------------------------------------------'
