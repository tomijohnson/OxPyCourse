# Module for Oxford's 'Introduction to Python' course
__author__ = 'tomi'

# Imports

# Functions
def getMin(alist, method="iterative"):
    """ Finds the minimum number in a list
    :param alist: a list of numbers
    :param method: the method to use
    :return min_num: the number with the minimum value
    """
    if method == "iterative":
        min_num = getMinIterative(alist)
    elif method == "recursive":
        min_num = getMinRecursive(alist)
    else:
        print "In getMin, method", method, "not recognised. Using iterative..."
        min_num = getMinIterative(alist)
    return min_num

def getMinIterative(alist):
    """ Iteratively finds the minimum number in a list
    :param alist: a list of numbers
    :return min_num: the number with the minimum value
    """
    min_num = alist[0]
    for i in range(1,len(alist)):
        if alist[i] < min_num:
            min_num = alist[i]
    return min_num

def getMinRecursive(alist):
    """ Recursively finds the minimum number in a list
    :param alist: a list of numbers
    :return: the number with the minimum value
    """
    if len(alist) <= 2:
        if len(alist) <= 1:
            return alist
        elif alist[0] < alist[1]:
            return alist[0]
        else:
            return alist[1]
    else:
        next_level = getMinRecursive(alist[1:])
        if alist[0] < next_level:
            return alist[0]
        else:
            return next_level

def getMax(alist, method="iterative"):
    """ Finds the maximum number in a list
    :param alist: a list of numbers
    :param method: the method to use
    :return max_num: the number with the maximum value
    """
    if method == "iterative":
        max_num = getMaxIterative(alist)
    elif method == "recursive":
        max_num = getMaxRecursive(alist)
    else:
        print "In getMax, method", method, "not recognised. Using iterative..."
        max_num = getMaxIterative(alist)
    return max_num

def getMaxIterative(alist):
    """ Iteratively finds the maximum number in a list
    :param alist: a list of numbers
    :return max_num: the number with the maximum value
    """
    max_num = alist[0]
    for i in range(1,len(alist)):
        if alist[i] > max_num:
            max_num = alist[i]
    return max_num

def getMaxRecursive(alist):
    """ Recursively finds the maximum number in a list
    :param alist: a list of numbers
    :return max_num: the number with the maximum value
    """
    if len(alist) <= 2:
        if len(alist) <= 1:
            return alist
        elif alist[0] > alist[1]:
            return alist[0]
        else:
            return alist[1]
    else:
        next_level = getMaxRecursive(alist[1:])
        if alist[0] > next_level:
            return alist[0]
        else:
            return next_level

def sortList(alist, type="modifier"):
    """ A function that sorts a list
    :param alist: a list of numbers
    :param type: the type of function
    :return None:
    """
    if type == "modifier":
        return sortListModifier(alist)
    elif type == "pure":
        return sortListPure(alist)
    else:
        print "In sortList,type", type, "not recognised. Using modifier..."
        return sortListModifier(alist)

def sortListModifier(alist):
    """ A modifier function that sorts a list
    :param alist: a list of numbers
    :return: the same list of numbers, but sorted
    """
    return bubbleSort(alist)

def bubbleSort(alist):
    """ A modifier function that sorts a list, using the bubble method
    :param alist: a list of numbers
    :return: the same list of numbers, but sorted
    """
    return bubbleSortIterative(alist)

def bubbleSortIterative(alist):
    """ An iterative modifier function that sorts a list, using the bubble method
    :param alist: a list of numbers
    :return alist: the same list of numbers, but sorted
    """
    n = len(alist)
    while n > 0:
        new_n = 0
        for i in range(1,n):
            if alist[i - 1] > alist[i]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                new_n = i
        n = new_n
    return alist

def sortListPure(alist):
    """ A pure function that sorts a list
    :param alist: a list of numbers
    :return sortedlist: a copy of the same list of numbers, but sorted
    """
    sortedlist = alist[:] # Copy rather than create alias
    sortList(sortedlist)
    return sortedlist

def binarySearch(alist, target):
    """ Finds the index at which a number appears in a sorted list, or returns -1
    :param alist: a sorted list of numbers
    :param target: a target number
    :return index: the index at which target appears in alist, or -1 if it does not appear
    """
    index = binarySearchIterative(alist, target)
    return index

def binarySearchIterative(alist, target):
    """ Iteratively finds the index at which a number appears in a sorted list, or returns -1
    :param alist: a sorted list of numbers
    :param target: a target number
    :return index: the index at which target appears in alist, or -1 if it does not appear
    """
    index = 0
    return index

def binarySearchRecursive(alist, target):
    """ Recursively finds the index at which a number appears in a sorted list, or returns -1
    :param alist: a sorted list of numbers
    :param target: a target number
    :return index: the index at which target appears in alist, or -1 if it does not appear
    """
    index = 0
    return index

# Classes

# Executable code
if __name__ == "__main__":
    # Imports
    import sys

    # Get arguments
    params = sys.argv[1:]

    # Code you wish to run on execution goes here