#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

donneeBrut = np.genfromtxt('preferences.csv', dtype=str, delimiter=',')

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


print(getNoteeWithMark("21708799", "I"))
