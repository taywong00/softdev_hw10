# TIC TAC
# Carol Pan and Taylor Wong
# SoftDev1 pd7
# HW10 -- Average
# 2017-10-17

#==========================================================
import sqlite3   #enable control of an sqlite database

f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================

# STEPS TO THE HW
'''1. Look up each student's grades'''
command = "SELECT name,mark FROM peeps,courses WHERE peeps.id=courses.id"
stu_info = c.execute(command)

# create a dictionary of grades
grades = {}

for info in stu_info:
    name = info[0]
    mark = info[1]
    if name in grades:
        grades[name].append(mark)
    else:
        grades[name] = []
        grades[name].append(mark)

'''
print "TEST: "
for key in grades:
    print key + ": "
    print grades[key]
'''

'''2. Compute each student's average'''
def average(lst):
    total = 0;
    for item in lst:
        total += float(item)
    avg = total / len(lst)
    return avg

for name in grades:
    avg = average(grades[name])
    grades[name].insert(0, avg) #the first value in the grade dict is the avg

'''
print "TEST: "
for key in grades:
    print key + ": "
    print grades[key]
'''


'''3. Display each student's name, id, and average'''
command = "SELECT name,id FROM peeps"
stu_ids = c.execute(command)

for info in stu_ids:
    name = info[0]
    id = info[1]
    if name in grades:
        grades[name].insert(0, id)
    else:
        grades[name] = []
        grades[name].insert(0, id) #first value in the grade dict is now the id, second is the avg

#display info
for key in grades: #key = name #note: must change floats/int avgs to str type in order to concatinate
    print "\n\nNAME: " + key + "\nID: " + str(grades[key][0]) + "\nAVERAGE: " + str(grades[key][1])


'''4. Create a table of IDs and associated averages'''
'''
print "TEST: "
for key in grades:
    print key + ": "
    print grades[key]
'''

try:
    command = "CREATE TABLE peeps_avg (id INTEGER PRIMARY KEY, average NUMERIC)"
    c.execute(command)
except:
    print "TABLE AVERAGES ALREADY EXISTS"


for key in grades:
    command = "INSERT INTO peeps_avg VALUES(" + str(grades[key][0]) + "," + str(grades[key][1]) +")"
    c.execute(command)
    #print str(grades[key][0])
    #print str(grades[key][1])
#except:
#    print "INSERTED VALUES ALREADY EXIST"
