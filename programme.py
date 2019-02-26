#!/usr/bin/env python3

import numpy as np
import itertools
import matplotlib.pyplot as plt

donneeBrut = np.genfromtxt('preferences.csv', dtype=str, delimiter=',')

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
    """Return a tuple of form (number of groups of 3, number of groups of 2)

    Function minimizes the number of groups of 2
    """
    if size%3 == 0:
        return int(size/3)
    if size%3 == 1:
        return int((size-4)/3)
    if size%3 == 2:
        return int((size-2)/3)

def getNumberOf2Group(size):
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

def bruteForceRepatition(personnes):
    i = 0
    for group in list(itertools.combinations(personnes, r = 3)):
        group = list(group)
        pCopy = [x for x in personnes if x not in group]
        for item in list(itertools.combinations(pCopy, r = 3)):
            item = list(item)
            seen = (group + item)
            pCopy2 = [x for x in personnes if x not in seen]
            for item2 in list(itertools.combinations(pCopy2, r = 3)):
                item2 = list(item2)
                seen = (group + item + item2)
                pCopy3 = [x for x in personnes if x not in seen]
                for item3 in list(itertools.combinations(pCopy3, r = 2)):
                    item3 = list(item3)
                    i += 1
                    print(group, item, item2, item3)

# print(getNoteeWithMark("21708799", "I"))
# print(getMarkOfFor("21706894", "21505186"))
# print(getMarksOfGroup(fakeRepartition[0]))
# print(getRepartitionMark(fakeRepartition))
# print(getNumberOf3Group(10))
# print(getNumberOf3Group(11))
# print(getNumberOf3Group(12))
# print(getNumberOf3Group(13))
bruteForceRepatition(donneeBrut[0][1:])
# print(list(itertools.combinations(donneeBrut[0][1:], r = 3)))
