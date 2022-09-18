# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 21:02:06 2022

@author: soumy
"""

import cv2

img = cv2.imread(r'C:\Users\soumy\Pictures\StateFlow_tutorial_Robot_Vacuum_bug.png', cv2.IMREAD_COLOR)
img = cv2.resize(img, (400, 300))
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()