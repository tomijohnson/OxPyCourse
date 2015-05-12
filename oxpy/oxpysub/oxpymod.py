# Module for Oxford's 'Introduction to Python' course
__author__ = 'tomi'


# Functions
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
            return alist
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
            return alist
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


def linear_search_iterative(alist, target):
    """ Iteratively finds the first index at which a number appears in a sorted list, or returns -1
    :param alist: a sorted list of numbers
    :param target: a target number
    :return index: the index at which target appears in alist, or -1 if it does not appear
    """
    index_target = -1
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
    index_target = -1
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
            return -1
    else:
        if alist[start + range_len//2 - 1] < target:
            return binary_search_recursive(alist, target, start + range_len//2, end)
        else:
            return binary_search_recursive(alist, target, start, start + range_len//2)


def get_data():
    # open the file
    datafile = open("data.txt", "r")
    # read the first line the file must be sorted and separated by a space
    inputstring = datafile.readline()
    # close the file
    datafile.close()
    # remove the new line character
    inputstring.strip()
    # split the data into a list
    datatoadd = inputstring.split()
    datalist = []
    for i in range(len(datatoadd)):
        datalist.append(float(datatoadd[i]))
    datalist = sort_list(datalist)
    print "Data loaded from data.txt"
    return datalist


def save_data(datalist):
    # open the file
    datafile = open("data.txt", "w")
    # write list all one line separated by spaces
    for item in datalist:
        datafile.write(str(item) + " ")
    datafile.write("\n")
    # close the file
    datafile.close()
    print "Data saved to data.txt"


def print_data(datalist):
    print "The current data are:"
    print datalist


def data_loading_prompt():
    option = str(input("Would you like to load your previous data (y/n):"))
    # strip the new line character and any extraneous white space
    option = option.strip()
    if option == "y" or option == "Y":
        datalist = get_data()
    else:
        datalist = []
    return datalist


def data_adding_prompt(datalist):
    # get input
    inputstring = str(input("Please enter new values separated by spaces:"))
    # remove new line character
    inputstring.strip()
    # split the string
    datatoadd = inputstring.split()
    for i in range(len(datatoadd)):
        datalist.append(float(datatoadd[i]))
    datalist = sort_list(datalist)
    print "Data added. Data are now:"
    print datalist
    return datalist


def data_searching_prompt(datalist):
    # get input
    searchoption = str(input("What would you like to find?"))
    # remove new line character
    searchoption.strip()
    # sort and search
    index = binary_search(datalist, float(searchoption))
    if index > -1:
        print("The value was found at index", index)
    else:
        print("The value was not found")


def main_prompt(datalist):
    option = str(input("What would you like to do?\n" +
                       "(1) View the List\n" +
                       "(2) Add to the list\n" +
                       "(3) Search the list\n" +
                       "(4) Save the list\n" +
                       "(q) Quit the program"))
    option = option.strip()

    if option == "1":
        print_data(datalist)
        return datalist
    elif option == "2":
        datalist = data_adding_prompt(datalist)
        return datalist
    elif option == "3":
        data_searching_prompt(datalist)
        return datalist
    elif option == "4":
        save_data(datalist)
        return datalist
    elif option == "q":
        return None
    else:
        print "You did not enter a valid choice."
        return datalist


def main_program():
    datalist = data_loading_prompt()
    stop = False
    while stop is False:
        datalist = main_prompt(datalist)
        if datalist is None:
            stop = True


# Classes
class Student:
    """ Class for representing and manipulating a Student.
    The main data represented are the student's ID,
    name,
    grades,
    and whether the student is active"""

    def __init__(self, idy, name):
        """ Assign ID and name, make active and create empty dictionary for grades. """
        self.idy = idy
        self.name = name
        self.active = True
        self.grades = {}

    def get_idy(self):
        return self.idy

    def get_name(self):
        return self.name

    def is_active(self):
        return self.active

    def get_grades(self):
        return self.grades

    def get_grade(self, exam):
        return self.grades[exam]

    def update_grades(self, grades):
        self.grades.update(grades)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def get_grade_average(self):
        average = 0
        for exam in self.grades:
            average += self.grades[exam]
        average /= len(self.grades)
        return average

    def get_exams(self):
        return self.grades.keys()


class StudentGroup:
    """ Class for representing and manipulating a Student Group.
    The main data represented are a dictionary of Students with ID numbers as keys,
    and a name for the group"""

    def __init__(self, name):
        """ Assign name and create empty dictionary for the list. """
        self.name = name
        self.studentlist = []
        self.maxidy = 0

    def get_name(self):
        return self.name

    def get_studentlist(self):
        return self.studentlist

    def add_student(self, name):
        self.studentlist.append(Student(self.maxidy + 1, name))
        self.maxidy += self.maxidy

    def find_student_by_id(self, idy):
        found = False
        student = None
        i = 0
        while i < len(self.studentlist) and found is False:
            if self.studentlist[i].idy == idy:
                student = self.studentlist[i]
                found = True
                i += 1
        return student

    def find_student_by_name(self, name):
        found = False
        student = None
        i = 0
        while i < len(self.studentlist) and found is False:
            if self.studentlist[i].name == name:
                student = self.studentlist[i]
                found = True
                i += 1
        return student

    def delete_student_by_id(self, idy):
        deleted = False
        i = 0
        while i < len(self.studentlist) and deleted is False:
            if self.studentlist[i].idy == idy:
                del self.studentlist[i]
                deleted = True
                i += 1

    def delete_student_by_name(self, name):
        deleted = False
        i = 0
        while i < len(self.studentlist) and deleted is False:
            if self.studentlist[i].name == name:
                del self.studentlist[i]
                deleted = True
                i += 1

# Executable code
if __name__ == "__main__":
    # Imports
    import sys

    # Get arguments
    params = sys.argv[1:]

    # Code you wish to run on execution goes here