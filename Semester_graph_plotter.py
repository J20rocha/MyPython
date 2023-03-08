import matplotlib.pyplot as plt
import numpy as np
import sys

#You could use array, but simply using lists is more efficient
courses = []
grades = []

#This functions adds the name of the new course to the list and simultaneously asks for the respective grade, to save lines
#And returns the new list of grades and courses
def addCourses():
    new_course=input("Name of the course: ")
    new_grade= input("Grade of the course: ")
    courses.append(str(new_course))
    grades.append(str(new_grade))
    return courses,grades
     


def plot():
    plt.title=("1st semestre plot")
    plt.xlabel=("Course")
    plt.ylabel=("Grade")
    #The bar starts at the lowest valu. Fix this later
    plt.ylim(ymin=0, ymax=20)
    plt.bar(courses, grades)
    plt.show()


def interface():

    print("0. Exit")
    print("1. Add courses.")
    print("2. Plot")
    option = input("Choose option ")

    if str(option) == "0":
        sys.exit()
    if str(option) == "1":
        addCourses()

    if str(option) == "2":
        plot()
    else:
        print("Invalid option")
    
       

if __name__ == "__main__": 
    
    while True:
        interface()
   