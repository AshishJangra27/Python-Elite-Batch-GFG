# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-Fp4rmRldYwZbzXXp4uPdfuquTITcuwO
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

block = [[0,0,0,0,0,0,0],
         [0,1,1,1,1,1,0],
         [0,1,0,0,0,1,0],
         [0,1,0,0,0,1,0],
         [0,1,0,0,0,1,0],
         [0,1,1,1,1,1,0],
         [0,0,0,0,0,0,0]]

qr = np.ones((7,27),dtype=int)

qr[:,1:8] = block
qr[:,19:26] = block

for i in qr:
  print(i)

ms = []
for i in 'google':
  sp = []
  for j in (bin(ord(i)).replace('b','')):
    sp.append(j)
  ms.append(sp)

print(ms)

np.array(ms).shape

qr[:-1,9:17] = ms

for i in qr:
  print(i)

plt.imshow(qr)

for i in qr[:-1,9:17]:
  print(i)

cv.imwrite("qr.png",qr)

qr = qr*255

for i in "Hello":
  print(chr(ord(i)+5))