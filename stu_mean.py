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


print "TEST: "
for key in grades:
    print key + ": "
    print grades[key]



'''2. Compute each student's average'''




'''3. Display each student's name, id, and average'''
