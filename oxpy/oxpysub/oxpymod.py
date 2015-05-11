# Module for Oxford's 'Introduction to Python' course
__author__ = 'tomi'

# Imports

# Functions

def getMin(alist):
    """ Finds the minimum number in a list
    :param alist: a list of numbers
    :return min_num: the number with the minimum value
    """
    min_num = 0
    return min_num

def getMax(alist):
    """ Finds the maximum number in a list
    :param alist: a list of numbers
    :return max_num: the number with the maximum value
    """
    max_num = 0
    return max_num

def sortList(alist):
    """ A modifier function that sorts a list
    :param alist: a list of numbers
    :return:
    """
    bubbleSort(alist)

def bubbleSort(alist):
    """ A modifier function that sorts a list, using the bubble method
    :param alist: a list of numbers
    :return:
    """

def sortListPure(alist):
    """ A pure function that sorts a list
    :param alist: a list of numbers
    :return sortedlist: the same list of numbers, but sorted
    """
    bubbleSortPure(alist)

def bubbleSortPure(alist):
    """ A pure function that sorts a list, using the bubble method
    :param alist: a list of numbers
    :return sortedlist: the same list of numbers, but sorted
    """

def binarySearch(alist, target):
    """ Finds the index at which a number appears in a sorted list, or returns -1
    :param alist: a sorted list of numbers
    :param target: a target number
    :return index: the index at which target appears in alist, or -1 if it does not appear
    """
    index = binarySearchIterative(alist, target)
    return index

def binarySearchIterative(alist, target):
    """ Iterative algorithm that finds the index at which a number appears in a sorted list, or returns -1
    :param alist: a sorted list of numbers
    :param target: a target number
    :return index: the index at which target appears in alist, or -1 if it does not appear
    """
    index = 0
    return index

def binarySearchRecursive(alist, target):
    """ Iterative algorithm that finds the index at which a number appears in a sorted list, or returns -1
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