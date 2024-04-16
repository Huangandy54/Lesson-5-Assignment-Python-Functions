# Objective:
# The aim of this assignment is to analyze a set of grades and provide statistics.

# Task 1: Code a function to calculate the average grade.
def calculate_average(grades):
    return sum(grades)/len(grades)

# Task 2: Implement a function to find the highest and lowest grade.
def find_max(grades):
    return max(grades)

def find_min(grades):
    return min(grades)

# Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).
def letter_grades(grades):
    letter_list=[]
    for grade in grades:
        if grade >= 90:
            letter_list.append("A")
        elif grade >= 80 :
            letter_list.append("B")
        elif grade >= 70 :
            letter_list.append("C")
        elif grade >= 60 :
            letter_list.append("D")
        else:
            letter_list.append("F")
    return letter_list

# example list of grades
grades=[90, 80, 88, 94, 83, 75, 72, 65, 60, 59, 57]

print("List of grades being analyzed: ", grades)

while True:
    print("Enter \"1\" To Calculate The Average")
    print("Enter \"2\" To Find The Highest Grade")
    print("Enter \"3\" To Find The Lowest Grade")
    print("Enter \"4\" To Display Grades In Letter Grade")
    print("Enter \"5\" To Exit")
    action = int(input())
    if action==1:
        print("The Average is: ", calculate_average(grades))
    elif action==2:
        print("The Highest Grade is: " + str(find_max(grades)))
    elif action==3:
        print("The Lowest Grade is: " + str(find_min(grades)))
    elif action==4:
        print("Displaying Letter Grades...\n", letter_grades(grades))
    elif action==5:
        print("Exiting")
        break
    else:
        print("Not a valid choice.")