import csv
import matplotlib.pyplot as plt
import re

# Headers
date = 0
muscleGroup = 1
workout = 2
weight = 3
reps = 4

# Muscle Groups
legs = "Legs"
chest = "Chest"
back = "Back"
abs = "Abs"
bicep = "Bicep"
tricep = "Tricep"
shoulders = "Shoulders"

def Brzycki(weight, reps):
    weight = float(weight)
    reps = float(reps)
    return weight / (1.0278 - 0.0278 * reps)

file = open('workout.csv')
csvreader = csv.reader(file)
next(csvreader) # skip headers

workingSets = []
for row in csvreader:
    if any(row): # dont append if row empty
        workingSets.append(row)
file.close()

x = [] # x axis
y = [] # y axis
dates = []
index = 0

workoutSearch = input("Workout: ")
my_regex = r"\b(?=\w)" + workoutSearch + r"\b(?!\w)"

for set in workingSets:
    if re.search(r'(?i)\bbench\b', set[workout]):
        oneRepPred = Brzycki(set[weight], set[reps])
        # print(set[date] + ' ' + str(oneRepPred))
        y.append(oneRepPred)
        dates.append(set[date])
        x.append(index)
        index += 1
        

# Graph by predicted 1RM to account for changing weight and volume

plt.title(workoutSearch)
plt.xticks(ticks = x, labels = dates)
plt.plot(x, y)
plt.ylabel("One Rep Prediction")
plt.xlabel("Date")

plt.show()