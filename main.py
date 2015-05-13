__author__ = 'tomi'

# Imports (creating modules within a subpackage within a package is unnecessary, but something I wanted to try)
import oxpy.oxpysub.ass2 as ass2
import oxpy.oxpysub.ass3 as ass3
import oxpy.oxpysub.ass4 as ass4
import oxpy.oxpysub.ass5 as ass5
import oxpy.oxpysub.ass6 as ass6


# Functions
def assignment2():
    """ Demonstrates the completion of Assignment 2
    """
    print "--- Starting Assignment 2 ---"
    alist = [0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9]
    print "List of numbers:", alist
    print "Min function returns:", ass2.get_min(alist), "Expecting:", -45
    print "Max function returns:", ass2.get_max(alist), "Expecting:", 34
    print "--- Finished Assignment 2 ---"


def assignment3():
    """ Demonstrates the completion of Assignment 3
    """
    print "--- Starting Assignment 3 ---"
    alist = [0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9]
    print "List of numbers:", alist
    print "Sort function returns:", ass3.sort_list(alist), "Expecting", [-45, -1, 0, 3, 8, 9, 9, 12, 21.9, 34]
    print "--- Finished Assignment 3 ---"


def assignment4():
    """ Demonstrates the completion of Assignment 4
    """
    print "--- Starting Assignment 4 ---"
    alist = [0, -1, 9, 34, -45, 8, 12, 3, 9, 21.9]
    alist = ass3.sort_list(alist)
    print "List of numbers:", alist
    print "Searching for 12 returns:", ass4.binary_search(alist, 12), "Expecting", 7
    print "Searching for 9 returns:", ass4.binary_search(alist, 9), "Expecting", 5
    print "--- Finished Assignment 4 ---"


def assignment5():
    """ Demonstrates the completion of Assignment 5
    """
    print "--- Starting Assignment 5 ---"
    ass5.main_program()
    print "--- Finished Assignment 5 ---"


def assignment6():
    """ Demonstrates the completion of Assignment 6
    """
    print "--- Starting Assignment 6 ---"
    ass6.main_program()
    print "--- Finished Assignment 6 ---"


# Main function
def main():
    """ Runs the assignment demonstrations in order
    """
    assignment2()
    assignment3()
    assignment4()
    assignment6()

main()