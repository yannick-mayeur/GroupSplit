#!/usr/bin/env python3

import numpy as np

donneeBrut = np.genfromtxt('preferences.csv', dtype=str, delimiter=',')

for ligne in donneeBrut:
  for item in ligne:
    print(item)
