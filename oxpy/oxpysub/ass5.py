# Module for Oxford's 'Introduction to Python' course
__author__ = 'tomi'

# Imports
import ass3
import ass4

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
    datalist = ass3.sort_list(datalist)
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
    datalist = ass3.sort_list(datalist)
    print "Data added. Data are now:"
    print datalist
    return datalist


def data_searching_prompt(datalist):
    # get input
    searchoption = str(input("What would you like to find?"))
    # remove new line character
    searchoption.strip()
    # sort and search
    index = ass4.binary_search(datalist, float(searchoption))
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


# Executable code
if __name__ == "__main__":
    # Imports
    import sys

    # Get arguments
    params = sys.argv[1:]

    # Code you wish to run on execution goes here