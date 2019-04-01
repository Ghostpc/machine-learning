#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 12:46:39 2019

@author: root
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cv2
import numpy as np
dog=cv2.imread('dog.jpg')
cat=cv2.imread('cat.jpg')
#img2=img*2
add=dog+cat
weighted=cv2.addWeighted(cat,.7,dog,0.3,1)
rev=dog[:,-1,:]
cv2.imshow('win',rev)
cv2.waitKey(0)
