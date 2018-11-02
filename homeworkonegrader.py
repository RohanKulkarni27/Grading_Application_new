
import os
import homeworkonegraderfinalim
import csv

directory_in_str = os.getcwd()
directory = os.fsencode(directory_in_str)

names = ['filename']
grades = [0]
didcheat = ['yesorno']

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".py") and filename != 'homeworkonegrader.py' and filename != 'homeworkonegraderfinalim.py':
        grade = homeworkonegraderfinalim.homeworkone(filename)
        print(grade)
        names.append(filename)
        grades.append(grade)
        continue
    else:
        continue

files = [f for f in os.listdir('.') if os.path.isfile(f)]

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".py") and filename != 'homeworkonegrader.py' and filename != 'homeworkonegraderfinalim.py':
        for f in files:
            if f.endswith(".py") and f != 'homeworkonegrader.py' and f != 'homeworkonegraderfinalim.py' and filename != f:
              filenamet = os.fsdecode(f)
              cheat = homeworkonegraderfinalim.checkcheat(filename,filenamet)
              if cheat:
                  didcheat.append('yes'+' '+str(filename)+' '+str(filenamet))
              else:
                  didcheat.append('no')
                    
fullgrades = []

for n in range(len(names)):
    fullgrades.append(str(names[n]) + " " + str(grades[n]) + " " + str(didcheat[n]))


with open("output.csv", "w") as f:
    writer = csv.writer(f)
    for word in fullgrades:
        writer.writerow([word])
