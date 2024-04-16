# Objective:
# The aim of this assignment is to create a program that tracks fitness activities and calories burned.

# Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = [’Dancing’, ‘Swimming’, ‘Biking’] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and Biking corresponds to 15 minutes.

activities=[]
durations=[]

def add_activity():
    new_activity=input("Enter your activity: ")
    activity_duration=input("Enter the duration(in minutes): ")
    activities.append(new_activity)
    durations.append(int(activity_duration))

# Task 2: Write a simple function that estimates calories burned based on the activity and duration. For instance, Total calories burned = Duration (in minutes)*3.5
def calculate_calories(duration):
    return duration*3.5

# Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.
def display_summary():
    total_calories=0
    for i in range(0,len(activities)):
        total_calories+=calculate_calories(durations[i])
        print(f"{activities[i]} for a duration of {durations[i]} minutes. Calories burned: {calculate_calories(durations[i])}")
    print(f"Total calories burned today: {total_calories}")

while True:
    print("Enter \"1\" To Add An Activity")
    print("Enter \"2\" To See The Summary")
    print("Enter \"3\" To Exit")
    action = int(input())
    if action==1:
        add_activity()
    elif action==2:
        display_summary()
    elif action==3:
        print("Exiting")
        break
    else:
        print("Not a valid choice.")
