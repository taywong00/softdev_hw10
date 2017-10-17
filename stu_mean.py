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
def populate(stu_info, grades = {}):
    for info in stu_info:
        name = info[0] #to include name
        mark = info[1] #and mark
        if name in grades:
            grades[name].append(mark) #add to mark list of marks
        else:
            grades[name] = [] #list to hold marks
            grades[name].append(mark) #add in mark
    return grades

grades = populate(stu_info)

'''
print "TEST: "
for key in grades:
    print key + ": "
    print grades[key]
'''

'''2. Compute each student's average'''
#computes average given a list
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
#insert id corresponding to name
command = "SELECT name,id FROM peeps"
stu_ids = c.execute(command)

for info in stu_ids:
    name = info[0]
    id = info[1]
    if name in grades:
        grades[name].insert(0, id) #insert id if name is already a key
        #first value in the grade dict is now the id, second is the avg
    else:
        grades[name] = []
        grades[name].insert(0, id) 

#display info
for key in grades: #key = name #note: must change floats/int avgs to str type in order to concatinate
    print "\n\nNAME: " + key + "\nID: " + str(grades[key][0]) + "\nAVERAGE: " + str(grades[key][1])


'''4. Create a table of IDs and associated averages'''

#in case table has already been created
try:
    command = "CREATE TABLE peeps_avg (id INTEGER PRIMARY KEY, average NUMERIC)"
    c.execute(command)
except:
    print "TABLE AVERAGES ALREADY EXISTS"

#in case values have already been inserted
for key in grades:
    try:
        command = "INSERT INTO peeps_avg VALUES(" + str(grades[key][0]) + "," + str(grades[key][1]) + ")"
        #print command
        c.execute(command)
    except:
        print "INSERTED VALUES ALREADY EXIST"

'''5. Facilitate updating a student's average'''

def update_avg():
    for key in grades:
        #get all values not id and avg
        comp_list = grades[key][2: ]
        avg = average(comp_list)
        #replace now obsolete avg
        grades[key].pop(1)
        grades[key].insert(1, avg)
    return

update_avg()
'''
print "TEST: "
for key in grades:
    print key + ": "
    print grades[key]
'''
    

'''6. Facilitate adding rows to the courses table'''


#==========================================================
db.commit()
db.close()
