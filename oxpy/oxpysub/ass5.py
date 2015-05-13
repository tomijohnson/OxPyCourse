# Module for Oxford's 'Introduction to Python' course
__author__ = 'tomi'

# Imports
import ass3
import ass4


def get_data(rfile="data_ass5.txt"):
    datafile = open(rfile, "r")
    inputstring = datafile.readline()
    datafile.close()
    datatoadd = inputstring.strip().split()
    datalist = []
    for i in range(len(datatoadd)):
        datalist.append(float(datatoadd[i]))
    datalist = ass3.sort_list(datalist)
    print "Data loaded from " + rfile
    return datalist


def save_data(datalist, wfile="data_ass5.txt"):
    datafile = open(wfile, "w")
    for item in datalist:
        datafile.write(str(item) + " ")
    datafile.write("\n")
    datafile.close()
    print "Data saved to " + wfile


def print_data(datalist):
    print "The current data are:"
    print datalist


def get_data_loading_prompt_input():
    return raw_input("Would you like to load your previous data (y or Y for yes, otherwise no): ")


def data_loading_prompt(input_func=get_data_loading_prompt_input):
    option = input_func()
    if option == "y" or option == "Y":
        datalist = get_data()
    else:
        datalist = []
    return datalist


def get_data_adding_prompt_input():
    return raw_input("Please enter new values separated by spaces: ")


def data_adding_prompt(datalist, input_func=get_data_adding_prompt_input):
    inputstring = input_func()
    datatoadd = inputstring.split()
    for i in range(len(datatoadd)):
        datalist.append(float(datatoadd[i]))
    datalist = ass3.sort_list(datalist)
    print "Data added. Data are now:"
    print datalist
    return datalist


def get_data_searching_prompt_input():
    return raw_input("What would you like to find? ")


def data_searching_prompt(datalist, input_func=get_data_searching_prompt_input):
    searchoption = input_func()
    index = ass4.binary_search(datalist, float(searchoption))
    if index is None:
        print "The value was not found"
    else:
        print "The value was found at index", index


def get_main_prompt_input():
    return raw_input("What would you like to do?\n" +
                     "(1) View the List\n" +
                     "(2) Add to the list\n" +
                     "(3) Search the list\n" +
                     "(4) Save the list\n" +
                     "(q) Quit the program\n: ")


def main_prompt(datalist, input_func=get_main_prompt_input):
    option = input_func()
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