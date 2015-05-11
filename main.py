__author__ = 'tomi'

# Imports (creating a module within a subpackage within a package is unnecessary, but something I wanted to try)
import oxpy.oxpysub.oxpymod as oxpy

# Functions
def templateFunction(inputs):
    """ Description goes here
    :param inputs:
    :return:
    """
    return 0

def assignment2():
    """ Demonstrates the completion of Assignment 2
    :param None:
    :return None:
    """
    print "--- Starting Assignment 2 ---"
    alist = [0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9]
    print "List of numbers:", alist
    print "Min function returns:", oxpy.getMin(alist), "Expecting:", -45
    print "Max function returns:", oxpy.getMax(alist), "Expecting:", 34
    print "--- Finished Assignment 2 ---"

def assignment3():
    """ Demonstrates the completion of Assignment 3
    :param None:
    :return None:
    """
    print "--- Starting Assignment 3 ---"
    alist = [0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9]
    print "List of numbers:", alist
    print "Sort function returns:", oxpy.sortList(alist), "Expecting", [ -45,-1, 0, 3, 8, 9, 9, 12, 21.9, 34]
    print "--- Finished Assignment 3 ---"

# Classes

# Main function
def main():
    assignment2()
    assignment3()

    # Tests that may be deleted
    print oxpy.getMinRecursive([1, 2, 3])
    print oxpy.getMaxRecursive([1, 2, 3])
    a = [2, 1, 3]
    print oxpy.sortListPure(a)
    print a
main()