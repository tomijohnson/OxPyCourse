# Module for Oxford's 'Introduction to Python' course, assignment 2
__author__ = 'tomi'


def get_min(alist, method="iterative"):
    """ Finds the minimum number in a list
    :param alist: a list of numbers
    :param method: the method to use
    :return min_num: the number with the minimum value
    """
    if method == "iterative":
        min_num = get_min_iterative(alist)
    elif method == "recursive":
        min_num = get_min_recursive(alist)
    else:
        print "In getMin, method", method, "not recognised. Using iterative..."
        min_num = get_min_iterative(alist)
    return min_num


def get_min_iterative(alist):
    """ Iteratively finds the minimum number in a list
    :param alist: a list of numbers
    :return min_num: the number with the minimum value
    """
    if len(alist) == 0:
        return None
    else:
        min_num = alist[0]
        for i in range(1, len(alist)):
            if alist[i] < min_num:
                min_num = alist[i]
        return min_num


def get_min_recursive(alist):
    """ Recursively finds the minimum number in a list
    :param alist: a list of numbers
    :return: the number with the minimum value
    """
    if len(alist) <= 2:
        if len(alist) <= 1:
            if len(alist) == 1:
                return alist[0]
            else:
                return None
        elif alist[0] < alist[1]:
            return alist[0]
        else:
            return alist[1]
    else:
        next_level = get_min_recursive(alist[1:])
        if alist[0] < next_level:
            return alist[0]
        else:
            return next_level


def get_max(alist, method="iterative"):
    """ Finds the maximum number in a list
    :param alist: a list of numbers
    :param method: the method to use
    :return max_num: the number with the maximum value
    """
    if method == "iterative":
        max_num = get_max_iterative(alist)
    elif method == "recursive":
        max_num = get_max_recursive(alist)
    else:
        print "In getMax, method", method, "not recognised. Using iterative..."
        max_num = get_max_iterative(alist)
    return max_num


def get_max_iterative(alist):
    """ Iteratively finds the maximum number in a list
    :param alist: a list of numbers
    :return max_num: the number with the maximum value
    """
    if len(alist) == 0:
        return None
    else:
        max_num = alist[0]
        for i in range(1, len(alist)):
            if alist[i] > max_num:
                max_num = alist[i]
        return max_num


def get_max_recursive(alist):
    """ Recursively finds the maximum number in a list
    :param alist: a list of numbers
    :return max_num: the number with the maximum value
    """
    if len(alist) <= 2:
        if len(alist) <= 1:
            if len(alist) == 1:
                return alist[0]
            else:
                return None
        elif alist[0] > alist[1]:
            return alist[0]
        else:
            return alist[1]
    else:
        next_level = get_max_recursive(alist[1:])
        if alist[0] > next_level:
            return alist[0]
        else:
            return next_level


# Executable code
if __name__ == "__main__":
    # Imports
    import sys

    # Get arguments
    params = sys.argv[1:]

    # Code you wish to run on execution goes here