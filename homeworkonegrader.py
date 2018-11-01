
import os
import homeworkonegraderfinalim
import csv

directory_in_str = os.getcwd()#'/Users/Rebecca/desktop/pythonhomework1'
#print (directory_in_str)
directory = os.fsencode(directory_in_str)#os.getcwd()#os.fsencode(directory_in_str)
#print(directory)

names = ['filename']
grades = [0]
didcheat = ['yesorno']

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".py") and filename != 'homeworkonegrader.py' and filename != 'homeworkonegraderfinalim.py': #filename.endswith(".asm") or filename.endswith(".py"):
        #print(os.path.join(directory, filename))
        #print(filename)
        #print(type(filename))
        grade = homeworkonegraderfinalim.homeworkone(filename)
     #   print (directory)
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
        #print(filename)
        #files = [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:#for file in os.listdir(directory):
            if f.endswith(".py") and f != 'homeworkonegrader.py' and f != 'homeworkonegraderfinalim.py' and filename != f:
              filenamet = os.fsdecode(f)
              #print(filename,filenamet)
              cheat = homeworkonegraderfinalim.checkcheat(filename,filenamet)
              if cheat:
                  didcheat.append('yes'+' '+str(filename)+' '+str(filenamet))
              else:
                  didcheat.append('no')

#grades = list(map(str, grades))

#fullgrades = [' '.join(x) for x in zip(names,grades)]

fullgrades = []

for n in range(len(names)):
    fullgrades.append(str(names[n]) + " " + str(grades[n]) + " " + str(didcheat[n]))

#print(fullgrades)

with open("output.csv", "w") as f:
    writer = csv.writer(f)
    for word in fullgrades:
        writer.writerow([word])
    #writer.writerow([fullgrades])

#for root, dirs, files in os.walk(directory):
    #for file in files:
        #if filename.endswith(".py"): #filename.endswith(".asm") or filename.endswith(".py"):
            # print(os.path.join(directory, filename))
            #print(filename)
            #print(type(filename))
            #homeworkonegraderfinalim.homeworkone(filename)
