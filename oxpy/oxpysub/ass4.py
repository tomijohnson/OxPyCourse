# Module for Oxford's 'Introduction to Python' course
__author__ = 'tomi'


def linear_search_iterative(alist, target):
    """ Iteratively finds the first index at which a number appears in a sorted list, or returns -1
    :param alist: a sorted list of numbers
    :param target: a target number
    :return index: the index at which target appears in alist, or -1 if it does not appear
    """
    index_target = None
    found = False
    index_current = 0
    while index_current < len(alist) and found is False:
        if alist[index_current] == target:
            index_target = index_current
            found = True
        index_current += 1
    return index_target


def binary_search(alist, target):
    """ Finds the first index at which a number appears in a sorted list, or returns -1
    :param alist: a sorted list of numbers
    :param target: a target number
    :return index: the index at which target appears in alist, or -1 if it does not appear
    """
    index = binary_search_iterative(alist, target)
    return index


def binary_search_iterative(alist, target):
    """ Iteratively finds the first index at which a number appears in a sorted list, or returns -1
    :param alist: a sorted list of numbers
    :param target: a target number
    :return index: the index at which target appears in alist, or -1 if it does not appear
    """
    index_target = None
    found = False
    start = 0
    end = len(alist)
    while found is False:
        range_len = end - start
        index_current = start + range_len//2 - 1
        if range_len <= 1:
            if range_len == 1 and alist[start] == target:
                index_target = start
                found = True
            else:
                found = True
        elif alist[index_current] < target:
            start = index_current + 1
        else:
            end = index_current + 1
    return index_target


def binary_search_recursive(alist, target, start=0, end=-1):
    """ Recursively finds the first index at which a number appears in a sorted list, or returns -1
    :param alist: a sorted list of numbers
    :param target: a target number
    :return index: the index at which target appears in alist, or -1 if it does not appear
    """
    if end == -1:
        end = len(alist)
    range_len = end - start
    if range_len <= 1:
        if range_len == 1 and alist[start] == target:
            return start
        else:
            return None
    else:
        if alist[start + range_len//2 - 1] < target:
            return binary_search_recursive(alist, target, start + range_len//2, end)
        else:
            return binary_search_recursive(alist, target, start, start + range_len//2)


# Executable code
if __name__ == "__main__":
    # Imports
    import sys

    # Get arguments
    params = sys.argv[1:]

    # Code you wish to run on execution goes here