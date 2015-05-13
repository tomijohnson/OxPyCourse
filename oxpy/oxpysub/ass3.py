# Module for Oxford's 'Introduction to Python' course
__author__ = 'tomi'


def sort_list(alist, ftype="modifier"):
    """ A function that sorts a list
    :param alist: a list of numbers
    :param ftype: the type of function
    :return None:
    """
    if ftype == "modifier":
        return sort_list_modifier(alist)
    elif ftype == "pure":
        return sort_list_pure(alist)
    else:
        print "In sortList,type", ftype, "not recognised. Using modifier..."
        return sort_list_modifier(alist)


def sort_list_modifier(alist):
    """ A modifier function that sorts a list
    :param alist: a list of numbers
    :return: the same list of numbers, but sorted
    """
    return bubble_sort(alist)


def bubble_sort(alist):
    """ A modifier function that sorts a list, using the bubble method
    :param alist: a list of numbers
    :return: the same list of numbers, but sorted
    """
    return bubble_sort_iterative(alist)


def bubble_sort_iterative(alist):
    """ An iterative modifier function that sorts a list, using the bubble method
    :param alist: a list of numbers
    :return alist: the same list of numbers, but sorted
    """
    n = len(alist)
    while n > 0:
        new_n = 0
        for i in range(1, n):
            if alist[i - 1] > alist[i]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
                new_n = i
        n = new_n
    return alist


def sort_list_pure(alist):
    """ A pure function that sorts a list
    :param alist: a list of numbers
    :return sortedlist: a copy of the same list of numbers, but sorted
    """
    # Copy rather than create alias
    sortedlist = alist[:]
    sort_list(sortedlist)
    return sortedlist


# Executable code
if __name__ == "__main__":
    # Imports
    import sys

    # Get arguments
    params = sys.argv[1:]

    # Code you wish to run on execution goes here