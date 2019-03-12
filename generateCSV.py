from random import *
import math
import csv

note = ["TB"]
nbEtu = 12
students = [ [ "" for y in range( nbEtu + 1) ] for x in range( nbEtu + 1) ]
names = ["", 1,2,3,4,5,6,7,8,9,10, 11, 12] 
# ["", 21706894,21505186,21712798,20144769,21507122,21502642,21705472,21000002,21712227,21507151,21708799,21507879,21506945,21710720,21506961,21506147,21503233,21712091,21707432,21503981,21404529,21500572,20134250,21712084,21513144,21000001,21708325,21602558,20140777,21707228,21502689,21504350,21710385,21504427,21500179,20140524,21507221,21501136,21505282,21703318]

for i in range(1,nbEtu+1) :
    for j in range(0,nbEtu+1) :
        if(j == 0):
            students[i][j] = names[i]
        elif(i == j):
            students[i][j] = -1
        else :
            students[i][j] = note[math.floor(random()*len(note))]

with open('preferencesL10TB.csv', mode='w') as preferences_file:
    employee_writer = csv.writer(preferences_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    employee_writer.writerow(names)
    for i in range(1,nbEtu+1) :
        employee_writer.writerow(students[i])
