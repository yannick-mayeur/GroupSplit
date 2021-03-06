#!/usr/bin/env python3

import numpy as np
import csv
import sys
import itertools

if len(sys.argv) < 2:
    raise RuntimeError("You must specify the -EXT")

ext = sys.argv[1][1:]

donneeBrut = np.genfromtxt('../DONNEES/preferences' + ext + '.csv', dtype=str, delimiter=',')

fakeRepartition = [
    [21706894, 21505186, 21712798],
    [20144769, 21507122, 21502642],
    [21705472, 21000002, 21712227],
    [21507151, 21708799]
]

def sortMarks(marks):
    """Return sorted marks

    The order is: TB > B > AB > P > I > AR
    """
    sortHelper = []
    for mark in marks:
        if mark == "TB":
            sortHelper.append(0)
        elif mark == "B":
            sortHelper.append(1)
        elif mark == "AB":
            sortHelper.append(2)
        elif mark == "P":
            sortHelper.append(3)
        elif mark == "I":
            sortHelper.append(4)
        elif mark == "AR":
            sortHelper.append(5)
    return [x for _,x in sorted(zip(sortHelper,marks))]

def getNumberOf3Group(size):
    """Return the number of groups of 3

    Function minimizes the number of groups of 2
    """
    if size%3 == 0:
        return int(size/3)
    if size%3 == 1:
        return int((size-4)/3)
    if size%3 == 2:
        return int((size-2)/3)

def getNumberOf2Group(size):
    """Return the number of groups of 2

    Function minimizes the number of groups of 2
    """
    if size%3 == 0:
        return 0
    if size%3 == 1:
        return 2
    if size%3 == 2:
        return 1


def getNoteeWithMark(noter, mark):
    """Return a list of Notees that Noter noted with mark"""
    i = -1
    isFound = False
    while i < (len(donneeBrut[0])-1) and not isFound:
        i += 1
        if noter ==  donneeBrut[i][0]:
            isFound = True
    result = []
    j = -1
    isFound = False
    while j < (len(donneeBrut)-1) and not isFound:
        j += 1
        if mark == donneeBrut[i][j]:
            result.append(donneeBrut[0][j])
    return result

def getRepartitionMark(repartition):
    """Return mark of the Repartition
    The mark is calculated by taking the median mark
    """
    marks = []
    for group in repartition:
        marks.extend(getMarksOfGroup(group))
    medianIndex = int(len(marks)/2)
    return sortMarks(marks)[medianIndex]


def getMarksOfGroup(group):
    """Return mark group members gave other members"""
    result = []
    for noter in group:
        for notee in group:
            mark = getMarkOfFor(str(noter), str(notee))
            if mark != "-1":
                result.append(mark)
    return result


def getMarkOfFor(noter, notee):
    """Return mark of noter for notee"""
    i = -1
    isFound = False
    while i < (len(donneeBrut[0])-1) and not isFound:
        i += 1
        if noter ==  donneeBrut[i][0]:
            isFound = True
    result = []
    j = -1
    isFound = False
    while j < (len(donneeBrut)-1) and not isFound:
        j += 1
        if notee ==  donneeBrut[0][j]:
            isFound = True
    return donneeBrut[i][j]

def compare(mark1, mark2):
    """Return comparison between params
    1 if mark1 > mark2
    -1 if mark1 < mark2
    = if mark1 = mark2
    """
    c1 = 0
    c2 = 0
    if mark1 == "TB":
        c1 = 5
    elif mark1 == "B":
        c1 = 4
    elif mark1 == "AB":
        c1 = 3
    elif mark1 == "P":
        c1 = 2
    elif mark1 == "I":
        c1 = 1
    elif mark == "AR":
        c1 = 1
    if mark2 == "TB":
        c2 = 5
    elif mark2 == "B":
        c2 = 4
    elif mark2 == "AB":
        c2 = 3
    elif mark2 == "P":
        c2 = 2
    elif mark2 == "I":
        c2 = 1
    elif mark2 == "AR":
        c2 = 0
    if c1 > c2:
        return 1
    elif c1 < c2:
        return -1
    return 0

def bestRepartition(repartitions):
    """Return list of equally best repartitions"""
    best = []
    best.append(repartitions[0])
    i = 0
    while i < (len(repartitions)-1):
        i += 1
        if compare(getRepartitionMark(repartitions[i]), best[0][0]) == 1:
            best = []
            best.append((getRepartitionMark(repartitions[i]), repartitions[i]))
        elif compare(getRepartitionMark(repartitions[i]), best[0][0]) == 0:
            best.append((getRepartitionMark(repartitions[i]), repartitions[i]))
    return best

def algoPermu(people):
    """Return all possible groups"""
    nb2 = getNumberOf2Group(len(people))
    nb3 = getNumberOf3Group(len(people))
    permu = list(itertools.permutations(people, r = len(people)))
    res = []
    for r in permu:
        r = list(r)
        res.append([])
        for i in range(nb2):
            item = [r.pop(), r.pop()]
            item.sort()
            res[-1].append(item)
        for i in range(nb3):
            item = [r.pop(), r.pop(), r.pop()]
            item.sort()
            res[-1].append(item)
    uniqueRes = []
    for elem in res:
        if elem not in uniqueRes:
            uniqueRes.append(elem)
    return uniqueRes

people = donneeBrut[0][1:]
res = algoPermu(people)
res = bestRepartition(res) 
final = []
stringbuilder = " "
for r in res:
    for item in r[1]:
        stringbuilder += ' '.join(map(str, item))
    stringbuilder += '; '
    stringbuilder = stringbuilder[:-2]
    stringbuilder += '\n '

with open('BFM.csv', 'w+') as the_file:
    the_file.write(stringbuilder)
