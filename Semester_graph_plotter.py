import matplotlib.pyplot as plt
import sys

#You could use array, but simply using lists is more efficient
courses = []
grades = []

#This functions adds the name of the new course to the list and simultaneously asks for the respective grade, to save lines
#And returns the new list of grades and courses
def addCourses():
    new_course=input("Name of the course: ")
    new_grade= int(input("Grade of the course: "))
    if new_grade<0 or new_grade>20:
        print("Invalid value")
    else:    
        courses.append(new_course)
        grades.append(new_grade)
    return courses,grades


def plot():
    
    plt.bar(courses, grades)

    plt.ylim(bottom=0, top=20) #Sets the limits of the grid

    #Simple syntax that evaluates the grade
    for x in range(len(grades)):
     if grades[x]>= 15 and grades[x]<=20:
         plt.bar(x, grades[x], color='green')
     if grades[x]>=10 and grades[x] <15:
         plt.bar(x, grades[x], color='yellow')
     if grades[x]<10: plt.bar(x, grades[x], color= 'red')
        

    plt.title=("1st semestre plot")
    plt.xlabel=("Course")
    plt.ylabel=("Grade")
    plt.show()


def interface():
#We'll add several options
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
    
       
#Main function
if __name__ == "__main__": 
    
    while True:
        interface()
   