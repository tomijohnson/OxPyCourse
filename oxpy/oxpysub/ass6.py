# Module for Oxford's 'Introduction to Python' course
__author__ = 'tomi'

# Imports
import ass3
import ass4


def load_from_file(file="data2.txt"):
    """ Creates a student group based on file, and returns that group
    :param file: file that has a student group stored
    :return studentgroup: the student group created from that file
    """
    datafile = open(file, "r")
    linenum = 0
    for line in datafile:
        linenum += 1
        if linenum == 1:
            groupdata = line.strip().split()
            group = StudentGroup(groupdata[0])
            group.maxidy = int(groupdata[1])
        else:
            studentdata = line.strip().split()
            student = Student(int(studentdata[0]), studentdata[1])
            student.active = bool(studentdata[2])
            group.studentlist.append(student)
            for i in range(3, len(studentdata), 2):
                student.grades[studentdata[i]] = float(studentdata[i + 1])
    datafile.close()
    print "Data loaded from " + file
    return group


def make_safe(name):
    """ Takes a string and removes the spaces, replacing them with underscores
    :param name:
    :return name:
    """
    "_".join(name.split())
    return name


def save_data(group):
    group.save_to_file()


def print_data(group):
    print group


def data_loading_prompt():
    option = str(input("Would you like to load your previous student group (y/n):"))
    option = option.strip()
    if option == "y" or option == "Y":
        group = load_from_file()
    else:
        name = str(input("Enter the name of the new group:"))
        name = make_safe(name.strip())
        group = StudentGroup(name)
    return group


def student_adding_prompt(group):
    name = str(input("Please enter new student name:"))
    name = make_safe(name).strip()
    group.add_student(name)
    print "Student added. Group is now:"
    print group


def data_searching_prompt(group):
    searchoption = str(input("Enter the name of the student you want to find:"))
    searchoption.strip()
    students = group.find_student_by_name(searchoption)
    if students == None:
        print "There is no student by that name."
    else:
        print str(len(students)) + " student(s) was(were) found by that name."
        for student in students:
            print student


def exam_result_adding_prompt(group):
    idy = str(input("Enter the student's ID:"))
    idy = int(idy.strip())
    student = group.find_student_by_id(idy)[0]
    inputstring = input("Enter the exams and scores separated by spaces:")
    inputstring.strip()
    datatoadd = inputstring.split()
    for i in range(0,len(datatoadd),2):
        student.update_grades({datatoadd[i]: float(datatoadd[i + 1])})
    print "Exam(s) added. The student's data is now:"
    print student


def main_prompt(group):
    option = str(input("What would you like to do?\n" +
                       "(1) View the group\n" +
                       "(2) Add a student\n" +
                       "(3) Search for a student\n" +
                       "(4) Add an exam result\n" +
                       "(5) Save the group\n" +
                       "(q) Quit the program"))
    option = option.strip()

    if option == "1":
        print_data(group)
        return None
    elif option == "2":
        student_adding_prompt(group)
        return None
    elif option == "3":
        data_searching_prompt(group)
        return None
    elif option == "4":
        exam_result_adding_prompt(group)
    elif option == "5":
        save_data(group)
    elif option == "q":
        return 0
    else:
        print "You did not enter a valid choice."
        return None


def main_program():
    group = data_loading_prompt()
    stop = False
    while stop is False:
        output = main_prompt(group)
        if output is 0:
            stop = True


class Student:
    """ Class for representing and manipulating a student.
    The main data represented are the student's ID,
    name,
    grades,
    and whether the student's status is active.
    """

    def __init__(self, idy, name):
        """ Assign ID and name, make active and create empty dictionary for grades.
        """
        self.idy = idy
        self.name = name
        self.active = True
        self.grades = {}

    def __str__(self):
        text = "ID: " + str(self.idy) + ", Name: " + str(self.name) + ", Active: " + str(self.active) + ", Grades: "
        if len(self.grades) == 0:
            text += "none"
        else:
            for exam in self.grades:
                text += "\n" + str(exam) + ": " + str(self.grades[exam])
        return text

    def print_simple(self):
        text = str(self.idy) + " " + str(self.name) + " " + str(self.active)
        for exam in self.grades:
            text += " " + str(exam) + " " + str(self.grades[exam])
        return text

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
    The main data represented are a the name of the group,
    the max ID number assigned so far,
    and a list Students.
    """

    def __init__(self, name):
        """ Assign name and create empty dictionary for the list.
        """
        self.name = name
        self.maxidy = -1
        self.studentlist = []

    def __str__(self):
        text = "Name: " + str(self.name) + ", Max ID: " + str(self.maxidy) + ", Students: "
        if len(self.studentlist) == 0:
            text += "none"
        else:
            for student in self.studentlist:
                text += "\n" + str(student)
        return text

    def print_simple(self):
        return str(self.name) + " " + str(self.maxidy)

    def get_name(self):
        return self.name

    def get_maxidy(self):
        return self.maxidy

    def get_studentlist(self):
        return self.studentlist

    def add_student(self, name):
        student = Student(self.maxidy + 1, name)
        self.studentlist.append(student)
        self.maxidy += 1
        return student

    def save_to_file(self, file="data2.txt"):
        datafile = open(file, "w")
        datafile.write(self.print_simple())
        for student in self.studentlist:
            datafile.write("\n" + student.print_simple())
        datafile.close()
        print "Data saved to " + file

    def find_student_by_id(self, idy):
        found = False
        students = []
        i = 0
        while i < len(self.studentlist) and found is False:
            if self.studentlist[i].idy == idy:
                students += [self.studentlist[i]]
                found = True
            i += 1
        return students

    def find_student_by_name(self, name):
        found = False
        students = []
        i = 0
        while i < len(self.studentlist) and found is False:
            if self.studentlist[i].name == name:
                students += [self.studentlist[i]]
                found = True
            i += 1
        return students

    def delete_student(self, student):
        deleted = False
        i = 0
        while i < len(self.studentlist) and deleted is False:
            if self.studentlist[i] is student:
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